from fastapi import APIRouter
from api.database import SessionLocal
from api.schemas.customer import CustomerCreate, CustomerResponse, CustomerUpdate
from api.services.customer import get_customers, get_customer, create_customer, update_customer, delete_customer

customer_router = APIRouter(prefix="/api/customers", tags=["Customer"])

@customer_router.get("/", response_model=list[CustomerResponse])
def all_customers():
    
    db = SessionLocal()

    try:
        return get_customers(db)
    
    finally:
        db.close()


@customer_router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer_route(customer_id: int):
    db = SessionLocal()

    try:
        return get_customer(db, customer_id)
    finally:
        db.close()

@customer_router.post("/", response_model=CustomerResponse)
def post_customer(customer: CustomerCreate):
    
    db = SessionLocal()

    try:
        return create_customer(db, customer)

    finally:
        db.close()


@customer_router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer_route(customer_id: int, customer: CustomerUpdate):
    
    db = SessionLocal()

    try:
        return update_customer(db, customer_id, customer)
    
    finally:
        db.close()


@customer_router.delete("/{customer_id}")
def delete_customer_route(customer_id: int):
    
    db = SessionLocal()
    
    try:
        return delete_customer(db, customer_id)

    finally:
        db.close()