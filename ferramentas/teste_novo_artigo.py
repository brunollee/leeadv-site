#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bateria do novo_artigo.py. Biblioteca padrao, sem dependencia externa.

Rodar da raiz do repositorio:

    python -m unittest discover -s ferramentas -p "teste_*.py" -v

Cada regra de validacao tem um caso que passa e um que reprova. O caso que
passa existe para a regra nao virar um "reprova sempre" silencioso.
"""

import os
import re
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import novo_artigo as na  # noqa: E402


CORPO_BOM = "\n\n".join(
    ["## Secao %d\n\npalavra " % i + "palavra " * 90 for i in range(1, 9)])

CABECALHO_BOM = {
    "endereco": "juros-no-atraso-de-pagamento",
    "titulo_aba": "Atraso de pagamento: quanto cobrar de juros e multa",
    "descricao": "x" * 155,
    "h1": "Quanto cobrar quando o cliente atrasa o pagamento",
    "resumo_indice": "Uma linha de resumo para o indice.",
    "data_publicacao": "2026-11-17",
    "data_atualizacao": "2026-11-17",
    "fecho": "Quanto cabe em cada contrato depende de ler o que foi assinado.",
    "leia_tambem": "",
}


def cab(**mudancas):
    c = dict(CABECALHO_BOM)
    c.update(mudancas)
    return c


class PastaVazia:
    """Uma pasta de artigos vazia, para o teste nao depender do repositorio."""
    def __enter__(self):
        self.tmp = tempfile.TemporaryDirectory()
        return self.tmp.name
    def __exit__(self, *a):
        self.tmp.cleanup()


def problemas(cabecalho=None, corpo=None, pasta=None):
    if pasta is None:
        with PastaVazia() as p:
            return na.validar(cabecalho or cab(), CORPO_BOM if corpo is None else corpo, p)
    return na.validar(cabecalho or cab(), CORPO_BOM if corpo is None else corpo, pasta)


def tem(lista, trecho):
    return any(trecho.lower() in p.lower() for p in lista)


# --------------------------------------------------------------------------

class TesteCasoValido(unittest.TestCase):
    def test_o_caso_bom_passa_limpo(self):
        self.assertEqual(problemas(), [])

    def test_o_corpo_de_referencia_tem_tamanho_aceito(self):
        n = na._palavras_do_corpo(CORPO_BOM)
        self.assertTrue(na.CORPO_MIN_PALAVRAS <= n <= na.CORPO_MAX_PALAVRAS, n)


class TesteCamposObrigatorios(unittest.TestCase):
    def test_campo_ausente_reprova(self):
        for campo in na.CAMPOS_OBRIGATORIOS:
            c = cab()
            del c[campo]
            self.assertTrue(tem(problemas(c), "ausente no cabecalho: %s" % campo),
                            "nao reprovou a ausencia de %s" % campo)

    def test_campo_vazio_reprova(self):
        self.assertTrue(tem(problemas(cab(h1="   ")), "vazio no cabecalho: h1"))

    def test_campo_opcional_pode_faltar(self):
        c = cab()
        del c["leia_tambem"]
        self.assertEqual(problemas(c), [])

    def test_campo_desconhecido_reprova(self):
        self.assertTrue(tem(problemas(cab(autor="alguem")), "nao conhece"))


class TesteEndereco(unittest.TestCase):
    def test_tres_a_seis_palavras_passam(self):
        for e in ("um-dois-tres", "um-dois-tres-quatro-cinco-seis"):
            self.assertEqual(problemas(cab(endereco=e)), [], e)

    def test_poucas_ou_muitas_palavras_reprovam(self):
        for e in ("um-dois", "um-dois-tres-quatro-cinco-seis-sete"):
            self.assertTrue(tem(problemas(cab(endereco=e)), "palavra"), e)

    def test_maiuscula_reprova(self):
        self.assertTrue(tem(problemas(cab(endereco="Juros-No-Atraso")), "maiuscula"))

    def test_acento_reprova(self):
        self.assertTrue(tem(problemas(cab(endereco="juros-no-atrás-o")), "acento"))

    def test_espaco_reprova(self):
        self.assertTrue(tem(problemas(cab(endereco="juros no atraso")), "espaco"))

    def test_sublinhado_reprova(self):
        self.assertTrue(tem(problemas(cab(endereco="juros_no_atraso")), "hifen"))

    def test_endereco_ja_existente_reprova(self):
        with PastaVazia() as p:
            alvo = os.path.join(p, CABECALHO_BOM["endereco"] + ".html")
            with open(alvo, "w", encoding="utf-8") as f:
                f.write("ja existe")
            self.assertTrue(tem(problemas(pasta=p), "Ja existe um artigo"))

    def test_endereco_livre_passa(self):
        self.assertEqual(problemas(), [])


class TesteTituloEDescricao(unittest.TestCase):
    def test_titulo_no_limite_passa(self):
        self.assertEqual(problemas(cab(titulo_aba="t" * na.TITULO_MAX)), [])

    def test_titulo_longo_reprova(self):
        p = problemas(cab(titulo_aba="t" * (na.TITULO_MAX + 1)))
        self.assertTrue(tem(p, "titulo da aba tem 61"))

    def test_descricao_nos_dois_limites_passa(self):
        for n in (na.DESCRICAO_MIN, na.DESCRICAO_MAX):
            self.assertEqual(problemas(cab(descricao="d" * n)), [], n)

    def test_descricao_curta_ou_longa_reprova(self):
        for n in (na.DESCRICAO_MIN - 1, na.DESCRICAO_MAX + 1):
            self.assertTrue(tem(problemas(cab(descricao="d" * n)), "descricao tem"), n)


class TesteDatas(unittest.TestCase):
    def test_iso_passa(self):
        self.assertEqual(problemas(cab(data_publicacao="2026-01-01")), [])

    def test_formato_errado_reprova(self):
        for v in ("17/11/2026", "2026-11", "17 de novembro de 2026", "2026-1-1"):
            self.assertTrue(tem(problemas(cab(data_publicacao=v)), "AAAA-MM-DD"), v)

    def test_data_inexistente_reprova(self):
        self.assertTrue(tem(problemas(cab(data_atualizacao="2026-02-31")), "AAAA-MM-DD"))


class TesteCorpo(unittest.TestCase):
    def test_travessao_reprova(self):
        self.assertTrue(tem(problemas(corpo=CORPO_BOM + "\n\nfrase — outra"),
                            "travessao"))
        self.assertTrue(tem(problemas(corpo=CORPO_BOM + "\n\nfrase – outra"),
                            "travessao"))

    def test_hifen_comum_nao_reprova(self):
        self.assertEqual(problemas(corpo=CORPO_BOM + "\n\npre-pago e pos-pago"), [])

    def test_bloco_de_perguntas_reprova(self):
        for sinal in ("## Perguntas frequentes", "## Perguntas e respostas",
                      "FAQPage", "acceptedAnswer"):
            p = problemas(corpo=CORPO_BOM + "\n\n" + sinal)
            self.assertTrue(tem(p, "perguntas e respostas"), sinal)

    def test_a_palavra_pergunta_sozinha_nao_reprova(self):
        p = problemas(corpo=CORPO_BOM + "\n\nA pergunta do cliente foi outra.")
        self.assertEqual(p, [])

    def test_corpo_curto_reprova(self):
        self.assertTrue(tem(problemas(corpo="palavra " * 50), "corpo tem 50 palavras"))

    def test_corpo_longo_reprova(self):
        p = problemas(corpo="palavra " * (na.CORPO_MAX_PALAVRAS + 1))
        self.assertTrue(tem(p, "1201 palavras"))

    def test_titulo_nao_conta_como_palavra_do_corpo(self):
        so_titulos = "\n\n".join("## Titulo %d" % i for i in range(50))
        self.assertEqual(na._palavras_do_corpo(so_titulos), 0)


class TesteFecho(unittest.TestCase):
    def test_uma_frase_passa(self):
        self.assertEqual(problemas(cab(fecho="Isso depende do contrato.")), [])

    def test_duas_frases_reprovam(self):
        p = problemas(cab(fecho="Isso depende. O contrato manda."))
        self.assertTrue(tem(p, "mais de uma frase"))

    def test_sem_ponto_final_reprova(self):
        self.assertTrue(tem(problemas(cab(fecho="Isso depende do contrato")),
                            "nao termina com ponto"))

    def test_imperativo_no_comeco_reprova(self):
        for f in ("Fale comigo sobre o seu contrato.",
                  "Agende uma conversa sobre o contrato.",
                  "Peça a revisao do seu contrato.",
                  "Nao perca o prazo do seu contrato."):
            self.assertTrue(tem(problemas(cab(fecho=f)), "imperativo"), f)

    def test_imperativo_depois_de_virgula_reprova(self):
        p = problemas(cab(fecho="Se o contrato calou, consulte o que foi assinado."))
        self.assertTrue(tem(p, "imperativo"))

    def test_verbo_parecido_no_meio_nao_reprova(self):
        self.assertEqual(
            problemas(cab(fecho="O credor que consulta o contrato cobra melhor.")), [])


class TesteLeiaTambem(unittest.TestCase):
    def test_vazio_passa(self):
        self.assertEqual(problemas(cab(leia_tambem="")), [])

    def test_artigo_inexistente_reprova(self):
        p = problemas(cab(leia_tambem="nao-existe.html"))
        self.assertTrue(tem(p, "nao existe"))

    def test_artigo_existente_passa(self):
        with PastaVazia() as pasta:
            with open(os.path.join(pasta, "outro.html"), "w", encoding="utf-8") as f:
                f.write("x")
            self.assertEqual(problemas(cab(leia_tambem="outro.html"), pasta=pasta), [])


class TesteLeitura(unittest.TestCase):
    def escrever(self, texto):
        f = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                        encoding="utf-8")
        f.write(texto)
        f.close()
        self.addCleanup(os.unlink, f.name)
        return f.name

    def test_le_cabecalho_e_corpo(self):
        c, corpo = na.ler_entrada(self.escrever(
            "---\nendereco: um-dois-tres\nh1: Titulo\n---\n\nO corpo.\n"))
        self.assertEqual(c["endereco"], "um-dois-tres")
        self.assertEqual(c["h1"], "Titulo")
        self.assertEqual(corpo, "O corpo.")

    def test_valor_com_dois_pontos_nao_quebra(self):
        c, _ = na.ler_entrada(self.escrever(
            "---\ntitulo_aba: Atraso: quanto cobrar\n---\ncorpo\n"))
        self.assertEqual(c["titulo_aba"], "Atraso: quanto cobrar")

    def test_arquivo_inexistente(self):
        with self.assertRaises(na.ErroDeEntrada):
            na.ler_entrada("nao-existe-mesmo.md")

    def test_sem_cabecalho(self):
        with self.assertRaises(na.ErroDeEntrada):
            na.ler_entrada(self.escrever("corpo sem cabecalho\n"))

    def test_cabecalho_sem_fechar(self):
        with self.assertRaises(na.ErroDeEntrada):
            na.ler_entrada(self.escrever("---\nendereco: x\ncorpo\n"))

    def test_linha_sem_dois_pontos(self):
        with self.assertRaises(na.ErroDeEntrada):
            na.ler_entrada(self.escrever("---\nendereco\n---\ncorpo\n"))

    def test_campo_repetido(self):
        with self.assertRaises(na.ErroDeEntrada):
            na.ler_entrada(self.escrever("---\nh1: a\nh1: b\n---\ncorpo\n"))


class TesteMontagem(unittest.TestCase):
    def test_data_por_extenso(self):
        self.assertEqual(na.data_por_extenso("2026-11-17"), "17 de novembro de 2026")
        self.assertEqual(na.data_por_extenso("2027-01-01"), "1 de janeiro de 2027")

    def test_corpo_em_html(self):
        h = na.corpo_em_html("## Um titulo\n\nUm paragrafo.\n\nOutro.")
        self.assertIn("<h2>Um titulo</h2>", h)
        self.assertEqual(h.count("<p>"), 2)

    def test_linha_do_indice_tem_a_forma_do_indice(self):
        linha = na.linha_do_indice(cab())
        self.assertIn('<li class="item-artigo">', linha)
        self.assertIn('href="/artigos/juros-no-atraso-de-pagamento.html"', linha)
        self.assertIn('<time datetime="2026-11-17">17 de novembro de 2026</time>', linha)

    def test_entrada_do_sitemap_tem_os_tres_campos(self):
        e = na.entrada_do_sitemap(cab())
        for t in ("<loc>", "<lastmod>", "<priority>"):
            self.assertIn(t, e)
        self.assertIn("https://leeadv.com.br/artigos/juros-no-atraso-de-pagamento.html", e)


class TesteGeracao(unittest.TestCase):
    """Usa o modelo de verdade do repositorio, sem escrever nada nele."""

    def montar(self, **mudancas):
        return na.montar_marcadores(cab(**mudancas), CORPO_BOM)

    def test_onze_marcadores(self):
        marcadores, _ = self.montar()
        self.assertEqual(sorted(marcadores), sorted(na.MARCADORES))

    def test_o_modelo_tem_os_onze_e_so_eles(self):
        with open(na.MODELO, encoding="utf-8") as f:
            texto = f.read()
        sem_comentario = re.sub(r"<!--.*?-->", "", texto, flags=re.S)
        achados = set(re.findall(r"\{\{[A-Za-z0-9_]+\}\}", sem_comentario))
        self.assertEqual(achados, set(na.MARCADORES))

    def test_html_gerado_nao_tem_marcador_sobrando(self):
        marcadores, _ = self.montar()
        html = na.gerar_html(marcadores)
        self.assertEqual(re.findall(r"\{\{[A-Za-z0-9_]+\}\}", html), [])

    def test_html_gerado_nao_tem_noindex_nem_os_comentarios_do_modelo(self):
        marcadores, _ = self.montar()
        html = na.gerar_html(marcadores)
        self.assertNotIn("noindex", html)
        self.assertNotIn("MODELO DE P", html)
        self.assertNotIn("#LEIA-TAMBEM", html)

    def test_sem_leia_tambem_a_secao_inteira_sai(self):
        marcadores, _ = self.montar()
        marcadores["{{ITENS_LEIA_TAMBEM}}"] = ""
        html = na.gerar_html(marcadores)
        self.assertNotIn("leia-tambem", html)
        self.assertNotIn("Outros artigos", html)

    def test_com_leia_tambem_a_secao_fica_e_a_lista_nao_fica_vazia(self):
        marcadores, escolhidos = self.montar()
        if not escolhidos:
            self.skipTest("o indice do repositorio nao tem outro artigo")
        html = na.gerar_html(marcadores)
        self.assertIn("leia-tambem", html)
        self.assertIn('<li class="item-artigo">', html)

    def test_escolhe_dois_e_nunca_o_proprio(self):
        _, escolhidos = self.montar()
        self.assertLessEqual(len(escolhidos), na.QUANTOS_LEIA_TAMBEM)
        for i in escolhidos:
            self.assertNotIn("juros-no-atraso-de-pagamento", i["href"])

    def test_o_exemplo_comentado_do_indice_nao_vira_item(self):
        with open(na.INDICE, encoding="utf-8") as f:
            itens = na._itens_do_indice(f.read())
        for i in itens:
            self.assertNotIn("nome-do-artigo", i["href"])


HOME_FALSA = """<section>
    <!-- #CARTOES-HOME:INICIO -->
    <ul class="grade-artigos">
      <li class="cartao-artigo">
        <p class="cartao-artigo-data"><time datetime="2026-11-20">20 de novembro de 2026</time></p>
        <h3 id="destaque-apelido">Titulo velho</h3>
        <p>Frase escrita a mao para este cartao.</p>
        <a href="/artigos/artigo-velho.html" class="voltar" aria-describedby="destaque-apelido">Ler o artigo</a>
      </li>
    </ul>
    <!-- #CARTOES-HOME:FIM -->
