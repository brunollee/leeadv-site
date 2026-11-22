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
15/11/2026. A foto original, o script de tratamento e os arquivos em tamanho
cheio ficam na pasta de trabalho do titular, fora deste repositório. O que
entra aqui são só os seis derivados de 600x600, três pares de AVIF e WebP.

O recorte separou fundo e pele pela diferença entre o vermelho e o verde, e o
fundo foi substituído: #ececea na versão clara, branco puro na versão branca
e #1f1f1f na escura. É por isso que são três pares e não um, e é por isso que
o CSS não desenha fundo nem borda atrás do círculo: o fundo já está dentro da
imagem.

### O que foi refeito em 21/11/2026

Até esta data valia, para o retrato, a frase que esta seção ainda usa para a
imagem de compartilhamento: nada havia sido gerado, convertido ou alterado por
quem escreveu estas linhas. **Deixou de valer.** Os seis arquivos foram
reescritos aqui dentro, e os resumos abaixo são os dos arquivos novos.

**O aro claro, nos seis arquivos.** O recorte original guardava de 2 a 3
pixels do fundo claro do estúdio na borda do círculo, e sobre a página escura
isso aparecia como um aro claro em volta da cabeça. O conserto mexeu **só na
máscara de transparência**: o círculo passou de 300 para 296,5 pixels de raio,
com meio pixel de suavização, e os pixels que a máscara nova descarta
receberam a cor do anel imediatamente interno, para o navegador não ter cor
clara nenhuma para interpolar ao reduzir a imagem. Nenhum pixel da fotografia
foi reamostrado, recolorido ou movido.

**O tom do fundo, só no `retrato-escuro`.** Por decisão do titular, o disco
deixou de aparecer por um tom e passou a sumir na página: o fundo chapado
desceu de #1f1f1f para #0f0f0f, o `--bg`. A região foi identificada por
preenchimento a partir da borda do círculo, com tolerância de 7 níveis, que
não vaza pelo cabelo e para no terno; a borda da máscara entra suavizada, para
não deixar degrau. O desconto é medido pela mediana do próprio fundo de cada
arquivo, e não fixado, porque o WebP e o AVIF guardam valores um pouco
diferentes e precisam chegar no mesmo tom. Atinge 42,2% do disco, e nenhum
pixel da pessoa.

O efeito colateral foi apresentado e aceito na hora: sem o disco, o corte
circular nos ombros vira uma borda dura. **Em 22/11/2026 a decisão foi
revista**, depois de ver no ar, e a página inicial voltou ao disco branco. O
`retrato-escuro` ficou com o fundo #0f0f0f e sem uso; não foi revertido para
o #1f1f1f, porque reverter bytes de imagem sem necessidade só gera ruído no
histórico. Quem precisar da versão de #1f1f1f, ela está no commit anterior.

Quem for conferir: comparar com a versão anterior no histórico. Os resumos
antigos, que valiam até 20/11/2026, estão no commit anterior ao de
21/11/2026.

### Onde cada par é usado

| Par | Fundo dentro da imagem | Onde |
|---|---|---|
| `retrato-branco` | branco puro | `index.html`, seção da trajetória; e o bloco do autor dos artigos. Nos dois, sobre fundo escuro |
| `retrato-escuro` | #0f0f0f | sem uso em página desde 22/11/2026 |
| `retrato-claro` | #ececea | sem uso em página |

O mesmo par serve aos dois lugares porque os dois têm fundo escuro, e sobre
escuro o disco branco é destaque. No bloco do autor isso vale desde
22/11/2026, quando o cartão passou de branco a `--bg`; entre 21/11 e
22/11/2026 o cartão era branco e o disco não aparecia.

Nenhum dos dois pares fora de uso foi apagado: são registro do que esteve
publicado. O `retrato-claro` foi feito para o `--papel-2` da versão clara do
site, que não existe mais.

| Arquivo guardado | Formato | Dimensões | Tamanho | SHA-256 |
|---|---|---|---|---|
| `estatico/retrato/retrato-escuro.avif` | AVIF | 600x600 | 28.982 B | `d5dd44f71d5dcaf1c0af3f8e4e1d8578e429cd682d37b0d4304e46fcc5ddc62d` |
| `estatico/retrato/retrato-escuro.webp` | WebP | 600x600 | 29.168 B | `5a20475ee1a6df7a0661cfb7636b20fadffeaecf348fe43ece3b9cd9afa54b08` |
| `estatico/retrato/retrato-claro.avif` | AVIF | 600x600 | 29.895 B | `fc55ca84d3fe3a00229a194bc1690dd5b120ce9c7116447c46ec10bfc42f7bc5` |
| `estatico/retrato/retrato-claro.webp` | WebP | 600x600 | 27.830 B | `945341a4ac33ef7c10b8f3550868379cb9d97b771ccc5fbc1b06c47d7a54481b` |
| `estatico/retrato/retrato-branco.avif` | AVIF | 600x600 | 29.809 B | `93e4fc0e18a2d262c7f3c1608bb6d52de44d30aab61306016ea85a3bbe385b9f` |
| `estatico/retrato/retrato-branco.webp` | WebP | 600x600 | 28.054 B | `5b2fc247614aeaec98bd257b6b0f17ab837b6911177b23a76bf575d5af76dfad` |

Os formatos e as dimensões foram lidos dos próprios bytes, e não do nome do
arquivo: as caixas `ftypavif` e `ispe` nos AVIF, o cabeçalho `RIFF`/`WEBP` nos
WebP. Nenhum PNG e nenhum JPEG entram no site.

O navegador baixa **um** arquivo por página, e não os seis: o `<picture>`
escolhe pelo formato que o navegador aceita, e cada página referencia um par
só.

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
