from fastapi import APIRouter

from api.database import SessionLocal
from api.schemas.problem_solving import (
    ProblemSolvingCreate,
    ProblemSolvingResponse,
    ProblemSolvingUpdate,
)
from api.services.problem_solving import (
    create_problem_solving,
    delete_problem_solving,
    get_problem_solving,
    get_problem_solvings,
    update_problem_solving,
)


problem_solving_router = APIRouter(
    prefix="/api/problem-solvings",
    tags=["Problem Solving"],
)


@problem_solving_router.get(
    "/",
    response_model=list[ProblemSolvingResponse],
)
def get_all_problem_solvings():
    db = SessionLocal()

    try:
        return get_problem_solvings(db)
    finally:
        db.close()


@problem_solving_router.get(
    "/{problem_solving_id}",
    response_model=ProblemSolvingResponse,
)
def get_problem_solving_route(problem_solving_id: int):
    db = SessionLocal()

    try:
        return get_problem_solving(db, problem_solving_id)
    finally:
        db.close()


@problem_solving_router.post(
    "/",
    response_model=ProblemSolvingResponse,
    status_code=201,
)
def create_problem_solving_route(
    problem_solving: ProblemSolvingCreate,
):
    db = SessionLocal()

    try:
        return create_problem_solving(db, problem_solving)
    finally:
        db.close()


@problem_solving_router.put(
    "/{problem_solving_id}",
    response_model=ProblemSolvingResponse,
)
def update_problem_solving_route(
    problem_solving_id: int,
    problem_solving: ProblemSolvingUpdate,
):
    db = SessionLocal()

    try:
        return update_problem_solving(
            db,
            problem_solving_id,
            problem_solving,
        )
    finally:
        db.close()


@problem_solving_router.delete("/{problem_solving_id}")
def delete_problem_solving_route(problem_solving_id: int):
    db = SessionLocal()

    try:
        return delete_problem_solving(db, problem_solving_id)
    finally:
        db.close()