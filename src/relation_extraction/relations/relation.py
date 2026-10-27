from dataclasses import dataclass


@dataclass
class Relation:
    subject: str
    predicate: str
    object: str