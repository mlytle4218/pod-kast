from sqlite_database_creation import create_database, Category
from sqlalchemy import insert

from log import logging as log


table = 'categories'

class DatabaseAccessor:
    def add_new_category(session, category):
        exists = session.query(Category).filter_by(title=str(category)).first()
        if not exists:
            session.add(category)
            session.commit()
            return category
        else:
            return False

    def get_all_categories(session):
        return session.query(Category).all()

    def remove_category(session, title):
        result = session.query(Category).filter_by(title=str(title)).first()
        if result:
            try:
                session.delete(result)
                session.commit()
                return True
            except Exception as e:
                log.error(e)
                return False
        else:
            return False

