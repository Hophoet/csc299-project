from typing import List, Optional

from pydantic import BaseModel

class ContactBase(BaseModel):
    firstname: str
    lastname: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    company_id: Optional[int] = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True

class CompanyBase(BaseModel):
    email: Optional[str] = None
    name: str
    activityarea_id: Optional[int] = None


class CompanyCreate(BaseModel):
    pass

class Company(CompanyBase):
    id: int
    contacts: List[Contact] = []
    
    class Config:
        orm_mode = True


class ActivityareaBase(BaseModel):
    name: str

class ActivityareaCreate(BaseModel):
    pass

class Activityarea(ActivityareaBase):
    id: int
    companies: List[Company] = []
    
    class Config:
        orm_mode = True