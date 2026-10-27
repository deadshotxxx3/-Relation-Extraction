from RelationExtraction.src.relation_extraction.graph.graph import DependencyGraph
from RelationExtraction.src.relation_extraction.relations.relation import Relation


class RelationExtractor:
    def extract(self, graph: DependencyGraph) -> list[Relation]:
        relations = []

        for node in graph.nodes.values():
            token = node.token

            if token.pos != "VERB":
                continue

            children = graph.get_children(token.index)

            subjects = [
                child.token for child in children
                if child.token.dep in {"nsubj", "nsubj:pass"}
            ]

            objects = [
                child.token for child in children
                if child.token.dep in {"obj", "iobj"}
            ]

            for subject in subjects:
                for obj in objects:
                    relations.append(
                        Relation(
                            subject=subject.text,
                            predicate=token.lemma,
                            object=obj.lemma,
                        )
                    )

        return relations