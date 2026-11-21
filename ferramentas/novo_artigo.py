#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publica um artigo novo do site leeadv.com.br a partir de um arquivo .md.

O arquivo de entrada mora FORA do repositorio, numa pasta irma, e o caminho
dele e argumento do programa. Nada do que este programa le entra no site sem
passar pelas validacoes da funcao validar().

ETAPAS. O programa tem tres, e nunca envia nada para a main:

    testar    le a entrada, valida e mostra na tela o que seria gerado.
              Nao escreve nada em disco. E o padrao.
    preparar  cria o ramo, escreve os arquivos e abre o pull request.
              NAO IMPLEMENTADO: passo 4.
    conferir  roda depois do merge, confere o ar por endereco e, se algo
              falhar, abre um pull request de reversao.
              NAO IMPLEMENTADO: passo 5.

A separacao existe porque conferir precisa rodar depois que outra pessoa
juntou o pull request, e nao em seguida a preparar. Sao dois momentos, duas
invocacoes e dois resultados possiveis independentes.

Biblioteca padrao apenas, por decisao do projeto: o site nao tem etapa de
construcao e nao ha onde instalar dependencia.
"""

import argparse
import datetime
import os
import re
import sys
import unicodedata

# --------------------------------------------------------------------------
# Onde as coisas ficam
# --------------------------------------------------------------------------

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELO = os.path.join(RAIZ, "artigos", "_template.html")
INDICE = os.path.join(RAIZ, "artigos", "index.html")
SITEMAP = os.path.join(RAIZ, "sitemap.xml")
PASTA_ARTIGOS = os.path.join(RAIZ, "artigos")

BASE = "https://leeadv.com.br"
PREFIXO = BASE + "/artigos/"

# --------------------------------------------------------------------------
# Limites de validacao. Estao aqui em cima, juntos, para serem discutidos
# sem ler o resto do arquivo.
# --------------------------------------------------------------------------

CAMPOS_OBRIGATORIOS = (
    "endereco", "titulo_aba", "descricao", "h1",
    "resumo_indice", "data_publicacao", "data_atualizacao", "fecho",
)
CAMPOS_OPCIONAIS = ("leia_tambem",)

ENDERECO_MIN_PALAVRAS = 3
ENDERECO_MAX_PALAVRAS = 6
TITULO_MAX = 60
DESCRICAO_MIN = 150
DESCRICAO_MAX = 160
CORPO_MIN_PALAVRAS = 700
CORPO_MAX_PALAVRAS = 1200
QUANTOS_LEIA_TAMBEM = 2

# Deteccao de bloco de perguntas e respostas. Heuristica: nomes usados para
# a secao, e a marcacao de dados estruturados aposentada.
SINAIS_DE_PERGUNTAS = (
    "perguntas frequentes", "perguntas e respostas", "duvidas frequentes",
    "faqpage", "acceptedanswer", "\"@type\": \"question\"",
)

# Verbos no imperativo mais comuns em texto de captacao. HEURISTICA, nao
# analise gramatical: pega o caso comum, nao todos. Uma frase de fecho que
# passe aqui ainda pode precisar de olho humano.
IMPERATIVOS = (
    "fale", "ligue", "clique", "acesse", "agende", "marque", "contrate",
    "chame", "mande", "envie", "peca", "peça", "solicite", "escreva",
    "procure", "consulte", "conte", "venha", "descubra", "saiba", "veja",
    "confira", "aproveite", "garanta", "conheca", "conheça", "entre",
    "nao perca", "não perca", "fique", "comece", "resolva", "evite",
)

MESES = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro")

# Os onze marcadores do modelo, na ordem em que a documentacao dele os lista.
MARCADORES = (
    "{{TITLE}}", "{{DESCRIPTION}}", "{{CANONICAL}}", "{{H1}}",
    "{{DATA_PUBLICACAO}}", "{{DATA_PUBLICACAO_ISO}}",
    "{{DATA_ATUALIZACAO}}", "{{DATA_ATUALIZACAO_ISO}}",
    "{{CORPO}}", "{{FECHO}}", "{{ITENS_LEIA_TAMBEM}}",
)

LIMITE_INICIO = "<!-- #LEIA-TAMBEM:INICIO -->"
LIMITE_FIM = "<!-- #LEIA-TAMBEM:FIM -->"


class ErroDeEntrada(Exception):
    """Entrada invalida. A mensagem e para o operador, em portugues."""


# --------------------------------------------------------------------------
# Leitura
# --------------------------------------------------------------------------

def ler_entrada(caminho):
    """Devolve (cabecalho, corpo) do .md. Nao valida nada."""
    if not os.path.isfile(caminho):
        raise ErroDeEntrada("Arquivo de entrada nao encontrado: %s" % caminho)
    with open(caminho, encoding="utf-8") as f:
        texto = f.read().replace("\r\n", "\n")

    linhas = texto.split("\n")
    if not linhas or linhas[0].strip() != "---":
        raise ErroDeEntrada(
            "O arquivo tem de comecar com uma linha de tres hifens, que abre "
            "o cabecalho.")
    try:
        fim = linhas.index("---", 1)
    except ValueError:
        raise ErroDeEntrada(
            "O cabecalho foi aberto e nao foi fechado: falta a segunda linha "
            "de tres hifens.")

    cabecalho = {}
    for n, linha in enumerate(linhas[1:fim], start=2):
        if not linha.strip():
            continue
        if ":" not in linha:
            raise ErroDeEntrada(
                "Linha %d do cabecalho sem dois-pontos: %r" % (n, linha))
        chave, valor = linha.split(":", 1)
        chave = chave.strip()
        if chave in cabecalho:
            raise ErroDeEntrada("Campo repetido no cabecalho: %s" % chave)
        cabecalho[chave] = valor.strip()

    corpo = "\n".join(linhas[fim + 1:]).strip()
    return cabecalho, corpo


# --------------------------------------------------------------------------
# Validacao. Devolve lista de problemas; lista vazia quer dizer aprovado.
# Nada e escrito em disco por nenhuma funcao daqui.
# --------------------------------------------------------------------------

def _sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def _palavras_do_corpo(corpo):
    sem_titulo = re.sub(r"(?m)^#+ .*$", " ", corpo)
    return len(sem_titulo.split())


def _e_iso(valor):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", valor or ""):
        return False
    try:
        datetime.date.fromisoformat(valor)
    except ValueError:
        return False
    return True


def validar(cabecalho, corpo, pasta_artigos=PASTA_ARTIGOS):
    problemas = []

    # 1. campos obrigatorios presentes e nao vazios
    for campo in CAMPOS_OBRIGATORIOS:
        if campo not in cabecalho:
            problemas.append("Campo obrigatorio ausente no cabecalho: %s" % campo)
        elif not cabecalho[campo].strip():
            problemas.append("Campo obrigatorio vazio no cabecalho: %s" % campo)
    desconhecidos = set(cabecalho) - set(CAMPOS_OBRIGATORIOS) - set(CAMPOS_OPCIONAIS)
    for campo in sorted(desconhecidos):
        problemas.append(
            "Campo que o programa nao conhece, e por isso ignoraria em "
            "silencio: %s" % campo)

    # 2. endereco
    endereco = cabecalho.get("endereco", "").strip()
    if endereco:
        if endereco != endereco.lower():
            problemas.append("O endereco tem letra maiuscula: %s" % endereco)
        if endereco != _sem_acento(endereco):
            problemas.append("O endereco tem acento: %s" % endereco)
        if " " in endereco:
            problemas.append("O endereco tem espaco: %s" % endereco)
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", endereco):
            problemas.append(
                "O endereco so aceita letras minusculas, numeros e hifen "
                "separando palavras: %s" % endereco)
        else:
            n = len(endereco.split("-"))
            if not (ENDERECO_MIN_PALAVRAS <= n <= ENDERECO_MAX_PALAVRAS):
                problemas.append(
                    "O endereco tem %d palavra(s); o aceito e de %d a %d: %s"
                    % (n, ENDERECO_MIN_PALAVRAS, ENDERECO_MAX_PALAVRAS, endereco))
        destino = os.path.join(pasta_artigos, endereco + ".html")
        if os.path.exists(destino):
            problemas.append(
                "Ja existe um artigo nesse endereco: artigos/%s.html" % endereco)

    # 3. titulo_aba e descricao
    titulo = cabecalho.get("titulo_aba", "")
    if titulo and len(titulo) > TITULO_MAX:
        problemas.append(
            "O titulo da aba tem %d caracteres; o maximo e %d."
            % (len(titulo), TITULO_MAX))
    descricao = cabecalho.get("descricao", "")
    if descricao and not (DESCRICAO_MIN <= len(descricao) <= DESCRICAO_MAX):
        problemas.append(
            "A descricao tem %d caracteres; o aceito e de %d a %d."
            % (len(descricao), DESCRICAO_MIN, DESCRICAO_MAX))

    # 4. datas
    for campo in ("data_publicacao", "data_atualizacao"):
        valor = cabecalho.get(campo, "")
        if valor and not _e_iso(valor):
            problemas.append(
                "O campo %s tem de ser uma data real em AAAA-MM-DD: %s"
                % (campo, valor))

    # 5. corpo
    if "—" in corpo or "–" in corpo:
        problemas.append(
            "O corpo tem travessao. O padrao do site nao usa travessao.")
    baixo = _sem_acento(corpo.lower())
    for sinal in SINAIS_DE_PERGUNTAS:
        if _sem_acento(sinal) in baixo:
            problemas.append(
                "O corpo parece ter bloco de perguntas e respostas (%r). "
                "Decisao de 16/11/2026: artigo nao tem esse bloco." % sinal)
            break
    n = _palavras_do_corpo(corpo)
    if not (CORPO_MIN_PALAVRAS <= n <= CORPO_MAX_PALAVRAS):
        problemas.append(
            "O corpo tem %d palavras; o aceito e de %d a %d."
            % (n, CORPO_MIN_PALAVRAS, CORPO_MAX_PALAVRAS))

    # 6. fecho
    fecho = cabecalho.get("fecho", "").strip()
    if fecho:
        miolo = fecho[:-1] if fecho[-1] in ".!?" else fecho
        if re.search(r"[.!?]\s+\S", miolo):
            problemas.append(
                "O fecho tem mais de uma frase. E uma frase so: %s" % fecho)
        if fecho[-1] not in ".!?":
            problemas.append("O fecho nao termina com ponto: %s" % fecho)
        primeira = _sem_acento(fecho.lower()).lstrip()
        for verbo in IMPERATIVOS:
            v = _sem_acento(verbo)
            if re.match(r"%s\b" % re.escape(v), primeira) or \
               re.search(r"[,;:]\s*%s\b" % re.escape(v), primeira):
                problemas.append(
                    "O fecho comeca por verbo no imperativo (%r), que e "
                    "convite a contratar. Vedado pelo Provimento 205/2021."
                    % verbo)
                break

    # 7. leia_tambem
    leia = cabecalho.get("leia_tambem", "").strip()
    if leia:
        for nome in [x.strip() for x in leia.split(",") if x.strip()]:
            if not os.path.exists(os.path.join(pasta_artigos, nome)):
                problemas.append(
                    "O leia_tambem aponta para um artigo que nao existe: %s"
                    % nome)
    return problemas


# --------------------------------------------------------------------------
# Montagem. Nenhuma destas funcoes escreve em disco.
# --------------------------------------------------------------------------

def data_por_extenso(iso):
    d = datetime.date.fromisoformat(iso)
    return "%d de %s de %d" % (d.day, MESES[d.month - 1], d.year)


def _itens_do_indice(html):
    """Os itens reais do indice. Os comentarios saem antes: o indice traz um
    exemplo de item comentado, que nao e item."""
    limpo = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    achados = re.findall(
        r'<li class="item-artigo">\s*'
        r'<h2><a href="(/artigos/[^"]+)">(.*?)</a></h2>\s*'
        r'<p>(.*?)</p>\s*'
        r'<p class="datas"><time datetime="([^"]+)">(.*?)</time></p>',
        limpo, re.S)
    return [{"href": a, "titulo": b, "resumo": c, "iso": d, "data": e}
            for a, b, c, d, e in achados]


def escolher_leia_tambem(cabecalho, indice=INDICE, pasta_artigos=PASTA_ARTIGOS):
    """Os artigos que entram no bloco 'Leia tambem'.

    Se o cabecalho trouxe leia_tambem, vale o que ele diz, na ordem dada.
    Se nao trouxe, o programa escolhe os dois mais recentes do indice,
    tirando o proprio artigo. REGRA ESCOLHIDA AQUI, a confirmar: o indice ja
    esta do mais recente para o mais antigo, entao sao os dois do topo.
    """
    with open(indice, encoding="utf-8") as f:
        itens = _itens_do_indice(f.read())
    proprio = "/artigos/%s.html" % cabecalho.get("endereco", "")
    itens = [i for i in itens if i["href"] != proprio]

    pedido = cabecalho.get("leia_tambem", "").strip()
    if pedido:
        nomes = [x.strip() for x in pedido.split(",") if x.strip()]
        por_href = {i["href"]: i for i in itens}
        return [por_href["/artigos/" + n] for n in nomes
                if "/artigos/" + n in por_href]
    return itens[:QUANTOS_LEIA_TAMBEM]


def montar_marcadores(cabecalho, corpo, indice=INDICE, pasta_artigos=PASTA_ARTIGOS):
    endereco = cabecalho["endereco"]
    canonico = PREFIXO + endereco + ".html"
    pub = cabecalho["data_publicacao"]
    atu = cabecalho["data_atualizacao"]
    escolhidos = escolher_leia_tambem(cabecalho, indice, pasta_artigos)
    return {
        "{{TITLE}}": cabecalho["titulo_aba"],
        "{{DESCRIPTION}}": cabecalho["descricao"],
        "{{CANONICAL}}": canonico,
        "{{H1}}": cabecalho["h1"],
        "{{DATA_PUBLICACAO}}": data_por_extenso(pub),
        "{{DATA_PUBLICACAO_ISO}}": pub,
        "{{DATA_ATUALIZACAO}}": data_por_extenso(atu),
        "{{DATA_ATUALIZACAO_ISO}}": atu,
        "{{CORPO}}": corpo_em_html(corpo),
        "{{FECHO}}": cabecalho["fecho"],
        "{{ITENS_LEIA_TAMBEM}}": itens_em_html(escolhidos),
    }, escolhidos


def corpo_em_html(corpo):
    """O corpo do .md em <h2> e <p>. Sem negrito e sem travessao, que e o
    padrao do site; o que nao for titulo vira paragrafo.

    O recuo e de SEIS espacos, o do miolo do <article class="folha"> no
    modelo, desde 21/11/2026. A primeira linha sai sem recuo nenhum: a
    substituicao do {{CORPO}} acontece no lugar do marcador, que ja esta
    recuado na sua linha, e repetir o recuo ali empurraria so o primeiro
    bloco para dentro."""
    partes = []
    for bloco in re.split(r"\n\s*\n", corpo.strip()):
        bloco = bloco.strip()
        if not bloco:
            continue
        if bloco.startswith("## "):
            partes.append("      <h2>%s</h2>" % bloco[3:].strip())
        else:
            partes.append("      <p>%s</p>" % " ".join(bloco.split()))
    return "\n\n".join(partes).lstrip()


def itens_em_html(itens):
    if not itens:
        return ""
    linhas = []
    for i in itens:
        linhas.append(
            '      <li class="item-artigo">\n'
            '        <h2><a href="%s">%s</a></h2>\n'
            '        <p>%s</p>\n'
            '        <p class="datas"><time datetime="%s">%s</time></p>\n'
            '      </li>' % (i["href"], i["titulo"], i["resumo"], i["iso"], i["data"]))
    return "\n".join(linhas)


def gerar_html(marcadores, modelo=MODELO):
    """O HTML do artigo. Tira do modelo o que e do modelo, poe os valores e
    confere que nao sobrou marcador."""
    with open(modelo, encoding="utf-8") as f:
        html = f.read()

    # fora o comentario de documentacao do topo
    i = html.index("<!--")
    j = html.index("-->", i) + 3
    html = html[:i] + html[j:]
    html = html.replace("<!doctype html>\n\n<html", "<!doctype html>\n<html")

    # fora a linha noindex e o comentario que a explica
    i = html.index("<!-- Esta linha")
    marca = '<meta name="robots" content="noindex, nofollow">\n'
    html = html[:i] + html[html.index(marca) + len(marca):]

    # fora os comentarios de instrucao que sao do modelo
    for inicio in ("<!-- Os DOIS blocos de dados estruturados",
                   "<!-- O FECHO."):
        i = html.index(inicio)
        html = html[:i] + html[html.index("-->", i) + 4:]

    # a secao Leia tambem: ou se preenche, ou se apaga inteira
    if not marcadores["{{ITENS_LEIA_TAMBEM}}"]:
        i = html.index(LIMITE_INICIO)
        j = html.index(LIMITE_FIM) + len(LIMITE_FIM) + 1
        html = html[:i] + html[j:]
    else:
        html = html.replace(LIMITE_INICIO + "\n", "").replace(
            "\n" + LIMITE_FIM, "")

    for marca, valor in marcadores.items():
        html = html.replace(marca, valor)

    sobrando = re.findall(r"\{\{[A-Za-z0-9_]+\}\}",
                          re.sub(r"<!--.*?-->", "", html, flags=re.S))
    if sobrando:
        raise ErroDeEntrada(
            "Sobrou marcador no HTML gerado: %s" % ", ".join(sorted(set(sobrando))))
    return html


def linha_do_indice(cabecalho):
    return (
        '      <li class="item-artigo">\n'
        '        <h2><a href="/artigos/%s.html">%s</a></h2>\n'
        '        <p>%s</p>\n'
        '        <p class="datas"><time datetime="%s">%s</time></p>\n'
        '      </li>' % (
            cabecalho["endereco"], cabecalho["h1"], cabecalho["resumo_indice"],
            cabecalho["data_publicacao"],
            data_por_extenso(cabecalho["data_publicacao"])))


def entrada_do_sitemap(cabecalho):
    return (
        '  <url>\n'
        '    <loc>%s%s.html</loc>\n'
        '    <lastmod>%s</lastmod>\n'
        '    <priority>0.8</priority>\n'
        '  </url>' % (PREFIXO, cabecalho["endereco"],
                      cabecalho["data_atualizacao"]))


# --------------------------------------------------------------------------
# As tres etapas
# --------------------------------------------------------------------------

def cmd_testar(args):
    cabecalho, corpo = ler_entrada(args.entrada)
    problemas = validar(cabecalho, corpo)
    if problemas:
        print("ENTRADA REPROVADA. %d problema(s), e nada foi escrito:\n"
              % len(problemas))
        for p in problemas:
            print("  - %s" % p)
        return 1

    marcadores, escolhidos = montar_marcadores(cabecalho, corpo)
    html = gerar_html(marcadores)

    print("ENTRADA APROVADA. Modo de teste: nada foi escrito em disco.\n")
    print("=" * 74)
    print("OS ONZE MARCADORES E O VALOR QUE CADA UM RECEBERIA")
    print("=" * 74)
    for marca in MARCADORES:
        valor = marcadores[marca]
        uma_linha = " ".join(valor.split())
        if len(uma_linha) > 86:
            uma_linha = uma_linha[:83] + "..."
        print("  %-26s %s" % (marca, uma_linha or "(vazio)"))

    print()
    print("=" * 74)
    print("DE ONDE SAIRIA O BLOCO \"LEIA TAMBEM\"")
    print("=" * 74)
    if cabecalho.get("leia_tambem", "").strip():
        print("  Do cabecalho, campo leia_tambem.")
    else:
        print("  O cabecalho nao trouxe leia_tambem. O programa escolheria os")
        print("  %d mais recentes do indice, fora o proprio artigo:" % QUANTOS_LEIA_TAMBEM)
    for i in escolhidos:
        print("    - %s  (%s)" % (i["href"], i["data"]))
    if not escolhidos:
        print("    - nenhum. A secao inteira sairia do HTML.")

    print()
    print("=" * 74)
    print("A LINHA QUE ENTRARIA EM artigos/index.html")
    print("=" * 74)
    print(linha_do_indice(cabecalho))

    print()
    print("=" * 74)
    print("A ENTRADA QUE ENTRARIA EM sitemap.xml")
    print("=" * 74)
    print(entrada_do_sitemap(cabecalho))

    print()
    print("=" * 74)
    print("O HTML QUE SERIA GERADO EM artigos/%s.html  (%d bytes)"
          % (cabecalho["endereco"], len(html.encode("utf-8"))))
    print("=" * 74)
    if args.html_inteiro:
        print(html)
    else:
        linhas = html.split("\n")
        for n, linha in enumerate(linhas[:40], 1):
            print("%4d | %s" % (n, linha))
        print("     | ... mais %d linhas. Use --html-inteiro para ver tudo."
              % (len(linhas) - 40))
    return 0


def cmd_preparar(args):
    print("A etapa 'preparar' ainda nao existe: e o passo 4.")
    print("Ela vai criar o ramo, escrever os tres arquivos e abrir o pull")
    print("request. Este programa nunca envia para a main.")
    return 2


def cmd_conferir(args):
    print("A etapa 'conferir' ainda nao existe: e o passo 5.")
    print("Ela roda depois do merge, confere o ar por endereco e, se algo")
    print("falhar, abre um pull request de reversao.")
    return 2


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="novo_artigo",
        description="Publica um artigo do site leeadv.com.br a partir de um .md.")
    sub = p.add_subparsers(dest="etapa")

    t = sub.add_parser("testar", help="le, valida e mostra. Nao escreve nada.")
    t.add_argument("entrada", help="caminho do .md, fora do repositorio")
    t.add_argument("--html-inteiro", action="store_true",
                   help="mostra o HTML inteiro, em vez das primeiras linhas")
    t.set_defaults(func=cmd_testar)

    pr = sub.add_parser("preparar", help="cria o ramo e abre o pull request (passo 4)")
    pr.add_argument("entrada")
    pr.set_defaults(func=cmd_preparar)

    cf = sub.add_parser("conferir", help="confere o ar depois do merge (passo 5)")
    cf.add_argument("entrada", nargs="?")
    cf.set_defaults(func=cmd_conferir)

    argv = list(sys.argv[1:] if argv is None else argv)
    # testar e o padrao: "novo_artigo.py algo.md" vale por "testar algo.md"
    if argv and argv[0] not in ("testar", "preparar", "conferir", "-h", "--help"):
        argv.insert(0, "testar")
    args = p.parse_args(argv)
    if not getattr(args, "func", None):
        p.print_help()
        return 2
    try:
        return args.func(args)
    except ErroDeEntrada as e:
        print("ERRO: %s" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
