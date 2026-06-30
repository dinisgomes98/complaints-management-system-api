from fastapi import HTTPException
from api.models.customer import Customer

def get_customers(db):
    return db.query(Customer).all()


def get_customer(db, customer_id):
    customer = (db.query(Customer).filter(Customer.id == customer_id).first())

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


def create_customer(db, customer):

    existing_customer = db.query(Customer).filter(Customer.email == customer.email).first()
    
    if existing_customer is not None:
        raise HTTPException(
            status_code=409,
            detail="Customer already exists"
        )
        
   
    new_customer = Customer(
        name = customer.name,
        email = customer.email,
        phone = customer.phone
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


def update_customer(db, customer_id, customer):
    existing_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    
    if existing_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    if customer.name is not None:
        existing_customer.name = customer.name


    if customer.email is not None:
        
        valid_email = db.query(Customer).filter(Customer.email == customer.email, Customer.id != customer.id).first()
        
        if valid_email is not None:
            raise HTTPException(status_code=409, detail="Email already exists")

        
        existing_customer.email = customer.email


    if customer.phone is not None:
        existing_customer.phone = customer.phone

    db.commit()
    db.refresh(existing_customer)

    return existing_customer


def delete_customer(db, customer_id):
    existing_customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if existing_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    

    db.delete(existing_customer)
    db.commit()

    return {"message": "Customer deleted successfully"}
