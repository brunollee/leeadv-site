# De onde veio cada arquivo guardado aqui

O que entra neste repositório vindo de fora tem **procedência registrada**,
com origem, data e resumo SHA-256. Sem isso, daqui a dois anos ninguém sabe
se o arquivo é o mesmo que foi conferido um dia ou um que alguém colou de um
fórum.

Nada aqui é buscado em tempo de execução. Nem fonte, nem folha de estilo, nem
script. Uma página que busca fonte fora conta a esse terceiro cada vez que
alguém a abre, e deixa de desenhar no dia em que o terceiro é o problema.

## As fontes em uso: Caladea e Carlito

Instaladas em **15/11/2026**, no lugar da Archivo e da Montserrat.

**Por que estas duas.** A Caladea é metricamente compatível com a Cambria, e
a Carlito é metricamente compatível com a Calibri. Os documentos do escritório
já são escritos em Cambria e Calibri, que são proprietárias da Microsoft e não
podem ser hospedadas num site público. Estas duas ocupam as mesmas medidas sem
esse impedimento. O desenho não é idêntico ao da Microsoft; as métricas são.

### Origem

| Família | Repositório de origem | Arquivos baixados |
|---|---|---|
| Caladea | `github.com/huertatipografica/Caladea`, `fonts/ttf/` | `Caladea-Regular.ttf`, `Caladea-Bold.ttf`, `OFL.txt` |
| Carlito | `github.com/googlefonts/carlito` (licença) e `github.com/google/fonts`, `ofl/carlito/` (binários) | `Carlito-Regular.ttf`, `Carlito-Bold.ttf`, `OFL.txt` |

O repositório da Carlito versiona apenas as fontes em formato `.glyphs` e não
publica binário nem lançamento; os `.ttf` vieram do `google/fonts`, o mesmo
repositório canônico já usado antes neste arquivo.

A Caladea foi baixada da Huerta Tipográfica e **conferida contra a cópia do
`google/fonts`**: os dois `.ttf` são byte a byte idênticos, nos dois estilos.

| Arquivo de origem | SHA-256 do que foi baixado |
|---|---|
| `Caladea-Regular.ttf` (81.600 B, versão 1.001) | `f1e899278b7b4491aba5b6a8253c4b04c050cc59b21865be5c37559a775153cd` |
| `Caladea-Bold.ttf` (84.492 B, versão 1.001) | `ae3cb2dcbc925809dd29d2a44e9802211cab66be541bacbfc9c08c74b27c3742` |
| `Carlito-Regular.ttf` (628.032 B, versão 1.104) | `f6418f708baede9789daef5d458c0f53d2a888af9820e8062934e504fedc6595` |
| `Carlito-Bold.ttf` (682.468 B, versão 1.104) | `bb5d20f79b82599ec72983597437373a80f2d2085fa91fc144fd74e876a594db` |

### A licença das duas é a SIL OFL 1.1

Vale registrar, porque contraria o que se lê por aí: **as duas famílias estão
sob a SIL Open Font License 1.1**, e não a Caladea sob Apache 2.0, como consta
de material mais antigo.

A Caladea de fato saiu sob Apache 2.0 na primeira distribuição, de 2013, no
pacote `crosextrafonts`. A versão 1.001, que é a que está aqui, é OFL. Três
conferências independentes, todas feitas em 15/11/2026:

1. O `OFL.txt` do repositório da Huerta Tipográfica diz, na primeira linha:
   "Copyright 2012 The Caladea Project Authors", e em seguida "This Font
   Software is licensed under the SIL Open Font License, Version 1.1".
2. No `google/fonts`, a Caladea mora em `ofl/caladea/`, e não em `apache/`.
3. O próprio binário declara a licença no registro 13 da tabela `name`:
   "This Font Software is licensed under the SIL Open Font License,
   Version 1.1", com o registro 14 apontando para `scripts.sil.org/OFL`.

A OFL permite usar, embutir, modificar e redistribuir, inclusive o arquivo
recortado que está aqui, desde que a licença acompanhe. Ela acompanha, em
`fontes/caladea-LICENCA.txt` e `fontes/carlito-LICENCA.txt`.

### O recorte e a conversão

Cada `.ttf` foi recortado para os caracteres do português e convertido para
`woff2` com o `fontTools`, num ambiente descartável **fora** do repositório.
Ele não é dependência do site, que não tem dependência nenhuma. Mesmo comando
usado nas fontes anteriores:

