# leeadv-site

Site institucional do escritório **Lee Advogado**, em
[leeadv.com.br](https://leeadv.com.br).

HTML estático, sem framework, sem construção e sem dependência. O que está no
repositório é exatamente o que é servido. Nenhum recurso de terceiro é buscado
em tempo de execução: fontes, logotipos e folha de estilo moram aqui, e a
procedência de cada arquivo que veio de fora está em
[PROCEDENCIA.md](PROCEDENCIA.md).

## Publicação

Publicado pelo **GitHub Pages**, com origem "GitHub Actions". O fluxo
[`.github/workflows/publicar.yml`](.github/workflows/publicar.yml) roda a cada
envio para `main` e empacota a raiz do repositório, sem etapa de construção.

O arquivo `CNAME` guarda o domínio personalizado. **Não apague**: sem ele, cada
publicação apaga o domínio configurado no painel do GitHub.

## Estrutura

```
index.html · aviso.html · privacidade.html   as três páginas
CNAME · robots.txt · sitemap.xml             publicação e indexação
estatico/                                    estilo, logotipos e fontes
```

## Antes de alterar o conteúdo

Este é um site de advogado, e o que se pode dizer nele é regulado. **Toda
alteração de texto passa pela conferência de publicidade (Provimento 205/2021
do CFOAB) antes de entrar no repositório**, e o resultado fica registrado com
data. Alteração de texto publicada sem essa conferência é alteração a desfazer.

Ao publicar artigo em veículo externo, a referência entra na seção Publicações
no mesmo dia. A política de privacidade é reescrita no dia em que entrar
formulário, cookie ou medição de acesso — não depois.

## O que nunca entra aqui

O repositório é público. Nenhum dado de cliente, nenhuma credencial e nenhum
caminho de pasta pessoal podem entrar, nem em comentário de código.
