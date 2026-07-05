from fastapi import APIRouter

from app.services.embeddings import create_embeddings
from app.services.vector_store import search

router = APIRouter(tags=["Search"])


@router.get("/search")
def semantic_search(query: str):

    query_embedding = create_embeddings([query])[0]

    results = search(query_embedding)

    return results