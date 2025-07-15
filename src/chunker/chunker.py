import os

from docling import chunking
from docling.document_converter import DocumentConverter
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from transformers import AutoTokenizer


class Chunker:
    def __init__(self, embedding_model: str, max_tokens: int = 1024):
        tokenizer = HuggingFaceTokenizer(
            tokenizer=AutoTokenizer.from_pretrained(embedding_model),
            max_tokens=max_tokens,
        )
        self.__chunker = chunking.HybridChunker(tokenizer=tokenizer, merge_peers=True)

    def chunk(self, source: str):
        doc = DocumentConverter().convert(source=source).document
        chunk_iter = self.__chunker.chunk(dl_doc=doc)
        chunks = list(chunk_iter)
        chunks_dicts = []
        for chunk in chunks:
            chunks_dicts.append(
                {
                    "content": chunk.text,
                    "page_number": chunk.meta.doc_items[0].prov[0].page_no,
                    "pdf_name": os.path.basename(source),
                }
            )
        return chunks_dicts
