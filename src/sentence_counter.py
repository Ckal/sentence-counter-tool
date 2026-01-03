from transformers import AutoTokenizer
from transformers import Tool

class SentenceCounterTool(Tool):
    name = "sentence_counter"
    description = "This tool counts the sentences of a text."
    inputs = ["text"]
    outputs = ["text"]

    def __call__(self, text: str):
        print(text)
        print("----")
        sentences = text.split(". ")
        print(len(sentences))
        return len(sentences)
        