"""Algoritmo de Kruskal: conexão mínima de cinco pontos de uma escola.

Os pesos estão expressos em dezenas de metros de cabo.
Exemplo: peso 2 representa 20 metros.

Execução: python kruskal.py
Dependências: somente a biblioteca padrão do Python 3.9+.
"""

from typing import Dict, List, Tuple

Aresta = Tuple[str, str, int]
Etapa = Tuple[str, str, int, bool]

# Instalação de cabos entre os pontos A, B, C, D e E.
VERTICES = ["A", "B", "C", "D", "E"]
ARESTAS: List[Aresta] = [
    ("A", "B", 4),  # 40 m
    ("A", "C", 2),  # 20 m
    ("B", "C", 1),  # 10 m
    ("B", "D", 5),  # 50 m
    ("C", "D", 8),  # 80 m
    ("C", "E", 9),  # 90 m
    ("D", "E", 3),  # 30 m
]


class UnionFind:
    """Mantém os componentes conexos com compressão e união por rank."""

    def __init__(self, vertices: List[str]) -> None:
        self.pai: Dict[str, str] = {vertice: vertice for vertice in vertices}
        self.rank: Dict[str, int] = {vertice: 0 for vertice in vertices}

    def find(self, vertice: str) -> str:
        """Retorna o representante do conjunto do vértice."""
        if self.pai[vertice] != vertice:
            self.pai[vertice] = self.find(self.pai[vertice])
        return self.pai[vertice]

    def union(self, origem: str, destino: str) -> bool:
        """Une conjuntos distintos; retorna False quando formaria ciclo."""
        raiz_origem = self.find(origem)
        raiz_destino = self.find(destino)

        if raiz_origem == raiz_destino:
            return False

        if self.rank[raiz_origem] < self.rank[raiz_destino]:
            raiz_origem, raiz_destino = raiz_destino, raiz_origem

        self.pai[raiz_destino] = raiz_origem
        if self.rank[raiz_origem] == self.rank[raiz_destino]:
            self.rank[raiz_origem] += 1
        return True


def kruskal(
    vertices: List[str], arestas: List[Aresta]
) -> Tuple[List[Aresta], int, List[Etapa]]:
    """Calcula a árvore geradora mínima de um grafo não direcionado conexo.

    Retorna (arestas_escolhidas, peso_total, passos_executados).
    Levanta ValueError caso o grafo seja inválido ou desconexo.
    """
    if not vertices or len(vertices) != len(set(vertices)):
        raise ValueError("Informe uma lista não vazia de vértices distintos.")

    conhecidos = set(vertices)
    for origem, destino, _ in arestas:
        if origem not in conhecidos or destino not in conhecidos:
            raise ValueError("Toda aresta deve ligar vértices informados.")

    conjuntos = UnionFind(vertices)
    arvore: List[Aresta] = []
    total = 0
    passos: List[Etapa] = []

    # Kruskal escolhe arestas em ordem não decrescente de peso.
    for origem, destino, peso in sorted(arestas, key=lambda a: (a[2], a[0], a[1])):
        adicionada = conjuntos.union(origem, destino)
        passos.append((origem, destino, peso, adicionada))

        if adicionada:
            arvore.append((origem, destino, peso))
            total += peso

        # Uma árvore com V vértices tem exatamente V - 1 arestas.
        if len(arvore) == len(vertices) - 1:
            break

    if len(arvore) != len(vertices) - 1:
        raise ValueError("O grafo é desconexo: não existe árvore geradora.")

    return arvore, total, passos


def main() -> None:
    arvore, total, passos = kruskal(VERTICES, ARESTAS)

    print("ALGORITMO DE KRUSKAL - REDE DE CABOS DA ESCOLA")
    print("Unidade dos pesos: dezenas de metros (1 = 10 metros)")
    print("\nArestas analisadas em ordem crescente de peso:")
    for numero, (origem, destino, peso, adicionada) in enumerate(passos, 1):
        situacao = "ADICIONADA" if adicionada else "DESCARTADA (ciclo)"
        print(f"  {numero}. {origem}-{destino} | peso {peso} | {situacao}")

    print("\nÁrvore geradora mínima:")
    for origem, destino, peso in arvore:
        print(f"  {origem}-{destino}: peso {peso} ({peso * 10} m)")

    print(f"\nPeso total: {total} dezenas de metros = {total * 10} metros de cabo")
    print(f"Quantidade de conexões: {len(arvore)}")


if __name__ == "__main__":
    main()
