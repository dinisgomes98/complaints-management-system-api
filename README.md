# Complaints Management System API

A REST API built with FastAPI to manage customer complaints, corrective actions, workflows, and problem-solving processes.

This project simulates a real-world complaint management system inspired by industrial quality management and continuous improvement practices.

## Features

### Current

- PostgreSQL integration
- SQLAlchemy ORM
- Database relationships
- Environment variables with `.env`
- Seed database for lookup tables
- Modular project structure
- Pydantic request/response schemas

### Planned

- Full CRUD for complaints
- Customer management
- Employee management
- Problem solving management
- Complaint workflow
- Status and priority tracking
- Filtering and search
- Authentication & authorization
- Analytics endpoints
- Dashboard-ready statistics

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn
- python-dotenv

## Project Structure

```text
api/
├── models/
├── routes/
├── schemas/
├── services/
├── seeds/
└── database.py

src/
└── main.py
```

## Database

Current entities:

- Complaint
- Customer
- Employee
- Role
- Status
- Priority
- Problem Solving

Relationships are modelled using SQLAlchemy ORM with PostgreSQL.

## Purpose

This project was built to practice:

- Backend development
- Database design
- SQLAlchemy ORM
- PostgreSQL
- REST API architecture
- Entity relationships
- Data modelling
- Layered architecture
- Business workflow modelling
- Software engineering best practices

## Roadmap

- [x] Project setup
- [x] PostgreSQL configuration
- [x] SQLAlchemy models
- [x] Database creation
- [x] Pydantic schemas
- [x] Seed database
- [ ] CRUD Services
- [ ] API Routes
- [ ] Authentication & Authorization
- [ ] Analytics
- [ ] Testing
- [ ] Docker
- [ ] Deployment

## Getting Started

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
DATABASE_URL=postgresql://username:password@localhost/complaints_db
```

Run the API:

```bash
uvicorn src.main:app --reload
```

Populate lookup tables:

```bash
python -m api.seeds.seed_database
```

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```