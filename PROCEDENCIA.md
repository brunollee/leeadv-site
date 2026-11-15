# De onde veio cada arquivo guardado aqui

O que entra neste repositório vindo de fora tem **procedência registrada**,
com origem, data e resumo SHA-256. Sem isso, daqui a dois anos ninguém sabe
se o arquivo é o mesmo que o sistema usa ou um que alguém colou de um fórum.

Nada aqui é buscado em tempo de execução. Nem fonte, nem folha de estilo, nem
script. Uma página que busca fonte fora conta a esse terceiro cada vez que
alguém abre o site, e deixa de desenhar no dia em que o terceiro é o problema.

## Esta cópia

Copiados em **15/11/2026** da pasta de estáticos do Sistema Lee Advogado,
**sem reconversão, sem recorte e sem otimização**. Reconverter produziria
arquivo diferente do que o sistema usa, e a conferência de procedência
deixaria de fechar.

As linhas das fontes abaixo são as mesmas do `PROCEDENCIA.md` daquela pasta,
e os resumos foram conferidos arquivo a arquivo depois da cópia.

## As fontes

Origem primária: **`github.com/google/fonts`**, o repositório canônico do
Google Fonts, pelos endereços `raw.githubusercontent.com/google/fonts/main/ofl/...`,
baixados em 06/11/2026.

| Arquivo de origem | SHA-256 do que foi baixado |
|---|---|
| `ofl/archivo/Archivo[wdth,wght].ttf` (643 KB) | `0e094a7d3c7c4c25cf1310c4b30014f1dae9332220b1c2c88f4fa996f0b05053` |
| `ofl/archivo/OFL.txt` | `108b4e57c9c796d3d38d0428ca7ee39de47ad93187302718d9b2d8864b9b716b` |
| `ofl/montserrat/Montserrat[wght].ttf` (727 KB) | `0f7b311b2f3279e4eef9b2f968bcdbab6e28f4daeb1f049f4f278a902bcd82f7` |
| `ofl/montserrat/OFL.txt` | `8b7141c03fa4f8d44e6345d5d4931709290f0f67875e452e95ac1fd3a027802e` |

Os dois `.ttf` são **variáveis**, e não estáticos. Isso não é preferência: a
Archivo dos títulos é esticada (`font-stretch: 125%`) e o eixo de largura mora
dentro do arquivo variável. Com estática, o `font-stretch` não tem onde agir
e os títulos sairiam em largura normal.

Cada `.ttf` foi recortado para os caracteres do português e convertido para
`woff2` com o `fontTools`, num ambiente descartável fora do repositório:

```
python -m fontTools.subset <origem>.ttf \
    --unicodes=U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0300-0304,U+0308,U+0329,U+2000-206F,U+2074,U+20AC,U+2122,U+2212,U+2215,U+FEFF,U+FFFD \
    --layout-features='*' --flavor=woff2 --output-file=<destino>.woff2
```

| Arquivo guardado | Tamanho | SHA-256 |
|---|---|---|
| `estatico/fontes/archivo-variavel.woff2` | 95 KB | `cf2ebd5271ad07ad5ccbdceb54b664736e2cee3aad0e8ec0b94f66b4d8da927d` |
| `estatico/fontes/archivo-OFL.txt` | 4,3 KB | `108b4e57c9c796d3d38d0428ca7ee39de47ad93187302718d9b2d8864b9b716b` |
| `estatico/fontes/montserrat-variavel.woff2` | 58 KB | `cc913bdc76106cbd68d66e8e38924fd6fba42dc8ef9430cbfbe25d0e4be6cfa7` |
| `estatico/fontes/montserrat-OFL.txt` | 4,3 KB | `8b7141c03fa4f8d44e6345d5d4931709290f0f67875e452e95ac1fd3a027802e` |

Os eixos sobreviveram ao recorte, que é o que importa conferir depois de mexer
num arquivo de fonte: a Archivo mantém `wght 100..900` e `wdth 62..125`, a
Montserrat mantém `wght 100..900`. O `@font-face` precisa declarar essas
faixas — sem a declaração, o navegador assume que o arquivo só tem o padrão e
ignora o resto.

**Licença:** SIL Open Font License 1.1, em `estatico/fontes/archivo-OFL.txt` e
`estatico/fontes/montserrat-OFL.txt`. Ela permite usar, embutir e redistribuir,
e é por isso que as duas podem morar aqui.

## Os logotipos

`logo-lee-preto.svg` e `logo-lee-advogado-branco.svg` são do titular. São
**caminhos, não texto**: não dependem de fonte instalada e não desandam
enquanto a Archivo carrega. Carregam o metadado C2PA de proveniência do
arquivo original, que foi preservado — não cabe a quem publica apagar a
proveniência de uma peça de arte.

O `PROCEDENCIA.md` de origem não registra resumo para os dois. Os valores
abaixo foram calculados no dia da cópia e passam a ser a referência deste
repositório.

| Arquivo guardado | Tamanho | SHA-256 |
|---|---|---|
| `estatico/logo-lee-preto.svg` | 11 KB | `3fd42a96db0c8715828c3b66b0c10bc132974b4efbfbc116234484a18f093269` |
| `estatico/logo-lee-advogado-branco.svg` | 15 KB | `1d3cdc7e193b4e9d25575ed4a79e05a9d7a9cf66ef74f5a08a5aefd3f02dfc52` |

## Como conferir

Na raiz do repositório:

```
sha256sum estatico/fontes/*.woff2 estatico/fontes/*.txt estatico/*.svg
```

Qualquer divergência significa que o arquivo foi mexido. Nesse caso, não
corrija o resumo: descubra o que mexeu nele.
