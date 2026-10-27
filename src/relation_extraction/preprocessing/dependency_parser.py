from RelationExtraction.src.relation_extraction.models.token import Token
from RelationExtraction.src.relation_extraction.models.dependency import Dependency


class DependencyParser:
    def parse(self, tokens: list[Token]) -> list[Dependency]:
        return [
            Dependency(
                dependent=token.index,
                head=token.head,
                relation=token.dep,
            )
            for token in tokens
            if token.head is not None and token.dep is not None
        ]