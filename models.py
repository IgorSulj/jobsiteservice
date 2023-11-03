from datetime import date
from enum import Enum
from pydantic import BaseModel, EmailStr, PositiveInt
from pydantic.alias_generators import to_camel

from utils import Base64ImageStr, PhoneStr


class Personal(BaseModel):
    russian_name: str
    english_name: str

    class FamilyStatus(Enum):
        not_married = 'not-married'

    family_status: FamilyStatus
    birthday: date

    class WantedJob(Enum):
        germany = 'germany'
        europe = 'europe'

    salary: PositiveInt
    wanted_job: WantedJob

    class Config:
        alias_generator = to_camel


class Contacts(BaseModel):
    country: str
    city: str
    street: str
    flat: str
    index: str
    phone: PhoneStr
    email: EmailStr

    class Config:
        alias_generator = to_camel


class Education(BaseModel):
    start: int
    end: int
    name: str
    specialization: str
    qualification: str
    photo: Base64ImageStr

    class Config:
        alias_generator = to_camel


class Experience(BaseModel):
    start: int
    end: int
    organization: str
    position: str
    skills: str

    class Config:
        alias_generator = to_camel


class Additional(BaseModel):
    driving_license: str
    had_criminal_liability: bool
    additional: str

    class Config:
        alias_generator = to_camel


class WorkBlankModel(BaseModel):
    personal: Personal
    contacts: Contacts
    education: list[Education]
    experience: list[Experience]
    additional: Additional
