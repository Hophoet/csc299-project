from sqlalchemy.orm import Session

from . import models, schemas

def get_contact(db: Session, contact_id: int):
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()

def get_contact_by_email(db: Session, email: str):
    return db.query(models.Contact).filter(models.Contact.email == email).first()

def get_contact_by_id(db: Session, id: int):
    return db.query(models.Contact).filter(models.Contact.id == id).first()

def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contact).offset(skip).limit(limit).all()

def create_contact(db: Session, contact: schemas.ContactCreate):
    db_contact = models.Contact(firstname=contact.firstname, lastname=contact.lastname, phone=contact.phone)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Company).offset(skip).limit(limit).all()

def get_activityareas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Activityarea).offset(skip).limit(limit).all()