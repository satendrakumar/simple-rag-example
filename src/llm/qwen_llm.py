import torch
from transformers import pipeline


class QwenLLM:

    def __init__(self, model_id: str = "Qwen/Qwen1.5-1.8B"):
        self.pipe = pipeline(
            "text-generation",
            model=model_id,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            trust_remote_code=True,
            return_full_text=False
        )

    def invoke(self, prompt: str, max_new_tokens: int = 512) -> str:
        response = self.pipe(
            prompt,
            max_new_tokens=max_new_tokens,
            pad_token_id=self.pipe.tokenizer.eos_token_id
        )
        return response[0]['generated_text']
