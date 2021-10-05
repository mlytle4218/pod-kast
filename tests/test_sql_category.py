import config_test
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#local imports
from sql_category import DatabaseAccessor as da
from sqlite_database_creation import Category, create_database
from log import logging as log

test1 = 'test1'
test2 = 'test2'


class TestSqlCategoryClass:
    @classmethod
    def setup_class(self):
        create_database('{}{}'.format(config_test.home,config_test.name))
        data_base = "sqlite:///{}".format('{}{}'.format(config_test.home,config_test.name))
        self.engine = create_engine(data_base)

        self.Base = declarative_base()
        # Bind the engine to the metadata of the Base class so that the
        # declaratives can be accessed through a DBSession instance
        self.Base.metadata.bind = self.engine

        self.Base.metadata.create_all(self.engine)

        self.DBSession = sessionmaker(bind=self.engine)
        # A DBSession() instance establishes all conversations with the database
        # and represents a "staging zone" for all the objects loaded into the
        # database session object. Any change made against the objects in the
        # session won't be persisted into the database until you call
        # session.commit(). If you're not happy about the changes, you can
        # revert all of them back to the last commit by calling
        # session.rollback()
        self.session = self.DBSession()

    @classmethod
    def teardown_class(self):
        if os.path.isfile('{}{}'.format(config_test.home,config_test.name)):
            os.remove('{}{}'.format(config_test.home,config_test.name))




    def test_add_category(self):
        name  = test1
        category = Category(title=name)
        result = da.add_new_category(self.session,category)
        print(str(result))
        assert name == str(result)

        result = da.add_new_category(self.session,category)
        assert False == result

        name  = test2
        category = Category(title=name)
        result = da.add_new_category(self.session,category)
        print(str(result))
        assert name == str(result)

        result = da.get_all_categories(self.session)
        assert len(result) == 2

    def test_remove_category(self):
        result = da.remove_category(self.session,title=str(test1))
        assert result == True
        
        result = da.remove_category(self.session,title=str(test1))
        assert result == False
        
