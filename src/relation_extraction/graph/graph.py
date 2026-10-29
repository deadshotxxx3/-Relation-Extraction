import networkx as nx
from RelationExtraction.src.relation_extraction.graph.node import Node
from RelationExtraction.src.relation_extraction.graph.edge import Edge
from RelationExtraction.src.relation_extraction.models.token import Token
from RelationExtraction.src.relation_extraction.models.dependency import Dependency


class DependencyGraph:
    def __init__(self):
        self.nodes: dict[int, Node] = {}
        self.edges: list[Edge] = []

    def build(self, tokens: list[Token], dependencies: list[Dependency]) -> None:
        self.nodes = {token.index: Node(token=token) for token in tokens}
        self.edges = [
            Edge(
                source=self.nodes[dependency.dependent],
                target=self.nodes[dependency.head],
                relation=dependency.relation,
            )
            for dependency in dependencies
            if dependency.dependent != dependency.head
            and dependency.dependent in self.nodes
            and dependency.head in self.nodes
        ]

    def get_node(self, token_index: int) -> Node | None:
        return self.nodes.get(token_index)

    def get_children(self, token_index: int) -> list[Node]:
        return [
            edge.source for edge in self.edges
            if edge.target.token.index == token_index
        ]

    def get_parent(self, token_index: int) -> Node | None:
        for edge in self.edges:
            if edge.source.token.index == token_index:
                return edge.target
        return None

    def shortest_path(self, entity1_index: int, entity2_index: int) -> list[Node]:
        graph = nx.Graph()

        graph.add_nodes_from(self.nodes.keys())

        for edge in self.edges:
            source = edge.source.token.index
            target = edge.target.token.index

            graph.add_edge(source, target)

        path = nx.shortest_path(graph, source=entity1_index, target=entity2_index)

        return [self.nodes[token_index] for token_index in path]