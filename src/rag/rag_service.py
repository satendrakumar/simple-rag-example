import torch
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from transformers import pipeline

from src.embedding.custom_embedding import CustomEmbeddings

model_id = "Qwen/Qwen1.5-1.8B"

text_splitter = RecursiveCharacterTextSplitter(chunk_size=2024, chunk_overlap=128, add_start_index=True)
pdf_loader: PyPDFLoader = PyPDFLoader("data/829cf27a-8b4f-458b-b51b-24d491d3fd2c.pdf")
documents: list[Document] = pdf_loader.load_and_split(text_splitter)
embeddings = CustomEmbeddings("BAAI/bge-m3")
db = FAISS.from_documents(documents=documents, embedding=embeddings)

PROMPT = """You are an expert financial research analyst specializing in comprehensive company analysis. Your role is to provide accurate, insightful, and actionable responses based on thorough examination of company data and market intelligence.

**Instructions:**
- Analyze the provided context thoroughly before responding
- Provide concise yet comprehensive answers that directly address the question
- Support your analysis with specific data points and evidence from the context
- Maintain a professional, objective tone while being accessible to your audience
- If the context is insufficient to answer the question completely, clearly state what additional information would be needed
- Structure your response logically with clear reasoning

**Context:**
{context}

**Question:**
{question}

**Analysis & Response:**
[Provide your answer here, ensuring it is well-structured, evidence-based, and directly addresses the question posed]

**Key Insights:**
[If applicable, highlight 2-3 critical takeaways that support your analysis]

**Confidence Level:** [High/Medium/Low based on the quality and completeness of available context]
"""

question = "how should we think about the growth in this vertical over the next couple of quarters going ahead?"


def query_faiss_db(question: str, db: FAISS, k: int = 5, score_threshold: float = 0.5) -> str:
    relevant_docs_with_scores = db.similarity_search_with_score(question, k=k)
    context = ""
    relevant_count = 0
    for doc, score in relevant_docs_with_scores:
        if score >= score_threshold:  # Only include high-relevance documents
            relevant_count += 1
            context += f"Relevant Extract {relevant_count} (Relevance: {score:.3f}):\n{doc.page_content}\n\n"

    if relevant_count == 0:
        context = "No highly relevant information found in the database for this query."
    return context.strip()


def create_qwen_rag_response(question: str, db: FAISS, k: int = 5):
    context = query_faiss_db(question, db, k, score_threshold=0.25)
    prompt_template = PromptTemplate(template=PROMPT, input_variables=["context", "question"])
    formatted_prompt = prompt_template.format(context=context, question=question)
    pipe = pipeline(
        "text-generation",
        model="Qwen/Qwen1.5-1.8B",
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
        return_full_text=False
    )
    response = pipe(
        formatted_prompt,
        max_new_tokens=1024,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
        pad_token_id=pipe.tokenizer.eos_token_id
    )
    return response[0]['generated_text']


# Use the complete pipeline
final_response = create_qwen_rag_response(question, db, k=5)
print("\nFinal RAG Response:")
print(final_response)
