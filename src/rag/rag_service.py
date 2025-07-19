import pandas as pd

from src.chunker.chunker import Chunker
from src.config.config import EMBEDDING_MODEL, LLM_MODEL
from src.embedding.custom_embedding import CustomEmbeddings
from src.llm.qwen_llm import QwenLLM
from src.prompt.prompt_template import PromptTemplate
from src.storage.lancedb import LanceDB

pdf_data = "data/IPCC_AR6_SYR_LongerReport.pdf"


class RAGService:
    def __init__(self):
        self.embeddings = CustomEmbeddings(model_name=EMBEDDING_MODEL)
        self.llm = QwenLLM(model_name=LLM_MODEL)
        self.chunker = Chunker(embedding_model=EMBEDDING_MODEL)
        self.lancedb = LanceDB()
        count = self.lancedb.get_count()
        print(f"Count: {count}")
        if count < 1:
            print("Database is empty. Chunking and embedding started....")
            documents = self.chunker.chunk(pdf_data)
            print("Chunking done....")
            df = pd.DataFrame(documents, columns=["content", "page_number", "pdf_name"])
            df["embeddings"] = df["content"].apply(self.embeddings.embed_query)
            print(df)
            self.lancedb.save(df)
        else:
            print("Database already indexed. Skipping chunking and embedding.")


    def run(self, question: str, enable_thinking: bool):
        vector_query = self.embeddings.embed_query(question)
        result_df = self.lancedb.semantic_search(vector_query=vector_query, n=2)
        context = "\n\n".join(result_df["content"].tolist())
        formatted_prompt = PromptTemplate.build(context=context, question=question)
        print("\nFormatted Prompt:" + "\n" + formatted_prompt)
        final_response = self.llm.invoke(formatted_prompt, enable_thinking=enable_thinking, return_thinking=enable_thinking)
        print("\nFinal RAG Response:")
        print(final_response)
        return final_response
