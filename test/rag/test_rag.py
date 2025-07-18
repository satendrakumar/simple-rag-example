import pandas as pd

from src.chunker.chunker import Chunker
from src.embedding.custom_embedding import CustomEmbeddings
from src.llm.qwen_llm import QwenLLM
from src.prompt.prompt_template import PromptTemplate
from src.storage.lancedb import LanceDB

pdf_data = "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_LongerReport.pdf"

EMBEDDING_MODEL = "BAAI/bge-m3"
LLM_MODEL = "Qwen/Qwen3-1.7B"

if __name__ == '__main__':
    # initialize the embedding model
    embeddings = CustomEmbeddings(model_name=EMBEDDING_MODEL)

    # initialize the LLM
    llm = QwenLLM(model_name=LLM_MODEL)

    # initialize the Chunker
    chunker = Chunker(embedding_model=EMBEDDING_MODEL)

    # initialize the Vector DB
    lancedb = LanceDB(table_name="rag_table")
    # Run document Indexing
    print("Start Chunking ....")
    documents = chunker.chunk(pdf_data)
    print("Chunking done....")
    df = pd.DataFrame(documents, columns=["content", "page_number", "pdf_name"])
    print("Start Embedding ....")
    df["embeddings"] = df["content"].apply(embeddings.embed_query)
    print("Embedding  done....")
    print(df)
    print("Start saving ....")
    lancedb.save(df)

    # RAG
    query = "How is climate change affecting biodiversity?"

    vector_query = embeddings.embed_query(query)
    result_df = lancedb.semantic_search(vector_query=vector_query, n=2)
    context = "\n\n".join(result_df["content"].tolist())
    formatted_prompt = PromptTemplate.build(context=context, question=query)
    print("\nFormatted Prompt:" + "\n" + formatted_prompt)
    final_response = llm.invoke(formatted_prompt, enable_thinking=True, return_thinking=True)
    print("\nFinal RAG Response:")
    print(final_response["response"])
