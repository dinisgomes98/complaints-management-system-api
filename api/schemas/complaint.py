from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ComplaintResponse(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    closed_at: Optional[datetime] = None
    status_id: int
    priority_id: int
    customer_id: int
    assigned_employee_id: int
    problem_solving_id: Optional[int] = None

    class Config:
        from_attributes = True

class ComplaintCreate(BaseModel):
    title: str
    description: str
    status_id: int = Field(..., ge=1, le=5)
    priority_id: int = Field(..., ge=1, le=4)
    customer_id: int
    assigned_employee_id: int
    problem_solving_id: Optional[int] = None

class ComplaintUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    closed_at: Optional[datetime] = None
    status_id: Optional[int] = Field(None, ge=1, le=5)
    priority_id: Optional[int] = Field(None, ge=1, le=4)
    customer_id: Optional[int] = None
    assigned_employee_id: Optional[int] = None
    problem_solving_id: Optional[int] = None
    