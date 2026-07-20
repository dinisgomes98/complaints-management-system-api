from fastapi import APIRouter
from api.database import SessionLocal
from api.schemas.priority import PriorityResponse
from api.services.priority import get_priorities

priority_router = APIRouter(
    prefix="/api/priorities",
    tags=["Priority"],
)

@priority_router.get("/", response_model=list[PriorityResponse])
def get_all_statuses():
    db = SessionLocal()

    try:
        return get_priorities(db)
    finally:
        db.close()