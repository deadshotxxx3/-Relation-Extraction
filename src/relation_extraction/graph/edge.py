from dataclasses import dataclass
from RelationExtraction.src.relation_extraction.graph.node import Node


@dataclass
class Edge:
    source: Node
    target: Node
    relation: str