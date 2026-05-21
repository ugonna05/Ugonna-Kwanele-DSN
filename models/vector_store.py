import faiss
import numpy as np


class VectorStore:

    def __init__(self, embeddings):

        self.embeddings = np.array(
            embeddings
        ).astype("float32")

        dimension = self.embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(self.embeddings)

    def search(self, query_embedding, top_k=5):

        query_embedding = np.array(
            query_embedding
        ).astype("float32")

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        return distances, indices