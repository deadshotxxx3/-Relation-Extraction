from src.relation_extraction.data.semeval_loader import SemEvalLoader
from src.relation_extraction.parsing.parser import Parser
from src.relation_extraction.graph.graph import DependencyGraph


def find_entity_index(tokens, entity):
    for token in tokens:
        if token.text == entity:
            return token.index

    raise ValueError(f"Entity not found: {entity}")


def main():
    text = (
        "Sudden <e1>death</e1> from <e2>inhalation</e2> "
        "of petroleum distillates is well recognised in misuses of "
        "volatile substances."
    )

    loader = SemEvalLoader()
    example = loader.parse_example(text)

    print("Sentence:")
    print(example.sentence)

    print()
    print("Entity 1:", example.entity1)
    print("Entity 2:", example.entity2)

    parser = Parser()
    tokens, dependencies = parser.parse(example.sentence)

    entity1_index = find_entity_index(tokens, example.entity1)
    entity2_index = find_entity_index(tokens, example.entity2)

    print()
    print("Entity 1 index:", entity1_index)
    print("Entity 2 index:", entity2_index)

    graph = DependencyGraph()
    graph.build(tokens, dependencies)

    path = graph.shortest_path(
        entity1_index,
        entity2_index,
    )

    print()
    print("Shortest path:")

    for node in path:
        print(node.token.text)


if __name__ == "__main__":
    main()