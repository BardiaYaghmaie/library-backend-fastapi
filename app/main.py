from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models
import schemas
import crud
from database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Book Endpoints
@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# Member Endpoints
@app.post("/members/", response_model=schemas.Member)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.create_member(db=db, member=member)

@app.get("/members/", response_model=List[schemas.Member])
def read_members(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    members = crud.get_members(db, skip=skip, limit=limit)
    return members

@app.get("/members/{member_id}", response_model=schemas.Member)
def read_member(member_id: int, db: Session = Depends(get_db)):
    db_member = crud.get_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

@app.put("/members/{member_id}", response_model=schemas.Member)
def update_member(member_id: int, member: schemas.MemberCreate, db: Session = Depends(get_db)):
    db_member = crud.update_member(db, member_id=member_id, member=member)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

@app.delete("/members/{member_id}", response_model=schemas.Member)
def delete_member(member_id: int, db: Session = Depends(get_db)):
    db_member = crud.delete_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

# Employee Endpoints
@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

@app.get("/employees/", response_model=List[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees

@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.put("/employees/{employee_id}", response_model=schemas.Employee)
def update_employee(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, employee_id=employee_id, employee=employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.delete("/employees/{employee_id}", response_model=schemas.Employee)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.delete_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

# Publisher Endpoints
@app.post("/publishers/", response_model=schemas.Publisher)
def create_publisher(publisher: schemas.PublisherCreate, db: Session = Depends(get_db)):
    return crud.create_publisher(db=db, publisher=publisher)

@app.get("/publishers/", response_model=List[schemas.Publisher])
def read_publishers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    publishers = crud.get_publishers(db, skip=skip, limit=limit)
    return publishers

@app.get("/publishers/{publisher_id}", response_model=schemas.Publisher)
def read_publisher(publisher_id: int, db: Session = Depends(get_db)):
    db_publisher = crud.get_publisher(db, publisher_id=publisher_id)
    if db_publisher is None:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return db_publisher

@app.put("/publishers/{publisher_id}", response_model=schemas.Publisher)
def update_publisher(publisher_id: int, publisher: schemas.PublisherCreate, db: Session = Depends(get_db)):
    db_publisher = crud.update_publisher(db, publisher_id=publisher_id, publisher=publisher)
    if db_publisher is None:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return db_publisher

@app.delete("/publishers/{publisher_id}", response_model=schemas.Publisher)
def delete_publisher(publisher_id: int, db: Session = Depends(get_db)):
    db_publisher = crud.delete_publisher(db, publisher_id=publisher_id)
    if db_publisher is None:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return db_publisher

# TakenBook Endpoints
@app.post("/takenbooks/", response_model=schemas.TakenBook)
def create_taken_book(taken_book: schemas.TakenBookCreate, db: Session = Depends(get_db)):
    try:
        crud.create_taken_book(db=db, taken_book=taken_book)
        return taken_book
    except HTTPException as e:
        raise e

@app.get("/takenbooks/", response_model=List[schemas.TakenBook])
def read_taken_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    taken_books = crud.get_taken_books(db, skip=skip, limit=limit)
    return taken_books

@app.get("/takenbooks/{taken_book_id}", response_model=schemas.TakenBook)
def read_taken_book(taken_book_id: int, db: Session = Depends(get_db)):
    db_taken_book = crud.get_taken_book(db, taken_book_id=taken_book_id)
    if db_taken_book is None:
        raise HTTPException(status_code=404, detail="Taken book not found")
    return db_taken_book

@app.put("/takenbooks/{taken_book_id}", response_model=schemas.TakenBook)
def update_taken_book(taken_book_id: int, taken_book: schemas.TakenBookCreate, db: Session = Depends(get_db)):
    db_taken_book = crud.update_taken_book(db, taken_book_id=taken_book_id, taken_book=taken_book)
    if db_taken_book is None:
        raise HTTPException(status_code=404, detail="Taken book not found")
    return db_taken_book

@app.delete("/takenbooks/{taken_book_id}", response_model=schemas.TakenBook)
def delete_taken_book(taken_book_id: int, db: Session = Depends(get_db)):
    db_taken_book = crud.delete_taken_book(db, taken_book_id=taken_book_id)
    if db_taken_book is None:
        raise HTTPException(status_code=404, detail="Taken book not found")
    return db_taken_book

@app.post("/calculate_penalty/", response_model=schemas.PenaltyResponse)
def calculate_penalty(penalty_request: schemas.PenaltyRequest, db: Session = Depends(get_db)):
    penalty = crud.calculate_penalty(
        db=db,
        expected_return_date=penalty_request.expected_return_date,
        actual_return_date=penalty_request.actual_return_date
    )
    return schemas.PenaltyResponse(penalty=penalty)