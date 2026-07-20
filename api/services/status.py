from api.models.status import Status

def get_statuses(db):
    return db.query(Status).all()