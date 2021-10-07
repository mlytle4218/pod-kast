from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


import config
import sql_category
import sql_episode
import sql_podcast

class DataAccessor:
    def __init__(self):
        session = self.connect_to_database()
        return session

    def connect_to_database(self):
        create_engine('{}{}'.format(config.home,config.name))
        data_base = "sqlite:///{}".format('{}{}'.format(config.home,config.name))
        self.engine = create_engine(data_base)

        self.Base = declarative_base()
        self.Base.metadata.bind = self.engine

        self.Base.metadata.create_all(self.engine)

        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()