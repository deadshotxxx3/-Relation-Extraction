from dataclasses import dataclass


@dataclass
class SemEvalExample:
    sentence: str
    entity1: str
    entity2: str
    relation: str | None = None
