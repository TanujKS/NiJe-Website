from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import Story, Story_Content
import models

app = FastAPI()

@app.get('/')
def index():
    return {"message": "Hello World"}

@app.get('/story/{id}')
def get_story_by_id(id: int, db: Session = Depends(get_db)):
    data = db.query(Story).filter(models.Story.story_id == id).all()
    return data

@app.get('/story_content/{id}')
def get_story_content_by_id(id: int, db: Session = Depends(get_db)):
    data = db.query(Story_Content).filter(models.Story_Content.story_content_id == id).all()
    return data
