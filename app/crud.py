from sqlalchemy.orm import Session
import models
import schemas


# Book CRUD
def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.Id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.Id == book_id).first()
    if db_book is None:
        return None
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.Id == book_id).first()
    if db_book is None:
        return None
    db.delete(db_book)
    db.commit()
    return db_book

# Member CRUD
def get_members(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Member).offset(skip).limit(limit).all()

def get_member(db: Session, member_id: int):
    return db.query(models.Member).filter(models.Member.Id == member_id).first()

def create_member(db: Session, member: schemas.MemberCreate):
    db_member = models.Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def update_member(db: Session, member_id: int, member: schemas.MemberCreate):
    db_member = db.query(models.Member).filter(models.Member.Id == member_id).first()
    if db_member is None:
        return None
    for key, value in member.dict().items():
        setattr(db_member, key, value)
    db.commit()
    db.refresh(db_member)
    return db_member

def delete_member(db: Session, member_id: int):
    db_member = db.query(models.Member).filter(models.Member.Id == member_id).first()
    if db_member is None:
        return None
    db.delete(db_member)
    db.commit()
    return db_member

# Employee CRUD
def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.Id == employee_id).first()

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = db.query(models.Employee).filter(models.Employee.Id == employee_id).first()
    if db_employee is None:
        return None
    for key, value in employee.dict().items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.Id == employee_id).first()
    if db_employee is None:
        return None
    db.delete(db_employee)
    db.commit()
    return db_employee

# Publisher CRUD
def get_publishers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Publisher).offset(skip).limit(limit).all()

def get_publisher(db: Session, publisher_id: int):
    return db.query(models.Publisher).filter(models.Publisher.Id == publisher_id).first()

def create_publisher(db: Session, publisher: schemas.PublisherCreate):
    db_publisher = models.Publisher(**publisher.dict())
    db.add(db_publisher)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

def update_publisher(db: Session, publisher_id: int, publisher: schemas.PublisherCreate):
    db_publisher = db.query(models.Publisher).filter(models.Publisher.Id == publisher_id).first()
    if db_publisher is None:
        return None
    for key, value in publisher.dict().items():
        setattr(db_publisher, key, value)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

def delete_publisher(db: Session, publisher_id: int):
    db_publisher = db.query(models.Publisher).filter(models.Publisher.Id == publisher_id).first()
    if db_publisher is None:
        return None
    db.delete(db_publisher)
    db.commit()
    return db_publisher

# TakenBook CRUD
def get_taken_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TakenBook).offset(skip).limit(limit).all()

def get_taken_book(db: Session, taken_book_id: int):
    return db.query(models.TakenBook).filter(models.TakenBook.Id == taken_book_id).first()

def create_taken_book(db: Session, taken_book: schemas.TakenBookCreate):
    db_taken_book = models.TakenBook(**taken_book.dict())
    db.add(db_taken_book)
    db.commit()
    db.refresh(db_taken_book)
    return db_taken_book

def update_taken_book(db: Session, taken_book_id: int, taken_book: schemas.TakenBookCreate):
    db_taken_book = db.query(models.TakenBook).filter(models.TakenBook.Id == taken_book_id).first()
    if db_taken_book is None:
        return None
    for key, value in taken_book.dict().items():
        setattr(db_taken_book, key, value)
    db.commit()
    db.refresh(db_taken_book)
    return db_taken_book

def delete_taken_book(db: Session, taken_book_id: int):
    db_taken_book = db.query(models.TakenBook).filter(models.TakenBook.Id == taken_book_id).first()
    if db_taken_book is None:
        return None
    db.delete(db_taken_book)
    db.commit()
    return db_taken_book
