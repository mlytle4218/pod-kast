#! /usr/bin/env python3
from sqlite3.dbapi2 import Cursor
import config_test
import os
import sqlite3


from sqlite_database_creation import create_database
class TestClass:
    @classmethod
    def setup_class(self):
        create_database('{}{}'.format(config_test.home,config_test.name))

    @classmethod
    def teardown_class(self):
        if os.path.isfile('{}{}'.format(config_test.home,config_test.name)):
            os.remove('{}{}'.format(config_test.home,config_test.name))
            pass

    def test_create_database (self):
        conn = sqlite3.connect('{}{}'.format(config_test.home,config_test.name))
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        results = cursor.fetchall()
        for result in results:
            assert result in [('categories',),('episodes',),('podcasts',),]
