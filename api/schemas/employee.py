from pydantic import BaseModel, Field
from typing import Optional
from pydantic import EmailStr

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role_id: int = Field(..., ge=1)

    class Config:
        from_attributes = True

class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    role_id: int

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role_id: Optional[int] = Field(..., ge=1)
    