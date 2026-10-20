# Algoritmo de Kruskal — Seminário AV2 de Grafos

Implementação em **Python** do algoritmo de Kruskal, que encontra uma **árvore geradora mínima (AGM)** em um grafo não direcionado, ponderado e conexo. O exemplo corresponde ao relatório do seminário: interligar cinco pontos de uma escola usando a menor extensão total de cabos.

## Problema escolhido

Os pontos A, B, C, D e E representam locais da escola que precisam estar conectados por cabos. Cada aresta corresponde a um trecho de cabo possível e seu peso representa **dezenas de metros** (por exemplo, peso `4` representa `40 m`). O objetivo é interligar todos os pontos, direta ou indiretamente, sem circuitos redundantes e com a menor extensão de cabo.

| Conexão possível | Peso | Comprimento |
|---|---:|---:|
| A–B | 4 | 40 m |
| A–C | 2 | 20 m |
| B–C | 1 | 10 m |
| B–D | 5 | 50 m |
| C–D | 8 | 80 m |
| C–E | 9 | 90 m |
| D–E | 3 | 30 m |

Os comprimentos são **fictícios e apenas didáticos**, não resultados de medições reais.

## Requisitos e dependências

- **Python 3.9 ou superior**.
- **Nenhuma biblioteca externa.** Apenas recursos da biblioteca padrão (`typing` e `unittest`).
- Não é necessário executar `pip install`.

## Como executar

1. Instale Python 3.9+ se ainda não tiver. Confirme a versão no terminal:

   ```bash
   python --version
   ```

2. Clone o repositório (ou baixe o ZIP). Na raiz do repositório, entre na pasta `codigo`:

   ```bash
   cd codigo
   ```

3. Execute o programa:

   ```bash
   python kruskal.py
   ```

   Em sistemas nos quais o executável se chama `python3`, use `python3 kruskal.py`.

## Saída esperada

```text
ALGORITMO DE KRUSKAL - REDE DE CABOS DA ESCOLA
Unidade dos pesos: dezenas de metros (1 = 10 metros)

Arestas analisadas em ordem crescente de peso:
  1. B-C | peso 1 | ADICIONADA
  2. A-C | peso 2 | ADICIONADA
  3. D-E | peso 3 | ADICIONADA
  4. A-B | peso 4 | DESCARTADA (ciclo)
  5. B-D | peso 5 | ADICIONADA

Árvore geradora mínima:
  B-C: peso 1 (10 m)
  A-C: peso 2 (20 m)
  D-E: peso 3 (30 m)
  B-D: peso 5 (50 m)

Peso total: 11 dezenas de metros = 110 metros de cabo
Quantidade de conexões: 4
```

As arestas `C–D` e `C–E` não são analisadas porque o algoritmo termina assim que seleciona `|V| - 1 = 4` arestas.

## Como o algoritmo funciona

1. Ordena as arestas pelo peso, da menor para a maior.
2. Inicializa cada vértice como seu próprio conjunto na estrutura *Union-Find*.
3. Examina a menor aresta ainda disponível: se liga componentes diferentes, adiciona à solução; se cria ciclo, descarta.
4. Termina quando possui `|V| - 1` arestas, formando uma árvore geradora mínima.

A classe `UnionFind` usa **compressão de caminho** em `find` e **união por rank** em `union` para manter eficiente a verificação de ciclos.

## Resultado

As conexões escolhidas são **B–C (10 m), A–C (20 m), D–E (30 m) e B–D (50 m)**, totalizando **110 m de cabo**. Todos os cinco pontos ficam conectados e não há ciclos.

## Executar os testes (opcional)

Estando na pasta `codigo`, execute:

```bash
python -m unittest -v
```

Os testes verificam o resultado do exemplo, a rejeição de um grafo desconexo, o caso de apenas um vértice e a independência em relação à ordem inicial das arestas.

## Arquivos

```text
Entrega_Kruskal/
├── Relatorio_Algoritmo_de_Kruskal.pdf
├── Relatorio_Algoritmo_de_Kruskal.docx
├── README.md
├── roteiro_apresentacao.md
└── codigo/
    ├── kruskal.py
    ├── test_kruskal.py
    └── README.md
```

O **relatório** contém definição formal, pseudocódigo, justificativa de implementação, análise de complexidade, modelagem do grafo e resolução completa. O código-fonte deve ser enviado ao **GitHub**, conforme o enunciado do seminário.

## Referências teóricas

- CORMEN, Thomas H. et al. *Introduction to Algorithms*. 4. ed. Cambridge: MIT Press, 2022.
- KRUSKAL, Joseph B. On the shortest spanning subtree of a graph and the traveling salesman problem. *Proceedings of the American Mathematical Society*, v. 7, n. 1, p. 48–50, 1956. DOI: https://doi.org/10.1090/S0002-9939-1956-0078686-7.
