# Modelos de carrossel — Grupo E-SOL

Modelos de carrossel institucional (1080×1350, 4:5) para import no Canva, com a **órbita do e·sol**
aplicada por comprimento. Cada slide é marcado com `data-document-role="page"`, então o Canva
importa cada um como uma **página editável** (texto nativo + órbita vetorial).

## Arquivos

- `gen_carrossel.py` — gerador. Produz os `carrossel-N.html` (N = 3,4,6,7,8,9,10) a partir do
  conteúdo e da fórmula da órbita. Requer só Python 3 (usa `math`, sem dependências).
- `carrossel-N.html` — modelos gerados (não editar à mão; edite o gerador e rode de novo).
- `canva-import-carrossel-5.html` — o modelo de 5 slides aprovado (referência).

## Como usar

1. Ajuste conteúdo/estrutura em `gen_carrossel.py` (blocos `b_*` e o dicionário `SEQS`).
2. Rode: `python gen_carrossel.py` (gera os HTML na mesma pasta).
3. `git commit` + `git push`.
4. Importe no Canva a partir do **raw URL** do arquivo (o importador do Canva lê HTTPS público),
   ou suba o HTML pelo próprio Canva ("Criar design → Importar").

## A órbita (sistema travado)

Uma única curva contínua sobre a **tira global** do carrossel: `y(X) = 1080 − 360·sin(π·X/(N·W))`,
`W=1080`. O ponto (o "planeta") avança pela sequência com `cx = W·(i+1)/(N+1)` no slide `i` de `N`,
sempre abaixo da zona de texto. Inversão por fundo: amarelo sobre grafite; grafite sobre amarelo/branco.
Fonte de verdade: `rebranding/regra-ponto-orbital.md` e `design-system/tokens/tokens.base.json → orbita`
no repo do rebranding.
