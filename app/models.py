from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="contacts")


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    phone = Column(String)
    email = Column(String)
    activityarea_id = Column(Integer, ForeignKey("activityareas.id"))

    contacts = relationship("Contact", back_populates="company")
    activityarea = relationship("Activityarea", back_populates="companies")



class Activityarea(Base):
    __tablename__ = "activityareas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    companies = relationship("Company", back_populates="activityarea")