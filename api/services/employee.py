from fastapi import HTTPException
from api.models.employee import Employee

def get_employees(db):
    return db.query(Employee).all()


def get_employee(db, employee_id):
    employee = (db.query(Employee).filter(Employee.id == employee_id).first())

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


def create_employee(db, employee):

    existing_employee = db.query(Employee).filter(Employee.email == employee.email).first()
    
    if existing_employee is not None:
        raise HTTPException(
            status_code=409,
            detail="Employee already exists"
        )
        
   
    new_employee = Employee(
        name = employee.name,
        email = employee.email,
        role_id = employee.role_id
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


def update_employee(db, employee_id, employee):
    existing_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    
    if existing_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    if employee.name is not None:
        existing_employee.name = employee.name


    if employee.email is not None:
        
        valid_email = db.query(Employee).filter(Employee.email == employee.email, Employee.id != employee_id).first()
        
        if valid_email is not None:
            raise HTTPException(status_code=409, detail="Email already exists")

        
        existing_employee.email = employee.email


    if employee.role_id is not None:
        existing_employee.role_id = employee.role_id

    db.commit()
    db.refresh(existing_employee)

    return existing_employee


def delete_employee(db, employee_id):
    existing_employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if existing_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    

    db.delete(existing_employee)
    db.commit()

    return {"message": "Employee deleted successfully"}
