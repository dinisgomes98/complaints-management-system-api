from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.database import Base

class Priority(Base):
    __tablename__ = "priorities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    complaints = relationship("Complaint", back_populates="priority")