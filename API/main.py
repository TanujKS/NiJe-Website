from fastapi import FastAPI, Depends, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import Story, Story_Content, Email
import models
import schemas

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

@app.post("/emails/")
async def create_email(email: schemas.Email, db: Session = Depends(get_db)):
    db_email = models.Email(email=email.email_address)
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return schemas.Email(email_id =db_email.id, email_address=db_email.email)

@app.get("/story/")
def get_story(skip: int = Query(0, alias="page", ge=0), limit: int = Query(10, le=20), db: Session = Depends(get_db)):
    stories = db.query(models.Story).offset(skip * limit).limit(limit).all()
    return stories

@app.get("/story_content/")
def get_story_content(skip: int = Query(0, alias="page", ge=0), limit: int = Query(10, le=20), db: Session = Depends(get_db)):
    story_content = db.query(models.Story_Content).offset(skip * limit).limit(limit).all()
    return story_content