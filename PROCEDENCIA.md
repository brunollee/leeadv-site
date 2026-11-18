# De onde veio cada arquivo guardado aqui

O que entra neste repositório vindo de fora tem **procedência registrada**,
com origem, data e resumo SHA-256. Sem isso, daqui a dois anos ninguém sabe
se o arquivo é o mesmo que foi conferido um dia ou um que alguém colou de um
fórum.

Nada aqui é buscado em tempo de execução. Nem fonte, nem folha de estilo, nem
script. Uma página que busca fonte fora conta a esse terceiro cada vez que
alguém a abre, e deixa de desenhar no dia em que o terceiro é o problema.

## As fontes em uso: Literata, Source Sans 3 e Jost

Instaladas em **17/11/2026**, no lugar das duas fontes metricamente compatíveis com a
Cambria e a Calibri, junto com a inversão do site para o claro.

**Por que estas três.** As peças do escritório passaram a ser escritas em
Constantia e Corbel, que são proprietárias da Microsoft e não podem ser
hospedadas num site público. A Literata e a Source Sans 3 são as equivalentes
de tela, de licença livre: uma serifada de leitura longa no papel da
Constantia, uma sem serifa humanista no papel da Corbel. A Jost, geométrica,
faz só o rótulo pequeno em caixa alta, no papel da Century Gothic. Não há
compatibilidade métrica entre elas e as da Microsoft, nem se promete: a
continuidade é de desenho e de função.

| Família | Uso no site | Arquivos |
|---|---|---|
| Literata | títulos (`--titulo`) | regular 400, itálico 400, negrito 700 |
| Source Sans 3 | corpo (`--texto`) | regular 400, seminegrito 600 |
| Jost | rótulo em caixa alta (`--rotulo`) | regular 400 |

### Origem

Os três pacotes do Fontsource, no registro npm, nas versões abaixo. Os
`.woff2` são os subconjuntos latinos que esses pacotes distribuem, copiados
**sem reprocessamento**: nenhum foi regerado, reconvertido, recortado ou
tratado de outro modo. As licenças vieram dos mesmos pacotes.

| Família | Pacote | Versão | Licença |
|---|---|---|---|
| Literata | `@fontsource/literata` | 5.3.0 | OFL-1.1 |
| Source Sans 3 | `@fontsource/source-sans-3` | 5.3.1 | OFL-1.1 |
| Jost | `@fontsource/jost` | 5.3.0 | OFL-1.1 |

Na cópia, só o nome do arquivo mudou, para o padrão curto da pasta: por
exemplo, `literata-latin-400-normal.woff2` virou `literata-regular.woff2`. O
conteúdo é byte a byte o do pacote.

| Arquivo guardado | Arquivo de origem no pacote |
|---|---|
| `literata-regular.woff2` | `@fontsource/literata`, `literata-latin-400-normal.woff2` |
| `literata-italic.woff2` | `@fontsource/literata`, `literata-latin-400-italic.woff2` |
| `literata-bold.woff2` | `@fontsource/literata`, `literata-latin-700-normal.woff2` |
| `source-sans-3-regular.woff2` | `@fontsource/source-sans-3`, `source-sans-3-latin-400-normal.woff2` |
| `source-sans-3-semibold.woff2` | `@fontsource/source-sans-3`, `source-sans-3-latin-600-normal.woff2` |
| `jost-regular.woff2` | `@fontsource/jost`, `jost-latin-400-normal.woff2` |
| `literata-LICENCA.txt`, `source-sans-3-LICENCA.txt`, `jost-LICENCA.txt` | o arquivo de licença de cada pacote |

Os nomes de origem e o conteúdo foram conferidos contra os pacotes
`@fontsource/literata` 5.3.0, `@fontsource/source-sans-3` 5.3.1 e
`@fontsource/jost` 5.3.0: cada arquivo guardado é byte a byte idêntico ao
arquivo correspondente do pacote. Para reconferir, instale o pacote na versão
indicada e compare o resumo SHA-256 do arquivo de origem com a tabela de
somas abaixo.

