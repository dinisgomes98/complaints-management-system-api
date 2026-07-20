from api.models.role import Role

def get_roles(db):
    return db.query(Role).all()