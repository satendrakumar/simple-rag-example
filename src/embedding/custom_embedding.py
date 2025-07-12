from langchain.embeddings.base import Embeddings
from sentence_transformers import SentenceTransformer


class CustomEmbeddings(Embeddings):

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return list(map(lambda text: self.model.encode(text).tolist(), texts))

    def embed_query(self, text: str) -> list[float]:
        return self.model.encode(text).tolist()

    def __init__(self, model_name: str = "BAAI/bge-m3"):
        self.model = SentenceTransformer(model_name, trust_remote_code=True)
