from typing import List, Optional

from pydantic import BaseModel

class ContactBase(BaseModel):
    """ contacts base schema """
    firstname: str
    lastname: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    company_id: Optional[int] = None


class Contact(ContactBase):
    """ contact schema on the base schema """
    id: int

    class Config:
        orm_mode = True

class CompanyBase(BaseModel):
    """ companies base schema """
    email: Optional[str] = None
    name: str
    activityarea_id: Optional[int] = None



class Company(CompanyBase):
    """ company schema on the base model """
    id: int
    contacts: List[Contact] = []
    
    class Config:
        orm_mode = True


class ActivityareaBase(BaseModel):
    """ activity areas base schema """
    name: str


class Activityarea(ActivityareaBase):
    """ activity areas schema on the base schema """
    id: int
    companies: List[Company] = []
    
    class Config:
        orm_mode = True