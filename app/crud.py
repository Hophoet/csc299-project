from sqlalchemy.orm import Session

from . import models, schemas

#CONTACT
def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    """ contacts getter """
    return db.query(models.Contact).offset(skip).limit(limit).all()

def get_contact_by_id(db: Session, id: int):
    """ contact getter by id """
    return db.query(models.Contact).filter(models.Contact.id == id).first()


#COMPANY
def get_companies(db: Session, skip: int = 0, limit: int = 100):
    """ companies getter """
    return db.query(models.Company).offset(skip).limit(limit).all()

def get_company_by_id(db: Session, id: int):
    """ company getter by id """
    return db.query(models.Company).filter(models.Company.id == id).first()


#ACTIVITY AREAS
def get_activityareas(db: Session, skip: int = 0, limit: int = 100):
    """ activity areas getter"""
    return db.query(models.Activityarea).offset(skip).limit(limit).all()

def get_activityarea_by_id(db: Session, id: int):
    """ activity areas getter by id """
    return db.query(models.Activityarea).filter(models.Activityarea.id == id).first()


#COMMONS
def search(db: Session, query: str):
    """ items search getter """
    #set the empty dictionay for the items saving
    json = {}
    items =  db.query(models.Contact).filter(models.Contact.firstname == query).all()
    #find contact items case, with there saving 
    if(items):
        json['contacts'] = items
    items =  db.query(models.Company).filter(models.Company.name == query).all()
    #find company items case, with there saving 
    if(items):
        json['companies'] = items
    items =  db.query(models.Activityarea).filter(models.Activityarea.name == query).all()
    #find actity area items case, with there saving 
    if(items):
        json["activity areas"] = items    
    return json

