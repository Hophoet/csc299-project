from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

#create the app main object
app = FastAPI()

# database managment object getter
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    """ root endpoint for the API Presentation"""
    return {
        'Message': 'Welcome on the contacts management API application',
        'Endpoints':{
            '/contacts/?d=0&f=20': 'get contacts from 0 to 20',
            '/contact/contact_id': 'get contact as id=contact_id',
            '/companies/?d=0&f=20': 'get companies from 0 to 20',
            '/company/company_id': 'get company as id=company_id',
            '/activityareas/?d=0&f=20': 'get activity areas from 0 to 20',
            '/activityarea/activityarea_id': 'get activity area as id=activityarea_id',
            '/search/?query=q': 'get all items(contact, company, activity area) as name q'
            
        }
        }



@app.get("/contacts/", response_model=List[schemas.Contact])
def read_contacts(d: int = 0, f: int = 100, db: Session = Depends(get_db)):
    """ all contacts getter endpoind """
    #get contacts
    contacts = crud.get_contacts(db, skip=d, limit=f)
    return contacts

@app.get("/contact/{contact_id}")
def read_contact(contact_id: int, q: str = None, db: Session = Depends(get_db)):
    """ specific contact getter endpoint """
    #get contact by the id 
    contact = crud.get_contact_by_id(db, contact_id)
    return contact



@app.get("/companies/", response_model=List[schemas.Company])
def read_companies(d: int = 0, f: int = 100, db: Session = Depends(get_db)):
    """ all companies getter endpoint """
    #get companies
    companies = crud.get_companies(db, skip=d, limit=f)
    return companies

@app.get("/company/{company_id}")
def read_company(company_id: int, q: str = None, db: Session = Depends(get_db)):
    """ specific company getter endpoint """
    #get company by the id 
    company = crud.get_company_by_id(db, company_id)
    return company




@app.get("/activityareas/", response_model=List[schemas.Activityarea])
def read_activityareas(d: int = 0, f: int = 100, db: Session = Depends(get_db)):
    """ all acitivity areas getter endpoint """
    #get activity areas 
    activityareas = crud.get_activityareas(db, skip=d, limit=f)
    return activityareas

@app.get("/activityarea/{activityarea_id}")
def read_activityarea(activityarea_id: int, q: str = None, db: Session = Depends(get_db)):
    """ specific activity area getter endpoint """
    #get activity area  by the id 
    activityarea = crud.get_activityarea_by_id(db, activityarea_id)
    return activityarea



@app.get("/search/")
def search( query: str = None, db: Session = Depends(get_db)):
    """ seach items(contact, company, activity area) getter """
    #get items from the crud search method
    items = crud.search(db, query)
    #items not found case
    if(not items):
        #raise not found exception
        raise HTTPException(status_code=404, detail="item not found")
    return items
