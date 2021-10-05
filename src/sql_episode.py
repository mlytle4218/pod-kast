from sqlite_database_creation import Episode
from sqlalchemy import insert

from log import logging as log


table = 'episodes'

class DatabaseAccessor:
    def add_new_episode(session, episode):
        try:
            session.add(episode)
            return episode
        except Exception as e:
            log.error('add_episode')
            log.error(episode)
            log.error(e)
        return None

    def get_all_episodes(session):
        pass
    
    def get_episode_by_id(session):
        pass
    
    

    def get_episodes_by_podcast_id(session):
        pass

    def update_episode_as_downloaded(session):
        pass
    def get_episodes_with_downloads_available(session):
        pass
    def delete_episode(session, episode):
        try:
            session.query(Episode).filter(Episode.episode_id == episode.episode_id).delete()
            return episode
        except Exception as e:
            log.error('delete_episode')
            log.error(episode)
            log.error(str(e))
        return None
            
    

    def delete_episodes_by_podcast_id(session):
        pass

    def get_number_of_available_episodes_bu_podcast(session):
        pass
    def update_episodes_as_viewsed(session):
        pass
    def update_episodes_fix(session):
        pass
    def insert_single_episode(session):
        pass
    def insert_episodes(session):
        pass


