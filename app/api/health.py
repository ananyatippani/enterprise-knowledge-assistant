from fastapi import APIRouter

# Create a router for health-related endpoints
router = APIRouter(
    prefix="",
    tags=["Health"]
)

@router.get("/health")
def health_check():
    """
    Health check endpoint to verify that the API is running.
    """
    return {
        "status": "healthy",
        "service": "Enterprise Knowledge Assistant",
        "version": "1.0.0"
    }