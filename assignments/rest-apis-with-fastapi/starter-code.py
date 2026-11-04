# Starter Code for Building REST APIs with FastAPI
# Rename this file to main.py and run: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


# In-memory "database"
books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "year": 2019},
    {"id": 2, "title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2019},
    {"id": 3, "title": "Think Python", "author": "Allen B. Downey", "year": 2015},
]


# Task 1: Create your first endpoints
# TODO: GET /  -> return a welcome message


# TODO: GET /hello/{name}  -> return a personalized greeting


# Task 2: Read books
# TODO: GET /books  -> return all books


# TODO: GET /books/{book_id}  -> return one book or raise HTTPException(status_code=404)


# Task 3: Add, update, and delete books
# TODO: POST /books  -> add a new book (status_code=201)


# TODO: PUT /books/{book_id}  -> update an existing book


# TODO: DELETE /books/{book_id}  -> remove a book
