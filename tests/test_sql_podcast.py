import config_test
import os
import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#local imports
from sql_podcast import PodcastControls
from sqlite_database_creation import Podcast, create_database
from log import logging as log

test1 = Podcast(
    title='test1',
    url='http://whatever.com',
    audio='',
    video='',
    category=''
)

test2 = Podcast(
    title='test2',
    url='http://whatever.com',
    audio='',
    video='',
    category=''
)

class TestSqlCategoryClass:
    @classmethod
    def setup_class(self):
        self.podcastControls = PodcastControls()
        create_database('{}{}'.format(config_test.home,config_test.name))
        data_base = "sqlite:///{}".format('{}{}'.format(config_test.home,config_test.name))
        self.engine = create_engine(data_base)
        self.Base = declarative_base()
        self.Base.metadata.bind = self.engine
        self.Base.metadata.create_all(self.engine)
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

    @classmethod
    def teardown_class(self):
        if os.path.isfile('{}{}'.format(config_test.home,config_test.name)):
            os.remove('{}{}'.format(config_test.home,config_test.name))

    ## Tests when nothing in the database
    def test_get_first_podcast_no_data(self):
        result = self.podcastControls.get_first_podcast(self.session)
        assert None == result

    def test_get_all_podcasts_no_data(self):
        result = self.podcastControls.get_all_podcasts(self.session)
        assert result == []


    def test_get_podcast_by_id_no_data(self):
        result = self.podcastControls.get_podcast_by_id(self.session, 2)
        assert result == None

    def test_delete_podcast_no_data(self):
        result = self.podcastControls.get_podcast_by_id(self.session, 2)
        assert result == None

    ## Tests with some data in the database
    def test_insert_podcast(self):
        result = self.podcastControls.add_new_podcast(self.session,test1)
        assert result.title == test1.title

        result = self.podcastControls.add_new_podcast(self.session,test2)
        assert result.title == test2.title

    def test_get_first_podcast(self):
        result = self.podcastControls.get_first_podcast(self.session)
        assert result.title == test1.title

    def test_get_all_podcasts(self):
        result = self.podcastControls.get_all_podcasts(self.session)
        assert len(result) == 2

    def test_get_podcast_by_id(self):
        result = self.podcastControls.get_podcast_by_id(self.session, 2)
        assert result.title == test2.title

    def test_delete_podcast(self):
        result = self.podcastControls.get_podcast_by_id(self.session, 2)
        assert result.title == test2.title

