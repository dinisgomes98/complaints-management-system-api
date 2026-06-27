from pydantic import BaseModel

class PriorityResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True