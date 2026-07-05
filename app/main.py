from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.upload import router as upload_router
from app.api.search import router as search_router

app = FastAPI(
    title="Enterprise Knowledge Assistant"
)

app.include_router(health_router)
app.include_router(upload_router)
app.include_router(search_router)


@app.get("/")
def root():
    return {"message": "Enterprise Knowledge Assistant API"}