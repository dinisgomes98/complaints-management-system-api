from fastapi import FastAPI

from api.database import Base, engine
import api.models

import api.routes

app = FastAPI(
    title="Complaints Management System API",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(api.routes.customer_router)
app.include_router(api.routes.employee_router)


@app.get("/")
def index():
    return {
        "status": "complaints management system api is running"
    }