from api.models.priority import Priority

def get_priorities(db):
    return db.query(Priority).all()