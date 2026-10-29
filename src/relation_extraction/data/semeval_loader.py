import re
from src.relation_extraction.models.semeval_example import SemEvalExample


class SemEvalLoader:
    def parse_example(self, text: str, relation: str | None = None) -> SemEvalExample:
        entity1_match = re.search(r"<e1>(.*?)</e1>", text)
        entity2_match = re.search(r"<e2>(.*?)</e2>", text)

        if entity1_match is None or entity2_match is None:
            raise ValueError("Sentence must contain both e1 and e2")

        entity1 = entity1_match.group(1)
        entity2 = entity2_match.group(1)

        sentence = re.sub(r"</?e[12]>", "", text)

        return SemEvalExample(
            sentence=sentence,
            entity1=entity1,
            entity2=entity2,
            relation=relation,
        )
