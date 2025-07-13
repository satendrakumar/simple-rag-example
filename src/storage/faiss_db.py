from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings


class FaissDB:
    def __init__(self, data_dir: str, embeddings: Embeddings):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2024, chunk_overlap=128, add_start_index=True)
        pdf_loader: PyPDFLoader = PyPDFLoader(data_dir)
        documents: list[Document] = pdf_loader.load_and_split(text_splitter)
        self.__db = FAISS.from_documents(documents=documents, embedding=embeddings)

    def query(self, question: str, k: int = 5, similarity_score_threshold: float = 0.5) -> str:
        relevant_docs_with_scores = self.__db.similarity_search_with_score(question, k=k)
        context = ""
        relevant_count = 0
        for doc, score in relevant_docs_with_scores:
            if score >= similarity_score_threshold:  # Only include high-relevance documents
                relevant_count += 1
                context += f"Relevant Extract {relevant_count} (Relevance: {score:.3f}):\n{doc.page_content}\n\n"
        if relevant_count == 0:
            context = "No highly relevant information found in the database for this query."
        return context.strip()
