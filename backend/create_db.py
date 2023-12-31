from sqlalchemy.exc import IntegrityError
from models.init_db import DatabaseMusic

db = DatabaseMusic()


def create_tables():
    db.create_tables()
    return create_projects()


def create_projects():
    db.create_projects()
    db.close_session()


if __name__ == '__main__':
    try:
        create_tables()
        print("INFO: Database successfully created")
    except IntegrityError:
        print("INFO: Database already exists")