Como os arquivos são o subconjunto latino do próprio pacote, e não um recorte
feito aqui, o comando de recorte que aparece no registro das fontes
anteriores não se aplica a estas.

### A licença das três é a SIL OFL 1.1

A OFL permite usar, embutir, modificar e redistribuir, inclusive o arquivo
recortado que está aqui, desde que a licença acompanhe. Ela acompanha, em
`fontes/literata-LICENCA.txt`, `fontes/source-sans-3-LICENCA.txt` e
`fontes/jost-LICENCA.txt`.

### Os arquivos guardados

As somas dos seis `.woff2` foram informadas junto com os arquivos e
conferidas com `sha256sum` depois de copiados, uma a uma, em 17/11/2026: as
seis bateram. As das três licenças foram calculadas na instalação e passam a
ser a referência deste repositório.

| Arquivo guardado | Tamanho | SHA-256 |
|---|---|---|
| `estatico/fontes/literata-regular.woff2` | 20.420 B | `a60c193b55766b68b922e2327e15c2d8c145532f283a27c3411b9c47a8583d18` |
| `estatico/fontes/literata-italic.woff2` | 21.148 B | `1e98bfbbb4eb8177b9c21b3fd526e1118c4835d21ff870c0d1c25b1ef4409fba` |
| `estatico/fontes/literata-bold.woff2` | 22.004 B | `1f2985e0fc368aac76f95b847cd05ef6ec4bac2733a648098c62edf990756cf5` |
| `estatico/fontes/literata-LICENCA.txt` | 4.506 B | `9895ebc015226accf416b758ac1ca02a2fb4f83a89d316791ef697c3dc0852aa` |
| `estatico/fontes/source-sans-3-regular.woff2` | 15.696 B | `0f73f35e08cde0a2f10c109c6e01d71459d97e4099ecd9a50f1b6c0209e4de2b` |
| `estatico/fontes/source-sans-3-semibold.woff2` | 15.668 B | `14527d193b0e30bc32ef931549a246cdfd286573bb12869b7e052b8101a39d38` |
| `estatico/fontes/source-sans-3-LICENCA.txt` | 4.314 B | `18aabf190848725e2576eefb5c29ba06aac1029d02132252a7f312eac2e50cf3` |
| `estatico/fontes/jost-regular.woff2` | 9.404 B | `f94cffda16515fbb1667a2662d6b46f5610a942fd02fe88d67ff98f776288962` |
| `estatico/fontes/jost-LICENCA.txt` | 4.497 B | `536533cad95838e13777663c4109b802aa662ef1ef285337f0c7f51d35682fdc` |

**São arquivos estáticos, e não variáveis.** Um arquivo por peso e estilo,
declarados separadamente no `@font-face`. Não há eixo de largura nem de peso
para pedir, e nenhum `font-stretch` deve ser aplicado a elas. Peso que não
está na tabela acima não existe: o navegador sintetizaria o negrito, e por
isso o corpo destaca em 600 e o rótulo fica sempre em 400.

## As fontes retiradas em 17/11/2026

**Retiradas em 17/11/2026**, com a inversão do site para o claro. Eram as
duas fontes de tela metricamente compatíveis com a Cambria e a Calibri, uma
serifada nos títulos e uma sem serifa no corpo, instaladas em 15/11/2026 no
lugar da Archivo e da Montserrat.

**Motivo da retirada.** As peças do escritório deixaram de ser escritas em
Cambria e Calibri e passaram a Constantia e Corbel. A compatibilidade métrica
que justificava as duas deixou de servir a qualquer coisa.

O nome das duas não aparece mais em arquivo nenhum do repositório, de
propósito: uma busca por ele deve voltar vazia, e é assim que se percebe,
numa revisão futura, se alguém trouxe uma delas de volta sem querer. O
registro completo, com origem, licença, comando de recorte e os resumos
SHA-256 dos quatro `.woff2` e das duas licenças, continua no histórico do
git: é este mesmo arquivo, `PROCEDENCIA.md`, no commit `1c4c529`.

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

### O arquivo em uso desde 15/11/2026

