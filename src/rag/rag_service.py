from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings

from src.llm.qwen_llm import QwenLLM
from src.storage.faiss_db import FaissDB

faiss_db = FaissDB(data_dir="data/IPCC_AR6_SYR_LongerReport.pdf",
                   embeddings=HuggingFaceEmbeddings(model_name="BAAI/bge-m3"))

llm = QwenLLM(model_id="Qwen/Qwen1.5-1.8B", )

PROMPT = """You are a knowledgeable Climate Science Assistant, here to help people understand climate change using the latest IPCC research. You communicate complex science clearly and compassionately.

**Your Approach:**
- Answer questions using solid IPCC scientific evidence
- Explain concepts in accessible language for all audiences
- Be honest about uncertainties while providing clear guidance
- Support responses with specific data and findings
- Remain helpful, accurate, and encouraging
- **Keep responses under 256 tokens**

**Available Scientific Context (IPCC 2023 Synthesis Report):**
{context}

**Question:**
{question}

**Your Response (max 256 tokens):**

"""


def run(question: str):
    context = faiss_db.query(question=question, similarity_score_threshold=0.50)
    prompt_template = PromptTemplate(template=PROMPT, input_variables=["context", "question"])
    formatted_prompt = prompt_template.format(context=context, question=question)
    print("\nFormatted Prompt:" + "\n" + formatted_prompt)
    final_response = llm.invoke(formatted_prompt)
    print("\nFinal RAG Response:")
    print(final_response)
    return final_response
