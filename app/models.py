from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Book(Base):
    __tablename__ = 'Books'
    Id = Column(Integer, primary_key=True, index=True)
    PublisherId = Column(Integer, ForeignKey('Publishers.Id'))
    Name = Column(String(50))
    Genre = Column(String(50))
    Price = Column(Float)

class Member(Base):
    __tablename__ = 'Members'
    Id = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    Email = Column(String(50), nullable=True)
    Phone = Column(String(11), nullable=True)
    Address = Column(String(100), nullable=True)
    DateJoined = Column(Date)

class Employee(Base):
    __tablename__ = 'Employees'
    Id = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    DateJoined = Column(Date)
    Salary = Column(Float)
    Position = Column(String(50))

class Publisher(Base):
    __tablename__ = 'Publishers'
    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(50))
    Address = Column(String(100))

class TakenBook(Base):
    __tablename__ = 'TakenBook'
    Id = Column(Integer, primary_key=True, index=True)
    MemberId = Column(Integer, ForeignKey('Members.Id'))
    BookId = Column(Integer, ForeignKey('Books.Id'))
    IsTaken = Column(Boolean)
    BorrowDate = Column(Date, nullable=True)
    ReturnDate = Column(Date, nullable=True)

class EventLog(Base):
    __tablename__ = 'EventLog'
    Id = Column(Integer, primary_key=True, index=True)
    EventType = Column(String(10))
    TableName = Column(String(50))
    EventTime = Column(Date)
    EventData = Column(String(100))

class EventLogBook(Base):
    __tablename__ = 'Logs_Books'
    Id = Column(Integer, primary_key=True, index=True)
    EventType = Column(String(10))
    TableName = Column(String(50))
    EventTime = Column(Date)
    EventData = Column(String(100))

class EventLogMember(Base):
    __tablename__ = 'Logs_Members'
    Id = Column(Integer, primary_key=True, index=True)
    EventType = Column(String(10))
    TableName = Column(String(50))
    EventTime = Column(Date)
    EventData = Column(String(100))

class EventLogEmployee(Base):
    __tablename__ = 'Logs_Employees'
    Id = Column(Integer, primary_key=True, index=True)
    EventType = Column(String(10))
    TableName = Column(String(50))
    EventTime = Column(Date)
    EventData = Column(String(100))

class EventLogPublishers(Base):
    __tablename__ = 'Logs_Publishers'
    Id = Column(Integer, primary_key=True, index=True)
    EventType = Column(String(10))
    TableName = Column(String(50))
    EventTime = Column(Date)
    EventData = Column(String(100))