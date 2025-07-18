from typing import List

import torch
from sentence_transformers import SentenceTransformer


class CustomEmbeddings:

    def __init__(
            self,
            model_name: str,
            trust_remote_code: bool = True,
            device: str = torch.device("cuda" if torch.cuda.is_available() else "cpu"),
            normalize_embeddings: bool = True,
    ):
        self.model_name = model_name
        self.normalize_embeddings = normalize_embeddings
        self.model = SentenceTransformer(
            model_name,
            trust_remote_code=trust_remote_code,
            device=device,
        )

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        embeddings = self.model.encode(
            texts,
            normalize_embeddings=self.normalize_embeddings,
            convert_to_tensor=False
        )
        return embeddings.tolist()

    def embed_query(self, text: str) -> List[float]:
        embedding = self.model.encode(
            text,
            normalize_embeddings=self.normalize_embeddings,
            convert_to_tensor=False
        )
        return embedding.tolist()

    @property
    def embedding_dimension(self) -> int:
        """Get the dimension of the embeddings."""
        return self.model.get_sentence_embedding_dimension()




