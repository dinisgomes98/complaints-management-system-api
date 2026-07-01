from fastapi import APIRouter
from api.database import SessionLocal
from api.schemas.employee import EmployeeCreate, EmployeeResponse, EmployeeUpdate
from api.services.employee import get_employees, get_employee, create_employee, update_employee, delete_employee

employee_router = APIRouter(prefix="/api/employees", tags=["Employee"])

@employee_router.get("/", response_model=list[EmployeeResponse])
def all_employees():
    
    db = SessionLocal()

    try:
        return get_employees(db)
    
    finally:
        db.close()


@employee_router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee_route(employee_id: int):
    db = SessionLocal()

    try:
        return get_employee(db, employee_id)
    finally:
        db.close()

@employee_router.post("/", response_model=EmployeeResponse)
def post_employee(employee: EmployeeCreate):
    
    db = SessionLocal()

    try:
        return create_employee(db, employee)

    finally:
        db.close()


@employee_router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee_route(employee_id: int, employee: EmployeeUpdate):
    
    db = SessionLocal()

    try:
        return update_employee(db, employee_id, employee)
    
    finally:
        db.close()


@employee_router.delete("/{employee_id}")
def delete_employee_route(employee_id: int):
    
    db = SessionLocal()
    
    try:
        return delete_employee(db, employee_id)

    finally:
        db.close()