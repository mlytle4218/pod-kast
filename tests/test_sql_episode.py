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
    published =   datetime.datetime(2021, 5, 10),
    summary='summary1',
    length=20,
    audio=True,
    podcast_id=1,
    href='http://whatever1.com'
)

test2 = Episode(
    title = 'test2',
    published = datetime.datetime(2020, 4, 9),
    summary='summary2',
    length=20,
    audio=True,
    podcast_id=1,
    href='http://whatever2.com'
)


#     episode_id = Column(Integer, primary_key = True)
#     title = Column(String(100))
#     published  = Column(DateTime(250))
#     summary = Column(String(500))
#     length = Column(Integer)
#     audio = Column(Integer)
#     href = Column(String(250))
#     downloaded = Column(Integer)
#     podcast_id = Column(Integer, ForeignKey('podcasts.podcast_id'))
#     podcast = relationship(Podcast)
#     veiwed = Column(Integer)

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
        log.info('test_add_new_episode')
        log.info(result)
        assert result.title == test1.title
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
            
    # def test_add_new_episode(self, session, episode):
    #     try:
    #         session.add(episode)
    #         session.commit()
    #         return True
    #     except Exception as e:
    #         log.error('add_episode')
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

