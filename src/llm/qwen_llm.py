from typing import List, Dict, Tuple

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


class QwenLLM:

    def __init__(self, model_name: str = "Qwen/Qwen3-1.7B"):
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self.device = None
        self._load_model()

    def _load_model(self) -> None:
        print(f"Loading model: {self.model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        self.device = self.model.device
        print(f"Model loaded successfully on device: {self.device}")

    def _prepare_messages(self, prompt: str) -> List[Dict[str, str]]:
        return [{"role": "user", "content": prompt}]

    def _parse_thinking_content(self, output_ids: List[int]) -> Tuple[str, str]:
        try:
            # Find the index of </think> token (151668)
            index = len(output_ids) - output_ids[::-1].index(151668)
        except ValueError:
            # If </think> token not found, no thinking content
            index = 0
        thinking_content = self.tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
        main_content = self.tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

        return thinking_content, main_content

    def invoke(self,
               prompt: str,
               max_new_tokens: int = 1024,
               enable_thinking: bool = True,
               return_thinking: bool = True,
               **generation_kwargs) -> Dict[str, str]:
        messages = self._prepare_messages(prompt)
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=enable_thinking
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.device)
        with torch.no_grad():
            generated_ids = self.model.generate(
                **model_inputs,
                max_new_tokens=max_new_tokens,
                **generation_kwargs
            )
        output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()
        if enable_thinking and return_thinking:
            thinking_content, main_content = self._parse_thinking_content(output_ids)
            return {
                "response": main_content,
                "thinking": thinking_content
            }
        else:
            content = self.tokenizer.decode(output_ids, skip_special_tokens=True).strip("\n")
            return {
                "response": content,
                "thinking": ""
            }
