from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from api.database import Base
from datetime import datetime, UTC

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    closed_at = Column(DateTime)
    status_id = Column(Integer, ForeignKey("statuses.id"), nullable=False)
    priority_id = Column(Integer, ForeignKey("priorities.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    assigned_employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    problem_solving_id = Column(Integer, ForeignKey("problem_solvings.id"), nullable=True)

    status = relationship("Status", back_populates="complaints")
    priority = relationship("Priority", back_populates="complaints")
    customer = relationship("Customer", back_populates="complaints")
    assigned_employee = relationship("Employee", back_populates="complaints")
    problem_solving = relationship("Problem_Solving", back_populates="complaints")
