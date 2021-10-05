from sqlite_database_creation import create_database, Category
from sqlalchemy import insert


table = 'categories'

class DatabaseAccessor:
    def add_new_category(session, category):
        session.add(category)
        session.commit()
        return category

    def get_all_categories(session):
        return session.query(Category).all()
