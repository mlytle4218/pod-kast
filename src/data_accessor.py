# python imports
import os

# sqlalchemy imports
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

# local imports
import config
import sqlite_database_creation
import sql_category
import sql_episode
import sql_podcast

from log import logging as log

class DataAccessor:
    def __init__(self):
        data_base = "sqlite:///{}".format(config.home)
        self.engine = create_engine(data_base, echo=False)

        if os.path.isfile(config.home):
            self.engine.connect()
        else:
            sqlite_database_creation.create_database(config.home)

        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()
         
    def get_session(self):
        return self.session