from fastapi import FastAPI
from api.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def index():
    return {"status": "complaint management system api is running"}