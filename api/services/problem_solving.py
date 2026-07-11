from datetime import UTC, datetime

from fastapi import HTTPException

from api.models.employee import Employee
from api.models.problem_solving import Problem_Solving


def get_problem_solvings(db):
    return db.query(Problem_Solving).all()


def get_problem_solving(db, problem_solving_id):
    problem_solving = (
        db.query(Problem_Solving)
        .filter(Problem_Solving.id == problem_solving_id)
        .first()
    )

    if problem_solving is None:
        raise HTTPException(
            status_code=404,
            detail="Problem solving not found",
        )

    return problem_solving


def create_problem_solving(db, problem_solving):
    new_problem_solving = Problem_Solving(
        title=problem_solving.title,
        containment_action=problem_solving.containment_action,
        root_cause=problem_solving.root_cause,
        corrective_action=problem_solving.corrective_action,
        preventive_action=problem_solving.preventive_action,
        approved=False,
        approved_by_id=None,
        approved_at=None,
    )

    db.add(new_problem_solving)
    db.commit()
    db.refresh(new_problem_solving)

    return new_problem_solving


def update_problem_solving(db, problem_solving_id, problem_solving):
    existing_problem_solving = (
        db.query(Problem_Solving)
        .filter(Problem_Solving.id == problem_solving_id)
        .first()
    )

    if existing_problem_solving is None:
        raise HTTPException(
            status_code=404,
            detail="Problem solving not found",
        )

    if problem_solving.title is not None:
        existing_problem_solving.title = problem_solving.title

    if problem_solving.containment_action is not None:
        existing_problem_solving.containment_action = (
            problem_solving.containment_action
        )

    if problem_solving.root_cause is not None:
        existing_problem_solving.root_cause = problem_solving.root_cause

    if problem_solving.corrective_action is not None:
        existing_problem_solving.corrective_action = (
            problem_solving.corrective_action
        )

    if problem_solving.preventive_action is not None:
        existing_problem_solving.preventive_action = (
            problem_solving.preventive_action
        )

    if problem_solving.approved is not None:
        if problem_solving.approved is True:
            if problem_solving.approved_by_id is None:
                raise HTTPException(
                    status_code=422,
                    detail="approved_by_id is required to approve a problem solving",
                )

            approver = (
                db.query(Employee)
                .filter(Employee.id == problem_solving.approved_by_id)
                .first()
            )

            if approver is None:
                raise HTTPException(
                    status_code=404,
                    detail="Approving employee not found",
                )

            existing_problem_solving.approved = True
            existing_problem_solving.approved_by_id = (
                problem_solving.approved_by_id
            )
            existing_problem_solving.approved_at = datetime.now(UTC)

        else:
            existing_problem_solving.approved = False
            existing_problem_solving.approved_by_id = None
            existing_problem_solving.approved_at = None

    db.commit()
    db.refresh(existing_problem_solving)

    return existing_problem_solving


def delete_problem_solving(db, problem_solving_id):
    existing_problem_solving = (
        db.query(Problem_Solving)
        .filter(Problem_Solving.id == problem_solving_id)
        .first()
    )

    if existing_problem_solving is None:
        raise HTTPException(
            status_code=404,
            detail="Problem solving not found",
        )

    if existing_problem_solving.complaints:
        raise HTTPException(
            status_code=409,
            detail="Problem solving is associated with one or more complaints",
        )

    db.delete(existing_problem_solving)
    db.commit()

    return {"message": "Problem solving deleted successfully"}