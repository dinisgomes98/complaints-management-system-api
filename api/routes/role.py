from fastapi import APIRouter
from api.database import SessionLocal
from api.schemas.role import RoleResponse
from api.services.role import get_roles

role_router = APIRouter(
    prefix="/api/roles",
    tags=["Role"],
)

@role_router.get("/", response_model=list[RoleResponse])
def get_all_roles():
    db = SessionLocal()

    try:
        return get_roles(db)
    finally:
        db.close()