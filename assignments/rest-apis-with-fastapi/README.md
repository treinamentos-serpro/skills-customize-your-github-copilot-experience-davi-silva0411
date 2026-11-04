# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API in Python using the FastAPI framework. You'll create endpoints that read, create, update, and delete data, and see how HTTP methods and status codes work together.

## 📝 Tasks

### 🛠️	Create Your First Endpoint

#### Description
Set up a FastAPI app using `starter-code.py` and create a simple endpoint that greets the user. Install the dependencies with `pip install fastapi uvicorn`, rename the file to `main.py`, run the server with `uvicorn main:app --reload`, and open `http://127.0.0.1:8000/docs` to try it out.

#### Requirements
Completed program should:

- Define a `GET /` endpoint that returns `{"message": "Welcome to the Book API!"}`
- Define a `GET /hello/{name}` endpoint that returns a personalized greeting using a path parameter
- Run without errors and show both endpoints in the interactive docs at `/docs`

Example:

```
GET /hello/Ana
{"message": "Hello, Ana!"}
```


### 🛠️	Read Books from the API

#### Description
Use the in-memory `books` list in the starter code to build endpoints that return book data.

#### Requirements
Completed program should:

- Define a `GET /books` endpoint that returns the full list of books
- Define a `GET /books/{book_id}` endpoint that returns a single book by its `id`
- Return a `404` error with a clear message when a book is not found (use `HTTPException`)

Example:

```
GET /books/1
{"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "year": 2019}

GET /books/99
{"detail": "Book not found"}
```


### 🛠️	Add, Update, and Delete Books

#### Description
Complete the CRUD operations using the `Book` Pydantic model so FastAPI validates incoming data automatically.

#### Requirements
Completed program should:

- Define a `POST /books` endpoint that adds a new book and returns it with status code `201`
- Define a `PUT /books/{book_id}` endpoint that updates an existing book
- Define a `DELETE /books/{book_id}` endpoint that removes a book
- Return a `404` error when updating or deleting a book that doesn't exist

Example:

```
POST /books
{"id": 4, "title": "Fluent Python", "author": "Luciano Ramalho", "year": 2022}

Response (201):
{"id": 4, "title": "Fluent Python", "author": "Luciano Ramalho", "year": 2022}
```
