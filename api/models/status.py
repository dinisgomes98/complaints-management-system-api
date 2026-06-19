from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.database import Base

class Status(Base):
    __tablename__ = "statuses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    complaints = relationship("Complaint", back_populates="status")