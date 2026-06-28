from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from api.database import Base

class Problem_Solving(Base):
    __tablename__ = "problem_solvings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    containment_action = Column(String, nullable=True)
    root_cause = Column(String, nullable=True)
    corrective_action = Column(String, nullable=True)
    preventive_action = Column(String, nullable=True)
    approved = Column(Boolean, nullable=True)
    approved_by_id = Column(Integer, ForeignKey("employees.id"), nullable=True)
    approved_at = Column(Date, nullable=True)

    approver = relationship("Employee", back_populates="approved_problem_solvings")
    complaints = relationship("Complaint", back_populates="problem_solving")




