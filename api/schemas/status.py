from pydantic import BaseModel

class StatusResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True