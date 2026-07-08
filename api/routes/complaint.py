from fastapi import APIRouter
from api.database import SessionLocal
from api.schemas.complaint import ComplaintCreate, ComplaintResponse, ComplaintUpdate
from api.services.complaint import get_complaints, get_complaint, create_complaint, update_complaint, delete_complaint

complaint_router = APIRouter(prefix="/api/complaints", tags=["Complaint"])

@complaint_router.get("/", response_model=list[ComplaintResponse])
def all_complaint():
    
    db = SessionLocal()

    try:
        return get_complaints(db)
    
    finally:
        db.close()


@complaint_router.get("/{complaint_id}", response_model=ComplaintResponse)
def get_complaint_route(complaint_id: int):
    db = SessionLocal()

    try:
        return get_complaint(db, complaint_id)
    finally:
        db.close()

@complaint_router.post("/", response_model=ComplaintResponse)
def post_complaint(complaint: ComplaintCreate):
    
    db = SessionLocal()

    try:
        return create_complaint(db, complaint)

    finally:
        db.close()


@complaint_router.put("/{complaint_id}", response_model=ComplaintResponse)
def update_complaint_route(complaint_id: int, complaint: ComplaintUpdate):
    
    db = SessionLocal()

    try:
        return update_complaint(db, complaint_id, complaint)
    
    finally:
        db.close()


@complaint_router.delete("/{complaint_id}")
def delete_complaint_route(complaint_id: int):
    
    db = SessionLocal()
    
    try:
        return delete_complaint(db, complaint_id)

    finally:
        db.close()