from logging import exception

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
        except Exception as e:
            log.error('add_new_episode')
            log.error(episode)
            log.error(e)
        return None

    def get_all_episodes(session):
        try:
            return session.query(Episode).all()
        except Exception as e:
            log.error('get_all_episodes')
            log.error(e)
        return None
    
    def get_episode_by_id(session, id):
        try:
            return session.query(Episode).filter(Episode.episode_id == id).first()
        except Exception as e:
            log.error('get_episode_by_id')
            log.error(id)
            log.error(e)
        return None

    def get_episodes_by_podcast_id(session, id):
        try:
            return session.query(Episode).filter(Episode.podcast_id == id).all()
        except Exception as e:
            log.error('get_episode_by_podcast_id')
            log.error(id)
            log.error(e)
        return None

    def update_episode_as_downloaded(session, episode):
        try:
            session.query(Episode).filter(Episode.episode_id == episode.episode_id).update({"downloaded":True})
            session.commit()
            return episode
        except Exception as e:
            log.error('update_episode_as_downloaded')
            log.error(episode)
            log.error(e)
        return None

    def get_episodes_with_downloads_available_by_podcast_id(session, id):
        try:
            return session.query(Episode).filter(
                Episode.podcast_id == id
                ).filter(
                    Episode.downloaded == False
                    ).filter(
                        Episode.veiwed == False
                        ).all()
        except Exception as e:
            log.error('get_episodes_with_downloads_available')
            log.error(e)
        return None

    def delete_episode(session, episode):
        try:
            session.query(Episode).filter(Episode.episode_id == episode.episode_id).delete()
            return episode
        except Exception as e:
            log.error('delete_episode')
            log.error(episode)
            log.error(e)
        return None
            
    def delete_episodes_by_podcast_id(session, podcast):
        try:
            return session.query(Episode).filter(Episode.podcast_id == podcast.podcast_id).delete()
        except Exception as e:
            log.error('delete_episodes_by_podcast_id')
            log.error(podcast)
            log.error(e)
        return None

    def get_number_of_available_episodes_by_podcast(session):
        #just returns the number - must be  better way
        pass

    def update_episodes_as_viewed(session, episodeArray):
        for episode in episodeArray:
            try:
                result = session.query(Episode).get(episode.episode_id)
                result.veiwed = 1
                session.commit()
            except Exception as e:
                log.error("update_episodes_as_viewed for {} failed".format(episode))
                log.error(e)

    def update_episodes_fix(session):
        # not sure this is needed
        pass

    def insert_episodes(session, episodeArry):
        try:
            return session.bulk_save_objects(episodeArry)
        except Exception as e:
            log.error('insert_episodes')
            log.error(e)
        return None


