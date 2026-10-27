from src.relation_extraction.preprocessing.tokenizer import Tokenizer #SentenceSplitter
from src.relation_extraction.preprocessing.dependency_parser import DependencyParser
from src.relation_extraction.graph.graph import DependencyGraph
from src.relation_extraction.relations.extractor import RelationExtractor


def main():
    text = "Иван читает книгу."

    #splitter = SentenceSplitter()
    #sentences = splitter.split(text)
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)

    parser = DependencyParser()
    dependencies = parser.parse(tokens)

    graph = DependencyGraph()
    graph.build(tokens, dependencies)

    extractor = RelationExtractor()
    relations = extractor.extract(graph)

    print("RELATIONS:")
    for relation in relations:
        print(
            f"Subject: {relation.subject} | "
            f"Predicate: {relation.predicate} | "
            f"Object: {relation.object}"
        )

if __name__ == "__main__":
    main()