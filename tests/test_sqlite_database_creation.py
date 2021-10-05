#! /usr/bin/env python3
from sqlite3.dbapi2 import Cursor
import config_test
import os
import sqlite3

#local imports
from sqlite_database_creation import create_database
from test_sql_category import TestSqlCategoryClass

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

class TestSqliteDatabaseCreationClass:
    conn=None
    cursor=None
    session=None
    @classmethod
    def setup_class(self):
        create_database('{}{}'.format(config_test.home,config_test.name))
        self.conn = sqlite3.connect('{}{}'.format(config_test.home,config_test.name))
        self.cursor = self.conn.cursor()
         
        # metadata = MetaData(self.conn)
    
        # Session = sessionmaker(bind=self.conn)
        # self.session = Session()

    @classmethod
    def teardown_class(self):
        if os.path.isfile('{}{}'.format(config_test.home,config_test.name)):
            os.remove('{}{}'.format(config_test.home,config_test.name))
            pass

    def test_create_database (self):
        results = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for result in results.fetchall():
            assert result in [('categories',),('episodes',),('podcasts',),]

    # def test_sql_catagory(self):
    #     TestSqlCategoryClass.add_category_test(connection=self.cursor)