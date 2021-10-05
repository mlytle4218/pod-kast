from sqlalchemy.sql import expression
from sqlite_database_creation import Podcast
from sqlalchemy import insert

from log import logging as log


table = 'podcasts'

class DatabaseAccessor:
    def add_new_podcast(session, podcast):
        try:
            session.add(podcast)
            return podcast
        except Exception as e:
            log.error(e)
        return None

    def get_first_podcast(session):
        try:
            result = session.query(Podcast).first()
            return result
        except Exception as e:
            log.error(e)
        return None

    def get_all_podcasts(session):
        try:
            result = session.query(Podcast).all()
            return result
        except Exception as e:
            log.error(e)
        return None

    def get_podcast_by_id(session, id):
        try:
            result =  session.query(Podcast).filter(Podcast.podcast_id == id).first()
            return result
        except Exception as e:
            log.error(e)
        return None

    def delete_podcast_id(session, id):
        try:
            result =  session.query(Podcast).filter(Podcast.podcast_id == id).delete()
            return result
        except Exception as e:
            log.error(e)
        return None

    

    def get_all_podcasts_with_category(session):
        # this proabably goes in an utilty module
        pass
    
    def get_podcasts_with_downloads_available(session):
        # this proabably goes in an utilty module
        pass
    
    def update_podcast2(session):
        # this proabably goes in an utilty module
        pass
    


