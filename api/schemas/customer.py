from pydantic import BaseModel, Field
from typing import Optional
from pydantic import EmailStr

class CustomerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str

    class Config:
        from_attributes = True

class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    