# flask-rest-api-playground

A simple REST API built with Python and Flask to understand how REST APIs work. Covers full CRUD — Create, Read, Update, Delete — using proper HTTP methods and status codes.

---

## What I Learned Building This

- What a REST API is and how it works
- HTTP methods — GET, POST, PUT, DELETE
- How a client and server communicate via JSON
- How to test APIs using Postman
- Status codes — 200, 201, 404

---

## Tech Used

- Python
- Flask

---

## How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/flask-rest-api-playground
cd flask-rest-api-playground
```

**2. Install dependencies**
```bash
pip install flask
```

**3. Run the server**
```bash
python app.py
```

Server runs at `http://127.0.0.1:5000`

---

## API Endpoints

### Get all todos
```
GET /todos
```
Response:
```json
[
    {"id": 1, "task": "Buy groceries"},
    {"id": 2, "task": "Study Flask"}
]
```

---

### Create a new todo
```
POST /todos
```
Body:
```json
{
    "task": "Learn Postman"
}
```
Response: `201 Created`
```json
{"id": 3, "task": "Learn Postman"}
```

---

### Update a todo
```
PUT /todos/<id>
```
Body:
```json
{
    "task": "Study Flask and REST API"
}
```
Response: `200 OK`
```json
{"id": 2, "task": "Study Flask and REST API"}
```

---

### Delete a todo
```
DELETE /todos/<id>
```
Response: `200 OK`
```json
{"message": "Todo deleted"}
```

---

## What's Next

- Connect a real database (SQLite or PostgreSQL)
- Add user authentication with JWT
- Deploy to a cloud server
