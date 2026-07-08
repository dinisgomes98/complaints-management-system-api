from fastapi import HTTPException
from api.models.complaint import Complaint


def get_complaints(db):
    return db.query(Complaint).all()


def get_complaint(db, complaint_id):
    complaint = db.query(Complaint).filter(Complaint.id == complaint_id).first()

    if complaint is None:
        raise HTTPException(status_code=404, detail="Complaint not found")

    return complaint


def create_complaint(db, complaint):
    new_complaint = Complaint(
        title=complaint.title,
        description=complaint.description,
        status_id=complaint.status_id,
        priority_id=complaint.priority_id,
        customer_id=complaint.customer_id,
        assigned_employee_id=complaint.assigned_employee_id,
        problem_solving_id=complaint.problem_solving_id
    )

    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)

    return new_complaint


def update_complaint(db, complaint_id, complaint):
    existing_complaint = db.query(Complaint).filter(Complaint.id == complaint_id).first()

    if existing_complaint is None:
        raise HTTPException(status_code=404, detail="Complaint not found")

    if complaint.title is not None:
        existing_complaint.title = complaint.title

    if complaint.description is not None:
        existing_complaint.description = complaint.description

    if complaint.closed_at is not None:
        existing_complaint.closed_at = complaint.closed_at

    if complaint.status_id is not None:
        existing_complaint.status_id = complaint.status_id

    if complaint.priority_id is not None:
        existing_complaint.priority_id = complaint.priority_id

    if complaint.customer_id is not None:
        existing_complaint.customer_id = complaint.customer_id

    if complaint.assigned_employee_id is not None:
        existing_complaint.assigned_employee_id = complaint.assigned_employee_id

    if complaint.problem_solving_id is not None:
        existing_complaint.problem_solving_id = complaint.problem_solving_id

    db.commit()
    db.refresh(existing_complaint)

    return existing_complaint


def delete_complaint(db, complaint_id):
    existing_complaint = db.query(Complaint).filter(Complaint.id == complaint_id).first()

    if existing_complaint is None:
        raise HTTPException(status_code=404, detail="Complaint not found")

    db.delete(existing_complaint)
    db.commit()

    return {"message": "Complaint deleted successfully"}