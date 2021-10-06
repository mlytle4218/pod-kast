from logging import exception
from sqlalchemy.sql import expression

from sqlalchemy.sql.expression import false
from sqlite_database_creation import Episode
from sqlalchemy import insert

from log import logging as log


table = 'episodes'

class DatabaseAccessor:
    def add_new_episode(session, episode):
        try:
            session.add(episode)
            return episode
        except AttributeError as e:
            pass
        except Exception as e:
            log.error('add_new_episode')
            log.error(episode)
            log.error(e)
        return None

    def get_all_episodes(session):
        try:
            return session.query(Episode).all()
        except AttributeError as e:
            pass
        except Exception as e:
            log.error('get_all_episodes')
            log.error(e)
        return None
    
    def get_episode_by_id(session, id):
        try:
            return session.query(Episode).filter(Episode.episode_id == id).first()
        except AttributeError as e:
            pass
        except Exception as e:
            log.error('get_episode_by_id')
            log.error(id)
            log.error(e)
        return None

    def get_episodes_by_podcast_id(session, id):
        try:
            return session.query(Episode).filter(Episode.podcast_id == id).all()
        except AttributeError as e:
            pass
        except Exception as e:
            log.error('get_episode_by_podcast_id')
            log.error(id)
            log.error(e)
        return None

    def get_episodes_with_downloads_available_by_podcast_id(session, id):
        try:
            return session.query(Episode).filter(
                Episode.podcast_id == id
                ).filter(
                    Episode.downloaded == False
                    ).filter(
                        Episode.viewed == False
                        ).all()
        except AttributeError as e:
            pass
        except Exception as e:
            log.error('get_episodes_with_downloads_available')
            log.error(e)
        return None

    def update_episode_as_downloaded(session, episode):
        try:
            result = session.query(Episode).filter(Episode.episode_id == episode.episode_id).update({"downloaded":True})
            # result.downloaded = True
            session.commit()
            return episode
        except Exception as e:
            log.error('update_episode_as_downloaded')
            log.error(episode)
            log.error(e)
        return None

    def update_episode_as_viewed(session, episode):
        try:
            # log.info(session)
            session.query(Episode).filter(Episode.episode_id == episode.episode_id).update({"viewed":True})
            # session.commit()
            return episode
        except AttributeError as e:
            pass
        except Exception as e:
            log.error("update_episodes_as_viewed for {} failed".format(episode))
            log.error(e)
        return None

    def delete_episode(session, episode):
        try:
            session.query(Episode).filter(Episode.episode_id == episode.episode_id).delete()
            session.commit()
            return episode
        except Exception as e:
            log.error('delete_episode')
            log.error(episode)
            log.error(e)
        return None
            
    def delete_episodes_by_podcast_id(session, id):
        try:
            result  = session.query(Episode).filter(Episode.podcast_id == id).delete(synchronize_session=False)
            session.commit()
            return result
        except Exception as e:
            log.error('delete_episodes_by_podcast_id')
            log.error(id)
            log.error(e)
        return None

    def insert_episodes(session, episode_array):
        try:
            # for episode in episode_array:
            #     result = session.add(episode)
            session.bulk_save_objects(episode_array,return_defaults = True)
            session.commit()
            return episode_array
        except Exception as e:
            log.error('insert_episodes')
            log.error(e)
        return None

    def get_number_of_available_episodes_by_podcast(session):
        #just returns the number - must be  better way
        # is used to show the number on the screen
        pass

    def update_episodes_fix(session):
        # not sure this is needed
        pass


