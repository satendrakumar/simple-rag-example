import uvicorn
from fastapi import FastAPI

from src.api.rag_router import router

app = FastAPI()

app.include_router(router, prefix="/v1/api")

uvicorn.run(app, host="0.0.0.0", port=8000)
