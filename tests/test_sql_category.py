import config_test
import os
import sqlite3

#local imports
from sql_category import DatabaseAccessor as da
from sqlite_database_creation import Category, create_database


class TestSqlCategoryClass:
    def add_category_test(session):
        category = Category(category="test1")
        result = da.add_new_category(session,category)
        print(result)
        assert False
        # assert True