```
python -m fontTools.subset <origem>.ttf \
    --unicodes=U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0300-0304,U+0308,U+0329,U+2000-206F,U+2074,U+20AC,U+2122,U+2212,U+2215,U+FEFF,U+FFFD \
    --layout-features='*' --flavor=woff2 --output-file=<destino>.woff2
```

| Arquivo guardado | Tamanho | SHA-256 |
|---|---|---|
| `estatico/fontes/caladea-regular.woff2` | 21.160 B | `e0435f85e40438319b4e480a57a68b0c01e0278f2c567b4ae6b65dbc4605f7dc` |
| `estatico/fontes/caladea-bold.woff2` | 21.168 B | `504d934b406affbb05be8ecbd56764b190087122003cd45122d984336746fbb2` |
| `estatico/fontes/caladea-LICENCA.txt` | 4.393 B | `ccdab61d371d8c8683a128a92cd7d498dbdb1d37689f7cb21f1bf6b16658d213` |
| `estatico/fontes/carlito-regular.woff2` | 40.372 B | `b53c5732be6e529727a16436bf3b3fe8a7c4c70dbb8cd2fd25113c5761fad9d6` |
| `estatico/fontes/carlito-bold.woff2` | 42.756 B | `e0e7ec8efab22c1af00105bd3304f0458b58e5f78a46c13d9580eb7db6a5c66e` |
| `estatico/fontes/carlito-LICENCA.txt` | 4.424 B | `58402f82a7c332a700294988fe7554fbb0a63a8d27ccc1ee3bbc640311990a00` |

Os dois arquivos de licença são cópia exata do `OFL.txt` de cada repositório
de origem, só renomeados.

Depois do recorte, a cobertura foi conferida caractere a caractere contra uma
amostra do português, com acentuação, cedilha, aspas tipográficas, travessão,
ordinais e símbolos de moeda: nada faltando. A Caladea ficou com 232 glifos
por estilo e a Carlito com 253.

**São arquivos estáticos, e não variáveis.** São quatro arquivos porque são
dois pesos de cada família, declarados separadamente no `@font-face` com
`font-weight: 400` e `font-weight: 700`. É diferente do que havia antes aqui,
e a diferença importa: não há eixo de largura para pedir, e nenhum
`font-stretch` deve ser aplicado a elas.

## As fontes retiradas: Archivo e Montserrat

**Retiradas em 15/11/2026.** Esta seção fica para registro: os arquivos abaixo
estiveram no repositório entre 15/11/2026 e 15/11/2026, nos dois primeiros
commits do site, e foram apagados no terceiro.

**Motivo da retirada.** A identidade do site passou a seguir a dos documentos
do escritório, escritos em Cambria e Calibri. A Archivo e a Montserrat não têm
relação métrica com elas, e manter as quatro famílias significaria o site
falando uma língua tipográfica e as peças do escritório, outra.

Origem: `github.com/google/fonts`, por
`raw.githubusercontent.com/google/fonts/main/ofl/...`, baixadas em 06/11/2026.

| Arquivo de origem | SHA-256 do que foi baixado |
|---|---|
| `ofl/archivo/Archivo[wdth,wght].ttf` (643 KB) | `0e094a7d3c7c4c25cf1310c4b30014f1dae9332220b1c2c88f4fa996f0b05053` |
| `ofl/archivo/OFL.txt` | `108b4e57c9c796d3d38d0428ca7ee39de47ad93187302718d9b2d8864b9b716b` |
| `ofl/montserrat/Montserrat[wght].ttf` (727 KB) | `0f7b311b2f3279e4eef9b2f968bcdbab6e28f4daeb1f049f4f278a902bcd82f7` |
| `ofl/montserrat/OFL.txt` | `8b7141c03fa4f8d44e6345d5d4931709290f0f67875e452e95ac1fd3a027802e` |

| Arquivo que esteve guardado | Tamanho | SHA-256 |
|---|---|---|
| `estatico/fontes/archivo-variavel.woff2` | 97.092 B | `cf2ebd5271ad07ad5ccbdceb54b664736e2cee3aad0e8ec0b94f66b4d8da927d` |
| `estatico/fontes/archivo-OFL.txt` | 4.388 B | `108b4e57c9c796d3d38d0428ca7ee39de47ad93187302718d9b2d8864b9b716b` |
| `estatico/fontes/montserrat-variavel.woff2` | 59.268 B | `cc913bdc76106cbd68d66e8e38924fd6fba42dc8ef9430cbfbe25d0e4be6cfa7` |
| `estatico/fontes/montserrat-OFL.txt` | 4.400 B | `8b7141c03fa4f8d44e6345d5d4931709290f0f67875e452e95ac1fd3a027802e` |

