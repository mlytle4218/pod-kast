import config_test
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#local imports
import utils



class TestSqlCategoryClass:
    @classmethod
    def setup_class(self):
        pass

    @classmethod
    def teardown_class(self):
        pass

    def test_special_character_check(self):
        result = utils.special_characters_check('#bob')
        assert result == True

        result = utils.special_characters_check('bob')
        assert result == False

