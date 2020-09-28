from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {'Hello': 'World'}

@app.get("/contacts/{contact_id}")
def read_contact(contact_id: int, q: str = None, db: Session = Depends(get_db)):
    contact = crud.get_contact_by_id(db, contact_id)
    return contact

@app.get("/contacts/", response_model=List[schemas.Contact])
def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contacts = crud.get_contacts(db, skip=skip, limit=limit)
    #print(contacts)
    return contacts

@app.get("/companies/", response_model=List[schemas.Company])
def read_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = crud.get_companies(db, skip=skip, limit=limit)
    #print(companies)
    return companies

@app.get("/activityareas/", response_model=List[schemas.Activityarea])
def read_activityareas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    activityareas = crud.get_activityareas(db, skip=skip, limit=limit)
    #print(companies)
    return activityareas