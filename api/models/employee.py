from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True ,nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)

    complaints = relationship("Complaint", back_populates="assigned_employee")
    role = relationship("Role", back_populates="employees")
