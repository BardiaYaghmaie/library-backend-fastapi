from sqlalchemy.orm import Session
from sqlalchemy import text
import models
import schemas


# Book CRUD operations
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        for key, value in book.dict().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

# Member CRUD operations
def create_member(db: Session, member: schemas.MemberCreate):
    db_member = models.Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def get_members(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Member).offset(skip).limit(limit).all()

def get_member(db: Session, member_id: int):
    return db.query(models.Member).filter(models.Member.id == member_id).first()

def update_member(db: Session, member_id: int, member: schemas.MemberCreate):
    db_member = db.query(models.Member).filter(models.Member.id == member_id).first()
    if db_member:
        for key, value in member.dict().items():
            setattr(db_member, key, value)
        db.commit()
        db.refresh(db_member)
    return db_member

def delete_member(db: Session, member_id: int):
    db_member = db.query(models.Member).filter(models.Member.id == member_id).first()
    if db_member:
        db.delete(db_member)
        db.commit()
    return db_member

# Employee CRUD operations
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        for key, value in employee.dict().items():
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee

# Publisher CRUD operations
def create_publisher(db: Session, publisher: schemas.PublisherCreate):
    db_publisher = models.Publisher(**publisher.dict())
    db.add(db_publisher)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

def get_publishers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Publisher).offset(skip).limit(limit).all()

def get_publisher(db: Session, publisher_id: int):
    return db.query(models.Publisher).filter(models.Publisher.id == publisher_id).first()

def update_publisher(db: Session, publisher_id: int, publisher: schemas.PublisherCreate):
    db_publisher = db.query(models.Publisher).filter(models.Publisher.id == publisher_id).first()
    if db_publisher:
        for key, value in publisher.dict().items():
            setattr(db_publisher, key, value)
        db.commit()
        db.refresh(db_publisher)
    return db_publisher

def delete_publisher(db: Session, publisher_id: int):
    db_publisher = db.query(models.Publisher).filter(models.Publisher.id == publisher_id).first()
    if db_publisher:
        db.delete(db_publisher)
        db.commit()
    return db_publisher

# TakenBook CRUD operations
def create_taken_book(db: Session, taken_book: schemas.TakenBookCreate):
    try:
        db.execute(
            text("CALL AddTakenBook(:p_memberId, :p_bookId, :p_borrowDate)"),
            {
                "p_memberId": taken_book.member_id,
                "p_bookId": taken_book.book_id,
                "p_borrowDate": taken_book.borrow_date,
            },
        )
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_taken_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TakenBook).offset(skip).limit(limit).all()

def get_taken_book(db: Session, taken_book_id: int):
    return db.query(models.TakenBook).filter(models.TakenBook.id == taken_book_id).first()

def update_taken_book(db: Session, taken_book_id: int, taken_book: schemas.TakenBookCreate):
    db_taken_book = db.query(models.TakenBook).filter(models.TakenBook.id == taken_book_id).first()
    if db_taken_book:
        for key, value in taken_book.dict().items():
            setattr(db_taken_book, key, value)
        db.commit()
        db.refresh(db_taken_book)
    return db_taken_book

def delete_taken_book(db: Session, taken_book_id: int):
    db_taken_book = db.query(models.TakenBook).filter(models.TakenBook.id == taken_book_id).first()
    if db_taken_book:
        db.delete(db_taken_book)
        db.commit()
    return db_taken_book
##
def calculate_penalty(db: Session, expected_return_date: str, actual_return_date: str) -> int:
    result = db.execute(
        text("SELECT CalculatePenalty(:expectedReturnDate, :actualReturnDate) AS penalty"),
        {"expectedReturnDate": expected_return_date, "actualReturnDate": actual_return_date}
    ).fetchone()
    return result['penalty'] if result else 0