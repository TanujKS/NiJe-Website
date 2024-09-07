from pydantic import BaseModel
import sys
from os.path import dirname, join, abspath

class Story(BaseModel):
    story_id: int
    story_title: str
    story_url: str
    story_author: str
    story_credit: str
    class Config:
        from_attributes = True

class Story_Content(BaseModel):
    story_content_id: int
    story_id: int
    story_content: str
    class Config:
        from_attributes = True

class Email(BaseModel):
    email_id: int
    email_address: str
    class Config:
        from_attributes = True