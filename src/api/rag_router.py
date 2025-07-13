from fastapi import APIRouter
from pydantic import BaseModel
from starlette import status

from src.rag.rag_service import RAGService

router = APIRouter(tags=["RAG"])


class RagQuestion(BaseModel):
    question: str


rag_service = RAGService()

@router.post("/rag",
             summary="rag api",
             response_description="Return HTTP Status Code 200 OK",
             status_code=status.HTTP_200_OK,
             )
async def rag(req: RagQuestion):
    response = rag_service.run(req.question)
    return {"response": response}
