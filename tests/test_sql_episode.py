from logging import FATAL
from sqlalchemy.sql.expression import false
import config_test
import os, datetime
import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, DateTime

#local imports
from sql_episode import EpisodeControls
from sqlite_database_creation import Episode, create_database
from log import logging as log

test1 = Episode(
    title = 'test1',
    published = datetime.date(2021, 5, 1),
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
    published = datetime.date(2021, 5, 3),
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
        self.episodeControls = EpisodeControls()
        create_database('{}{}'.format(config_test.home,config_test.name))
        data_base = "sqlite:///{}".format('{}{}'.format(config_test.home,config_test.name))
        self.engine = create_engine(data_base)
        self.Base = declarative_base()
        self.Base.metadata.bind = self.engine
        self.Base.metadata.create_all(self.engine)
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()
        self.mock = {}

        self.episodes = []

        for i in range(8):
            id = None
            if i < 4 :
                id = 1
            else:
                id = 2

            test = Episode(
                title = 'test{}'.format(i),
                published = datetime.date(2021, 5, i+1),
                summary='summary{}'.format(i),
                length=20,
                audio=True,
                podcast_id=1,
                href='http://whatever{}.com'.format(i)
            )
            self.episodes.append(test)

    @classmethod
    def teardown_class(self):
        if os.path.isfile('{}{}'.format(config_test.home,config_test.name)):
            os.remove('{}{}'.format(config_test.home,config_test.name))


    def test_add_new_episode(self):
        result = self.episodeControls.add_new_episode(self.session,test1)
        assert result.title == test1.title
        
        result = self.episodeControls.add_new_episode(self.session,test2)
        assert result.title == test2.title

        result = self.episodeControls.add_new_episode(self.session,test3)
        assert result.title == test3.title

        result = self.episodeControls.add_new_episode(self.session,test4)
        assert result.title == test4.title

        result = self.episodeControls.add_new_episode(self.mock,test1)
        assert result == None

    def test_get_all_episodes(self):
        result = self.episodeControls.get_all_episodes(self.session)
        assert len(result) == 4

        result = self.episodeControls.get_all_episodes(self.mock)
        assert result == None

    def test_get_episode_by_id(self):
        result = self.episodeControls.get_episode_by_id(self.session, 1)
        assert result.title == test1.title

        result = self.episodeControls.get_episode_by_id(self.mock, 1)
        assert result == None

    def test_get_episodes_by_podcast_id(self):
        result = self.episodeControls.get_episodes_by_podcast_id(self.session, 1)
        assert len(result) == 2

        result = self.episodeControls.get_episodes_by_podcast_id(self.mock, 1)
        assert result == None

    def test_get_episodes_with_downloads_available_by_podcast_id(self):
        result = self.episodeControls.get_episodes_with_downloads_available_by_podcast_id(self.session, 1)
        assert len(result) == 2

        result = self.episodeControls.get_episodes_with_downloads_available_by_podcast_id(self.mock, 1)
        assert result == None


    def test_update_episode_as_downloaded(self):
        assert  test1.downloaded == False
        result = self.episodeControls.update_episode_as_downloaded(self.session, test1)

        episode = self.episodeControls.get_episode_by_id(self.session, result.episode_id)
        assert episode.downloaded == True

        result = self.episodeControls.update_episode_as_downloaded(self.mock, test1)
        assert result== None
        
    def test_update_episodes_as_viewed(self):
        episode = self.episodeControls.get_episode_by_id(self.session, 1)
        assert episode.viewed == False
        result = self.episodeControls.update_episode_as_viewed(self.session, episode)
        assert result.viewed == True

        result = self.episodeControls.update_episode_as_viewed(self.mock, test1)
        assert result== None


    def test_delete_episode(self):
        num_episodes = self.episodeControls.get_all_episodes(self.session)
        assert len(num_episodes) == 4

        result = self.episodeControls.delete_episode(self.session, test3)
        assert result.title == test3.title

        episode = self.episodeControls.get_episode_by_id(self.session, result.episode_id)
        assert episode == None

        num_episodes = self.episodeControls.get_all_episodes(self.session)
        assert len(num_episodes) == 3

        result = self.episodeControls.delete_episode(self.session, test4)
        assert result.title == test4.title

        num_episodes = self.episodeControls.get_all_episodes(self.session)
        assert len(num_episodes) == 2



    def test_delete_episodes_by_podcast_id(self):
        numEpisodes = self.episodeControls.get_all_episodes(self.session)
        assert len(numEpisodes) == 2

        result = self.episodeControls.delete_episodes_by_podcast_id(self.session, 1)
        assert result == 2

        numEpisodes = self.episodeControls.get_all_episodes(self.session)
        assert len(numEpisodes) == 0
    
    def test_insert_episodes(self):
        episode_array = []
        episode_array.append(test1)
        episode_array.append(test2)
        episode_array.append(test3)
        episode_array.append(test4)

        numEpisodes = self.episodeControls.get_all_episodes(self.session)
        assert len(numEpisodes) == 0

        result = self.episodeControls.insert_episodes(self.session, self.episodes)
        assert len(result) == len(self.episodes)

        numEpisodes = self.episodeControls.get_all_episodes(self.session)
        assert len(numEpisodes) == len(self.episodes)
        

    # def test_get_number_of_available_episodes_bu_podcast(self, session):
    #     pass

    # def test_update_episodes_fix(self, session):
    #     pass
    # def test_insert_single_episode(self, session):
    #     pass
    # def test_insert_episodes(self, session):
    #     pass

    
