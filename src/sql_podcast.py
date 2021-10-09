from sqlalchemy.sql import expression
from sqlite_database_creation import Podcast
from sqlalchemy import insert

from log import logging as log


table = 'podcasts'

class PodcastControls:
    def add_new_podcast(self, session, podcast):
        try:
            session.add(podcast)
            session.commit()
            return podcast
        except Exception as e:
            log.error(e)
        return None

    def get_first_podcast(self, session):
        try:
            result = session.query(Podcast).first()
            return result
        except Exception as e:
            log.error(e)
        return None

    def get_all_podcasts(self, session):
        try:
            result = session.query(Podcast).all()
            return result
        except Exception as e:
            log.error(e)
        return None

    def get_podcast_by_id(self, session, id):
        try:
            result =  session.query(Podcast).filter(Podcast.podcast_id == id).first()
            return result
        except Exception as e:
            log.error(e)
        return None

    def delete_podcast_id(self, session, id):
        try:
            result =  session.query(Podcast).filter(Podcast.podcast_id == id).delete()
            session.commit()
            return result
        except Exception as e:
            log.error(e)
        return None

    

    def get_all_podcasts_with_category(self, session):
        # this proabably goes in an utilty module
        pass
    
    def get_podcasts_with_downloads_available(self, session):
        # this proabably goes in an utilty module
        pass
    
    def update_podcast2(self, session):
        # this proabably goes in an utilty module
        pass
    


