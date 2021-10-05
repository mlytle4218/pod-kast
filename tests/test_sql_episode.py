import config_test
import os, datetime
import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, DateTime

#local imports
from sql_episode import DatabaseAccessor as da
from sqlite_database_creation import Episode, create_database
from log import logging as log

test1 = Episode(
    title = 'test1',
    published =   datetime.date(2021, 5, 1),
    summary='summary1',
    length=20,
    audio=True,
    podcast_id=1,
    href='http://whatever1.com'
)

test2 = Episode(
    title = 'test2',
    published = datetime.date(2021, 5, 2),
    summary='summary2',
    length=20,
    audio=True,
    podcast_id=1,
    href='http://whatever2.com'
)
test3 = Episode(
    title = 'test3',
    published =   datetime.date(2021, 5, 3),
    summary='summary3',
    length=20,
    audio=True,
    podcast_id=2,
    href='http://whatever3.com'
)

test4 = Episode(
    title = 'test4',
    published = datetime.date(2021, 5, 4),
    summary='summary4',
    length=20,
    audio=True,
    podcast_id=2,
    href='http://whatever4.com'
)




class TestSqlCategoryClass:
    @classmethod
    def setup_class(self):
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


    def test_add_new_episode(self):
        result = da.add_new_episode(self.session,test1)
        assert result.title == test1.title
        
        result = da.add_new_episode(self.session,test2)
        assert result.title == test2.title

        result = da.add_new_episode(self.session,test2)
        assert result.title == test2.title

        result = da.add_new_episode(self.session,test4)
        assert result.title == test4.title


    # def test_update_episode_as_downloaded(self):
    #     pass
    # def test_get_episodes_with_downloads_available(self, session):
    #     pass
    # def test_delete_episode(self, session, episode):
    #     try:
    #         session.query(Episode).filter(Episode.episode_id == episode.episode_id).delete()
    #         session.commit()
    #         return True
    #     except Exception as e:
    #         log.error('delete_episode')
    #         log.error(episode)
    #         log.error(str(e))
    #     return False

    # def test_delete_episodes_by_podcast_id(self, session):
    #     pass
    # def test_get_episodes_by_podcast_id(self, session):
    #     pass
    # def test_get_all_episodes(self, session):
    #     pass
    # def test_get_episode_by_id(self, session):
    #     pass
    # def test_get_number_of_available_episodes_bu_podcast(self, session):
    #     pass
    # def test_update_episodes_as_viewsed(self, session):
    #     pass
    # def test_update_episodes_fix(self, session):
    #     pass
    # def test_insert_single_episode(self, session):
    #     pass
    # def test_insert_episodes(self, session):
    #     pass

    # ## Tests when nothing in the database
    # def test_get_first_podcast_no_data(self):
    #     result = da.get_first_podcast(self.session)
    #     assert None == result

    # def test_get_all_podcasts_no_data(self):
    #     result = da.get_all_podcasts(self.session)
    #     assert result == []


    # def test_get_podcast_by_id_no_data(self):
    #     result = da.get_podcast_by_id(self.session, 2)
    #     assert result == None

    # def test_delete_podcast_no_data(self):
    #     result = da.get_podcast_by_id(self.session, 2)
    #     assert result == None

    # ## Tests with some data in the database
    # def test_insert_podcast(self):
    #     result = da.add_new_podcast(self.session,test1)
    #     assert result.name == test1.name

    #     result = da.add_new_podcast(self.session,test2)
    #     assert result.name == test2.name

    # def test_get_first_podcast(self):
    #     result = da.get_first_podcast(self.session)
    #     assert result.name == test1.name

    # def test_get_all_podcasts(self):
    #     result = da.get_all_podcasts(self.session)
    #     assert len(result) == 2

    # def test_get_podcast_by_id(self):
    #     result = da.get_podcast_by_id(self.session, 2)
    #     assert result.name == test2.name

    # def test_delete_podcast(self):
    #     result = da.get_podcast_by_id(self.session, 2)
    #     assert result.name == test2.name

