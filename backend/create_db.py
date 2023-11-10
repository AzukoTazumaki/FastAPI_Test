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
        print("\033[32m{}".format('INFO: Database successfully created (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧'))
    except IntegrityError:
        print("\033[31m{}".format('INFO: Database already exists ¯\_(ツ)_/¯'))
