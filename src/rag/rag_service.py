from langchain_huggingface import HuggingFaceEmbeddings

from src.llm.qwen_llm import QwenLLM
from src.prompt.prompt_builder import build_prompt
from src.storage.faiss_db import FaissDB

pdf_data = "data/IPCC_AR6_SYR_LongerReport.pdf"

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")

faiss_db = FaissDB(data_dir=pdf_data, embeddings=embeddings)

llm = QwenLLM(model_id="Qwen/Qwen1.5-1.8B", )


def run(question: str):
    context = faiss_db.query(question=question, score_threshold=0.50)
    formatted_prompt = build_prompt(context=context, question=question)
    print("\nFormatted Prompt:" + "\n" + formatted_prompt)
    final_response = llm.invoke(formatted_prompt)
    print("\nFinal RAG Response:")
    print(final_response)
    return final_response
