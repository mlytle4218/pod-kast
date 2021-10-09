from sqlite_database_creation import create_database, Category
from sqlalchemy import insert, asc

from log import logging as log


table = 'categories'

class CategoryControls:
    def add_new_category(self, session, category):
        try:
            exists = session.query(Category).filter_by(title=str(category)).first()
            if not exists:
                session.add(category)
                session.commit()
                return category
            else:
                return None
        except Exception as e:
            log.error(e)
            return None

    def get_all_categories(self, session):
        try:
            return session.query(Category).order_by(asc(Category.title)).all()
        except Exception as e:
            log.error(e)
            return None

    def update_category(self, session, category):
        try:
            result = session.query(Category).filter(Category.category_id == category.category_id).update({"title":category.title})
            session.commit()
            return result
        except Exception as e:
            log.error(e)
            return None

    def remove_category(self, session, category):
        try:
            result = session.query(Category).filter(Category.category_id == category.category_id).delete()
            session.commit()
            return category
        except Exception as e:
            log.error('remove_category')
            log.error(e)
            return None
        # # result = session.query(Category).filter_by(title=str(title)).first()
        # if result:
        #     try:
        #         session.delete(result)
        #         session.commit()
        #         return True
        #     except Exception as e:
        #         log.error(e)
        #         return None
        # else:
        #     return None

