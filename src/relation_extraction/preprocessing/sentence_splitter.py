import spacy


class SentenceSplitter:
    def __init__(self):
        self.nlp = spacy.load("ru_core_news_sm")

    def split(self, text: str):
        doc = self.nlp(text)

        return [sentence.text for sentence in doc.sents]