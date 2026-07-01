from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.upload import router as upload_router

app = FastAPI(
    title="Enterprise Knowledge Assistant",
    version="1.0.0",
    description="AI-powered Enterprise Knowledge Assistant using RAG"
)

app.include_router(health_router)
app.include_router(upload_router)


@app.get("/")
def root():
    return {
        "message": "Enterprise Knowledge Assistant API",
        "status": "running"
    }