Com a decisão do escuro fixo, o fundo do retrato passou a ser **branco puro**,
recortado: sobre a página escura o disco branco funcionava como destaque. É
este o par que a página carrega, e dele o navegador baixa **um** arquivo só.

Com a inversão para o claro, em 17/11/2026, o arquivo continuou o mesmo. O
retrato fica sobre o `--papel-2` do bloco da trajetória, e o disco branco
aparece por um tom só, sem moldura.

| Arquivo guardado | Formato | Dimensões | Tamanho | SHA-256 |
|---|---|---|---|---|
| `estatico/retrato/retrato-branco.avif` | AVIF | 600x600 | 29.388 B | `e7c021b1852628403aeaa9a2057aca20940ab620edb20225dd810302a875068e` |
| `estatico/retrato/retrato-branco.webp` | WebP | 600x600 | 29.140 B | `1fc8a89935827890577b66d76c8a9751786e424c1d335caf4dbaf4d6666d6dd9` |

### Os quatro arquivos fora de uso

As versões `retrato-claro` e `retrato-escuro` **deixaram de ser usadas na
página em 15/11/2026**, com a decisão do escuro fixo. Não foram apagadas:
ficam como registro do que esteve publicado entre os commits 564e9ab e o do
passo 4, e para o `og:image` da seção 6.4, que ainda não existe. Nenhuma das
duas é referenciada por qualquer HTML.

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

## A imagem de compartilhamento

Tratada **fora do repositório** e trazida pronta em 15/11/2026, como o
retrato: nada aqui foi gerado, convertido ou alterado por quem escreveu estas
linhas. Os dois arquivos foram conferidos, medidos e registrados como
chegaram. É o retrato sobre o fundo da página, com o nome e a inscrição na
OAB na serifada que o site usava em 15/11/2026, conforme a seção 6.4 do PRD.

| Arquivo guardado | Formato | Dimensões | Tamanho | SHA-256 |
|---|---|---|---|---|
| `estatico/retrato/og-image.webp` | WebP | 1200x630 | 34.304 B | `73fb1d1075754d1053bbc1ab493a085e3f2de2a265ea9c01844251d91ce7a284` |
| `estatico/retrato/og-image.avif` | AVIF | 1200x630 | 28.841 B | `806a0cfff852f618f905ac16a56e57c3d286273babeafac68941e44d979d12db` |

Formato e dimensões lidos dos próprios bytes, e não do nome do arquivo: as
caixas `ftypavif` e `ispe` no AVIF, o cabeçalho `RIFF`/`WEBP` com bloco
`VP8 ` no WebP.

### Qual está em uso, e por quê

**Em uso: o WebP, candidato único.** O AVIF fica no repositório sem ser
referenciado por marcação nenhuma.

O Open Graph define `og:image` como lista, e seria possível declarar os dois
candidatos, cada um com o seu `og:image:type`, deixando o leitor que não
decodifica AVIF pular para o seguinte. A lista existe no protocolo; o que o
protocolo **não** define é como cada leitor escolhe dentro dela.

Daí a decisão, tomada pelo titular em 15/11/2026: dois candidatos trocariam
um risco conhecido, o leitor que não lê AVIF, por um risco que ninguém
consegue medir, o leitor que escolhe o candidato errado. Com um candidato só,
em formato amplamente lido, não há escolha a adivinhar.

O custo é de 5.463 B, a diferença entre os dois arquivos. Não é peso de
página: a imagem de compartilhamento é buscada pelo robô de prévia, uma vez,
e o visitante do site nunca a carrega.

**Quando revisar:** no dia em que o AVIF for lido universalmente pelos
leitores de prévia, o candidato passa a ser o AVIF e o WebP sai, ou entra
como segundo da lista. Até lá, o arquivo AVIF fica guardado justamente para
essa troca não precisar de nova geração.

