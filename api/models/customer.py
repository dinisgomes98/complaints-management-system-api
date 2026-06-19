from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True ,nullable=False)
    phone = Column(String, nullable=False)

    complaints = relationship("Complaint", back_populates="customer")