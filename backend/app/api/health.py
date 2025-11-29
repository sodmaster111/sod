from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", summary="Health check")
def read_health() -> dict[str, str]:
    """Simple health endpoint for uptime checks."""
    return {"status": "ok"}