A URL declarada é absoluta, e não relativa: o leitor de prévia lê a marcação
fora do contexto da página e não resolve caminho relativo.

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
| `estatico/logo-lee-preto.svg` | 3.360 B | `b630b6e451f3bd60cb23f8d609dfb65f503e8a99c352c95c5aa22ece9136a9b3` |
| `estatico/logo-lee-advogado-branco.svg` | 7.655 B | `5bf25c05c14c056af34a58747c26352a0e0c9958e3360ba3d7d1174bde21c9ac` |

### A assinatura em preto, desde 17/11/2026

`logo-lee-advogado-preto.svg` foi gerado pelo titular **a partir do próprio
`logo-lee-advogado-branco.svg`**, trocando só as cores, e trazido pronto em
17/11/2026. O nome passou a `#141414` e o descritor "advogado" a `#6B6B6B`,
o cinza oficial da marca.

Conferido antes de gravar, contra o branco: mesmo `viewBox` (19206x4040),
mesmos nove `path`, a mesma estrutura com os atributos `fill` removidos, e o
mesmo resumo SHA-256 do conteúdo concatenado dos atributos `d`,
`6f777df9c27c395fa662e84cc33520db382ca19d63d69933…`, que é o que define o traço e o que a tabela do C2PA
abaixo registra para o branco. Nenhum `script`, nenhum `href`, nenhum
endereço externo.

| Arquivo guardado | Tamanho | SHA-256 |
|---|---|---|
| `estatico/logo-lee-advogado-preto.svg` | 7.657 B | `5b4ea7fadebdf8619229949da7dc2397f1ef1f709c038e820609419540c0ebee` |

### O manifesto C2PA foi retirado em 16/11/2026

Os dois arquivos carregavam um bloco `<metadata>` de 7.736 B cada, com um
manifesto C2PA de procedência de imagem, e o atributo `xmlns:c2pa` no
elemento raiz. Num site é peso morto: nenhum navegador o lê, e a procedência
que importa aqui é esta página.

**A alteração foi de metadado, não de desenho.** Conferido antes de gravar,
comparando o estado anterior com o posterior: mesmo `viewBox`, mesmo número
de `path`, mesmos valores de `fill`, e o mesmo resumo SHA-256 do conteúdo
concatenado dos atributos `d`, que é o que define o traço.

| Arquivo | Antes | Depois | SHA-256 dos traços, antes e depois |
|---|---|---|---|
| `logo-lee-preto.svg` | 11.134 B | 3.360 B | `6a06e04981514efcaf4caec39e5b066684835692bedca969…` nos dois |
| `logo-lee-advogado-branco.svg` | 15.429 B | 7.655 B | `6f777df9c27c395fa662e84cc33520db382ca19d63d69933…` nos dois |

Os resumos da tabela acima são os dos arquivos novos e passam a ser a
referência. Os anteriores, para quem precisar rastrear o histórico, eram
`3fd42a96db0c8715828c3b66b0c10bc132974b4efbfbc116234484a18f093269` e
`1d3cdc7e193b4e9d25575ed4a79e05a9d7a9cf66ef74f5a08a5aefd3f02dfc52`.

Registro, porque confundiu: até 17/11/2026 esta página dizia que o
`logo-lee-advogado-branco.svg` desenhava apenas a palavra "Lee". Não é
assim. Ele é a assinatura completa, "Lee" e "advogado", em nove `path`: o
nome em branco e o descritor em `#CBCBCB`. Quem desenha só o símbolo "Lee",
num `path` só, é o `logo-lee-preto.svg`.

Desde 17/11/2026, com a inversão para o claro, o cabeçalho e o rodapé de
todas as páginas usam o `logo-lee-advogado-preto.svg`, nas mesmas medidas do
branco (143x30 no cabeçalho, 124x26 no rodapé), porque o desenho e a
proporção são os mesmos. O branco continua guardado para uso dentro do bloco
invertido, e segue como favicon até existir o monograma. O
`logo-lee-preto.svg`, o símbolo isolado, é ativo da marca e fica no
repositório sem uso na página.

Até essa data, o traço do `logo-lee-preto.svg` também estava embutido na
marcação do `index.html`, como o L gigante da abertura. O ornamento saiu com
a inversão, e o `index.html` não carrega mais cópia nenhuma do traço.

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
