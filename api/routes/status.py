from fastapi import APIRouter
from api.database import SessionLocal
from api.schemas.status import StatusResponse
from api.services.status import get_statuses

status_router = APIRouter(
    prefix="/api/statuses",
    tags=["Status"],
)

@status_router.get("/", response_model=list[StatusResponse])
def get_all_statuses():
    db = SessionLocal()

    try:
        return get_statuses(db)
    finally:
        db.close()