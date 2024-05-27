from pydantic import BaseModel
from datetime import date
from typing import Optional

# Book Schemas
class BookBase(BaseModel):
    PublisherId: int
    Name: str
    Genre: str
    Price: float

class BookCreate(BookBase):
    PublisherId: int

class Book(BookBase):
    Id: int

    class Config:
        orm_mode = True

# Member Schemas
class MemberBase(BaseModel):
    FirstName: str
    LastName: str
    Email: Optional[str] = None
    Phone: Optional[str] = None
    Address: Optional[str] = None
    DateJoined: date

class MemberCreate(MemberBase):
    DateJoined: date

class Member(MemberBase):
    Id: int

    class Config:
        orm_mode = True

# Employee Schemas
class EmployeeBase(BaseModel):
    FirstName: str
    LastName: str
    DateJoined: date
    Salary: float
    Position: str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    Id: int

    class Config:
        orm_mode = True

# Publisher Schemas
class PublisherBase(BaseModel):
    Name: str
    Address: str

class PublisherCreate(PublisherBase):
    pass

class Publisher(PublisherBase):
    Id: int

    class Config:
        orm_mode = True

# TakenBook Schemas
class TakenBookBase(BaseModel):
    MemberId: int
    BookId: int
    IsTaken: bool
    BorrowDate: Optional[date] = None
    ReturnDate: Optional[date] = None

class TakenBookCreate(TakenBookBase):
    pass

class TakenBook(TakenBookBase):
    Id: int

    class Config:
        orm_mode = True

class PenaltyRequest(BaseModel):
    expected_return_date: date
    actual_return_date: date

class PenaltyResponse(BaseModel):
    penalty: int
