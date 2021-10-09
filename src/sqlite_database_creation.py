#! /usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime, time

from sqlalchemy.sql.sqltypes import Boolean


# local imports
import config
from log import logging as log


Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key = True)
    title = Column(String(250))

    def __str__(self):
        return self.title

    def __init__(self, title=''):
        self.title = title

class Podcast(Base):
    __tablename__ = 'podcasts'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    podcast_id = Column(Integer, primary_key = True)
    title = Column(String(250))
    url  = Column(String(250))
    audio = Column(String(250))
    video = Column(String(250))
    category = Column(String(250))

    def __str__(self):
        return self.title

    def __init__(self,title='',url='',audio='',video='',category=''):
        self.title = title
        self.url = url
        self.audio = audio
        self.video = video
        self.category = category

class Episode(Base):
    __tablename__ = 'episodes'
    # Here we define columns for the table episodes
    # Notice that each column is also a normal Python instance attribute.
    episode_id = Column(Integer, primary_key = True)
    title = Column(String(100))
    published  = Column(DateTime(250))
    summary = Column(String(500))
    length = Column(Integer)
    audio = Column(Boolean)
    href = Column(String(250))
    downloaded = Column(Boolean)
    podcast_id = Column(Integer, ForeignKey('podcasts.podcast_id'))
    podcast = relationship(Podcast)
    viewed = Column(Boolean)

    # def log(self,input):
    #     with open("test.txt", "a") as myfile:
    #         string=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    #         string=string+ ' - ' + str(input) + '\n'
    #         myfile.write(string)

    def __init__(self,title='', published='', summary='',length='',audio='',podcast_id='',href=''):
        self.title = title
        self.published = published
        self.summary = summary
        self.length = length
        self.audio = audio
        self.downloaded = False
        self.podcast_id = podcast_id
        self.href = href
        self.viewed = False
    
    def __str__(self):
        return self.title

    def __hash__(self):
        return hash((self.title, self.published))

    def __eq__(self,other):
        if not isinstance(other, Episode):
            return NotImplemented
        return self.title == other.title and self.published.replace(tzinfo=None) == other.published.replace(tzinfo=None)

    def __ne__(self,other):
        return self.title != other.title or self.published != other.published

def create_database(location):
    engine = create_engine('sqlite:///{}'.format(location))
    log.info(engine)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_database(config.home)
    log.info(config.home)
    pass