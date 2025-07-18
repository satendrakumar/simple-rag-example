from src.llm.qwen_llm import QwenLLM
from src.prompt.prompt_template import PromptTemplate

if __name__ == "__main__":
    # Initialize the Qwen LLM
    llm = QwenLLM(model_name="Qwen/Qwen3-1.7B")

    print("===  RAG TEST ===")
    context = """
    The IPCC AR6 Synthesis Report confirms that global surface temperature has 
    increased by 1.1°C (1.9°F) since 1850-1900. Human activities are the main 
    driver of climate change, primarily through emissions of greenhouse gases. 
    Without immediate and large-scale reductions in greenhouse gas emissions, 
    limiting warming to 1.5°C will be beyond reach.
    """

    question = "How much has global temperature increased since the industrial era?"

    prompt = PromptTemplate.build(context, question)
    response = llm.invoke(prompt, max_new_tokens=512)  # Limit tokens for concise response
    print("Question:", question)
    print("Thinking content:", response["thinking"])
    print("Response:", response["response"])