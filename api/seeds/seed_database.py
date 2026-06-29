from api.database import SessionLocal
import api.models

from api.models.status import Status
from api.models.priority import Priority
from api.models.role import Role

def seed_statuses(db):
    statuses = [
        "Open", 
        "In Progress", 
        "Waiting Customer", 
        "Resolved", 
        "Closed"
    ]

    for status in statuses:
        existing_status = db.query(Status).filter(Status.name == status).first()

        if existing_status is None:
           db.add(Status(name=status))

    db.commit()
    

def seed_priorities(db):
    priorities = [
        "Low", 
        "Medium", 
        "High", 
        "Critical"
    ]

    for priority in priorities:
        existing_priority = db.query(Priority).filter(Priority.name == priority).first()

        if existing_priority is None:
            db.add(Priority(name=priority))

    db.commit()


def seed_roles(db):
    roles = [
        "Admin", 
        "Manager", 
        "Employee"
    ]

    for role in roles:
        existing_role = db.query(Role).filter(Role.name == role).first()

        if existing_role is None:
            db.add(Role(name=role))
        
    db.commit()

def seed_database():

    db = SessionLocal()

    try:
        seed_statuses(db)
        seed_priorities(db)
        seed_roles(db)
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()