from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProblemSolvingResponse(BaseModel):
    id: int
    title: str
    containment_action: Optional[str] = None
    root_cause: Optional[str] = None
    corrective_action: Optional[str] = None
    preventive_action: Optional[str] = None
    approved: Optional[bool] = None
    approved_by_id: Optional[int] = None
    approved_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class ProblemSolvingCreate(BaseModel):
    title: str
    containment_action: Optional[str] = None
    root_cause: Optional[str] = None
    corrective_action: Optional[str] = None
    preventive_action: Optional[str] = None
    

class ProblemSolvingUpdate(BaseModel):
    title: Optional[str] = None
    containment_action: Optional[str] = None
    root_cause: Optional[str] = None
    corrective_action: Optional[str] = None
    preventive_action: Optional[str] = None
    approved: Optional[bool] = None
    approved_by_id: Optional[int] = None
    approved_at: Optional[datetime] = None
    