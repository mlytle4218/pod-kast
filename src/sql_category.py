from sqlite_database_creation import Category


class DatabaseAccessor:
    def add_new_category_old(self, category):
        existing_cat = self.session.query(Category).filter(
            Category.category == category.category).all()
        if (len(existing_cat)) == 0:
            try:
                self.session.add(category)
                self.session.commit()
                return True
            except Exception:
                return False
        # this is not good - find a better way
        return True 

    def add_new_category(session, category):
        result = session.add(category)
        print(result)
        return result
        # return session.add(category)

        # existing_cat = self.session.query(Category).filter(
        #     Category.category == category.category).all()
        # if (len(existing_cat)) == 0:
        #     try:
        #         self.session.add(category)
        #         self.session.commit()
        #         return True
        #     except Exception:
        #         return False
        # # this is not good - find a better way
        # return True 

    def get_all_categories(self):
        return self.session.query(Category).all()

    def get_all_categories_old(self):
        categories = self.session.query(Category).all()
        return categories


    # def get_or_create(session, model, **kwargs):
    #     instance = session.query(model).filter_by(**kwargs).first()
    # if instance:
    #     return instance
    # else:
    #     instance = model(**kwargs)
    #     session.add(instance)
    #     session.commit()
    #     return instance

if __name__ == "__main__":
    pass