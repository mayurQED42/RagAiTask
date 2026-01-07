from sentence_transformers import SentenceTransformer
from typing import List
from numpy import ndarray

class EmbeddingGenerator:
    def __init__(self, model_name: str = "intfloat/e5-small-v2"):
        """
        Initializes the embedding model.
        """
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: List[str]) -> ndarray:
        """
        Generates normalized vector embeddings for a list of text chunks.
        """
        if not texts:
            return []

        # E5 models expect "passage:" prefix for documents
        formatted_texts = [f"passage: {text}" for text in texts]

        embeddings = self.model.encode(
            formatted_texts,
            batch_size=8,
            show_progress_bar=True,
            normalize_embeddings=True
        )

        return embeddings


if __name__ == "__main__":
    docs = [
        "Python is a popular programming language.",
        "Streamlit helps build data apps quickly."
    ]

    embedder = EmbeddingGenerator()
    embeddings = embedder.embed_documents(docs)

    print(f"Generated {len(embeddings)} embeddings of dimension {embeddings.shape[1]}")

