import spacy
from RelationExtraction.src.relation_extraction.models.token import Token


class Tokenizer:
    def __init__(self):
        self.nlp = spacy.load("ru_core_news_sm")

    def tokenize(self, text: str):
        doc = self.nlp(text)
        return [
            Token(
                text=token.text,
                index=token.i,
                lemma=token.lemma_,
                pos=token.pos_,
                tag=token.tag_,
                dep=token.dep_,
                head=token.head.i,
            )
            for token in doc
        ]