# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md
from typing import List
from cog import BasePredictor, Input, BaseModel
from sentence_transformers import SentenceTransformer

class Item(BaseModel):
    text: str
    embedding: List[float]

class Output(BaseModel):
    items: List[Item]

class Predictor(BasePredictor):
    def setup(self) -> None:
        """Load the model into memory"""
        self.model = SentenceTransformer('thenlper/gte-base')

    def predict(
            self,
            text: str = Input(description="Text strings to embed (separated by newlines)"),
    ) -> Output:
        """Run prediction on text with lines separated by newlines"""

        # Split the input text by newlines into a list of text strings
        texts = text.split("\n")

        # Remove empty strings
        texts = [t.strip() for t in texts if t.strip()]

        # Embed the texts
        embeddings = self.model.encode(texts)

        # Create a list of Item objects, each containing input and embedding
        items = [Item(text=text, embedding=embedding.tolist()) for text, embedding in zip(texts, embeddings)]

        return Output(items=items)