</section>"""


def item(endereco, iso, titulo="Titulo", resumo="Primeira frase. Segunda frase."):
    return {"href": "/artigos/%s.html" % endereco, "titulo": titulo,
            "resumo": resumo, "iso": iso,
            "data": na.data_por_extenso(iso)}


class TesteCartoesDaHome(unittest.TestCase):
    def test_mostra_so_os_tres_mais_recentes_na_ordem_do_indice(self):
        itens = [item("a", "2026-11-22"), item("b", "2026-11-21"),
                 item("c", "2026-11-20"), item("d", "2026-11-19")]
        saida = na.atualizar_home(HOME_FALSA, itens)
        achados = re.findall(r'href="(/artigos/[^"]+)"', saida)
        self.assertEqual(achados, ["/artigos/a.html", "/artigos/b.html",
                                   "/artigos/c.html"])

    def test_cartao_que_ja_existe_conserva_ancora_e_frase(self):
        itens = [item("novo", "2026-11-22"), item("artigo-velho", "2026-11-20")]
        saida = na.atualizar_home(HOME_FALSA, itens)
        self.assertIn('id="destaque-apelido"', saida)
        self.assertIn("Frase escrita a mao para este cartao.", saida)

    def test_cartao_novo_sem_cabecalho_usa_a_primeira_frase_do_resumo(self):
        itens = [item("novo-artigo", "2026-11-22")]
        saida = na.atualizar_home(HOME_FALSA, itens)
        self.assertIn("<p>Primeira frase.</p>", saida)
        self.assertNotIn("Segunda frase.", saida)

    def test_cabecalho_manda_na_ancora_e_na_frase_do_cartao_novo(self):
        itens = [item("novo-artigo", "2026-11-22")]
        saida = na.atualizar_home(
            HOME_FALSA, itens,
            {"ancora_cartao": "destaque-escolhido", "resumo_cartao": "Frase do cabecalho."})
        self.assertIn('id="destaque-escolhido"', saida)
        self.assertIn("<p>Frase do cabecalho.</p>", saida)

    def test_ancora_padrao_junta_dois_pedacos_quando_o_primeiro_e_curto(self):
        self.assertEqual(na.ancora_padrao("fisco-pode-fechar"), "destaque-fisco")
        self.assertEqual(na.ancora_padrao("nota-fiscal-nao-e-titulo"),
                         "destaque-nota-fiscal")

    def test_aplicar_duas_vezes_nao_muda_nada_na_segunda(self):
        itens = [item("a", "2026-11-22"), item("artigo-velho", "2026-11-20")]
        uma = na.atualizar_home(HOME_FALSA, itens)
        duas = na.atualizar_home(uma, itens)
        self.assertEqual(uma, duas)

    def test_home_sem_marcador_reprova_em_vez_de_adivinhar(self):
        with self.assertRaises(na.ErroDeEntrada):
            na.atualizar_home("<section><ul></ul></section>", [item("a", "2026-11-22")])


class TesteLeiaTambemDeTodos(unittest.TestCase):
    def test_cada_artigo_recebe_os_dois_mais_recentes_fora_ele_proprio(self):
        itens = [item("a", "2026-11-22"), item("b", "2026-11-21"),
                 item("c", "2026-11-20")]
        mapa = na.leia_tambem_de_cada_artigo(itens)
        self.assertEqual([i["href"] for i in mapa["/artigos/a.html"]],
                         ["/artigos/b.html", "/artigos/c.html"])
        self.assertEqual([i["href"] for i in mapa["/artigos/b.html"]],
                         ["/artigos/a.html", "/artigos/c.html"])
        self.assertEqual([i["href"] for i in mapa["/artigos/c.html"]],
                         ["/artigos/a.html", "/artigos/b.html"])

    def test_nenhum_artigo_aponta_para_si_mesmo(self):
        itens = [item(x, "2026-11-2%d" % i) for i, x in enumerate("abcd", 1)]
        for href, escolhidos in na.leia_tambem_de_cada_artigo(itens).items():
            self.assertNotIn(href, [e["href"] for e in escolhidos])

class TesteEtapas(unittest.TestCase):
    def test_preparar_e_conferir_ainda_nao_fazem_nada(self):
        for etapa in ("preparar", "conferir"):
            self.assertEqual(na.main([etapa, "qualquer.md"]), 2)

    def test_testar_e_o_padrao(self):
        self.assertEqual(na.main(["nao-existe-mesmo.md"]), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
