from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, BigInteger
from sqlalchemy.orm import relationship
from database import Base

class Story(Base):
    __tablename__='story'
    story_id = Column(Integer,primary_key=True)
    story_title = Column(String(40))
    story_url = Column(String(40))
    story_author = Column(String(40))
    story_credit = Column(String(100))

class Story_Content(Base):
     __tablename__ = 'story_content'
     story_content_id = Column(Integer,primary_key=True)
     story_id = Column(Integer)
     content = Column(String(1000))

