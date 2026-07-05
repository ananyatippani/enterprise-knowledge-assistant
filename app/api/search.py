from fastapi import APIRouter

from app.models.request_models import SearchRequest
from app.models.response_models import SearchResponse
from app.services.rag_pipeline import ask_question
from app.utils.logger import logger

router = APIRouter(tags=["Search"])


@router.post(
    "/search",
    response_model=SearchResponse
)
def semantic_search(request: SearchRequest):
    """
    Perform semantic search using the RAG pipeline.
    """

    logger.info(f"Received search query: {request.query}")

    response = ask_question(request.query)

    logger.info("Successfully generated response.")

    return response