Eram arquivos **variáveis**, convertidos pelo mesmo comando de recorte, e
mantinham os eixos `wght 100..900` nas duas e `wdth 62..125` na Archivo. Quem
precisar delas de volta tem acima tudo o que é preciso para refazê-las iguais.

Licença: SIL Open Font License 1.1, nos dois casos.

## O retrato

Foto do titular, tratada **fora do repositório** e trazida pronta em
15/11/2026. Nada aqui foi gerado, convertido ou alterado por quem escreveu
estas linhas: os quatro arquivos foram conferidos, medidos e registrados como
chegaram.

A foto original, o script de tratamento e os arquivos em tamanho cheio ficam
na pasta de trabalho do titular, fora deste repositório. O que entra aqui são
só os quatro derivados de 600x600 que a página usa.

O recorte separou fundo e pele pela diferença entre o vermelho e o verde, e o
fundo foi substituído: `--bd2` #ececea na versão clara e #1f1f1f na escura. É
por isso que são quatro arquivos e não dois, e é por isso que o CSS não
desenha fundo nem borda atrás do círculo: o fundo já está dentro da imagem.

| Arquivo guardado | Formato | Dimensões | Tamanho | SHA-256 |
|---|---|---|---|---|
| `estatico/retrato/retrato-claro.avif` | AVIF | 600x600 | 29.393 B | `545887fffb56ad75c16afad9f9b5ba5455b737d6d8cd6998156611160cef2d18` |
| `estatico/retrato/retrato-claro.webp` | WebP | 600x600 | 28.986 B | `95e5a7888b25a6577a5b7b43f1508965c0d21bf308cd4c20a4e8d58fca3ac4a8` |
| `estatico/retrato/retrato-escuro.avif` | AVIF | 600x600 | 29.374 B | `ba467c1034f1eddcab7597fc949c2bcb319b761c896eec70c70ee15d3e2b1848` |
| `estatico/retrato/retrato-escuro.webp` | WebP | 600x600 | 28.536 B | `40ddb9a5d7c14e6bccf57e61fd5d6d86374cb4f3503879f97098e3f4e85f2091` |

Os formatos e as dimensões foram lidos dos próprios bytes, e não do nome do
arquivo: as caixas `ftypavif` e `ispe` nos AVIF, o cabeçalho `RIFF`/`WEBP` nos
WebP. Nenhum PNG e nenhum JPEG entram no site.

O navegador baixa **um** desses quatro, não os quatro: o `<picture>` escolhe
pelo modo de cor e pelo formato que o navegador aceita.

**Publicar a foto é permitido.** O art. 5º, § 2º, do Provimento 205/2021 do
CFOAB admite imagens, inclusive fotografias dos advogados. O que o art. 6º
veda é o cenário: escritório, fachada, prateleira de livros ou qualquer
elemento que sugira estrutura física. Por isso o fundo foi removido, e não
apenas desfocado.

## Os logotipos

`logo-lee-preto.svg` e `logo-lee-advogado-branco.svg` são do titular. São
**caminhos, não texto**: não dependem de fonte instalada e não desandam
enquanto a fonte do título carrega. Carregam o metadado C2PA de proveniência
do arquivo original, que foi preservado — não cabe a quem publica apagar a
proveniência de uma peça de arte.

O arquivo de origem não registrava resumo para os dois. Os valores abaixo
foram calculados em 15/11/2026 e são a referência deste repositório.

| Arquivo guardado | Tamanho | SHA-256 |
|---|---|---|
| `estatico/logo-lee-preto.svg` | 11.134 B | `3fd42a96db0c8715828c3b66b0c10bc132974b4efbfbc116234484a18f093269` |
| `estatico/logo-lee-advogado-branco.svg` | 15.429 B | `1d3cdc7e193b4e9d25575ed4a79e05a9d7a9cf66ef74f5a08a5aefd3f02dfc52` |

No modo escuro, o site não troca de arquivo: inverte o preto por CSS. Os dois
logotipos são composições diferentes, com proporções diferentes, e trocar um
pelo outro faria a marca mudar de forma conforme o modo do sistema
operacional de quem abre a página.

## Como conferir

Na raiz do repositório:

```
sha256sum estatico/fontes/* estatico/*.svg
```

Qualquer divergência significa que o arquivo foi mexido. Nesse caso, não
corrija o resumo: descubra o que mexeu nele.

O `.gitattributes` com `* -text` existe por causa desta conferência. Sem ele,
um clone no Windows trocaria LF por CRLF e mudaria o resumo dos SVGs e dos
arquivos de licença.
