# REST-API-with-Flask
# 🔥 REST API with Flask

This project demonstrates a simple **REST API built using Python and Flask**.  
It supports basic CRUD operations (Create, Read, Update, Delete) for managing user data.  
The goal of this project is to understand **API development fundamentals** and how REST endpoints work.

---

## 🚀 Features
- Create a new user (POST)
- Retrieve all users (GET)
- Retrieve a single user by ID (GET)
- Update existing user data (PUT)
- Delete a user by ID (DELETE)
- In-memory data storage (dictionary)
- Fully testable using cURL, Postman, or browser

---

## 🛠️ Technologies Used
- **Python 3**
- **Flask** (micro web framework)
- **cURL / Postman** (for testing API endpoints)

Install Flask:

```bash
pip install flask
▶️ How to Run the API

Clone the project:

git clone https://github.com/18Sonika/REST-API-with-Flask.git


Navigate to the folder:

cd REST-API-with-Flask


Install dependencies:

pip install flask


Run the Flask app:

python app.py


The API will start on:

http://127.0.0.1:5000

🧠 API Endpoints
✔ 1. Get all users
GET /users

✔ 2. Get user by ID
GET /users/<id>

✔ 3. Create a new user
POST /users

JSON Body Example:
{
  "id": "1",
  "name": "Sonika",
  "email": "sonika@example.com"
}

✔ 4. Update an existing user
PUT /users/<id>

JSON Body Example:
{
  "name": "New Name",
  "email": "newemail@example.com"
}

✔ 5. Delete a user
DELETE /users/<id>

🧪 Testing the API with cURL
Add a user (POST)
curl -X POST http://127.0.0.1:5000/users ^
    -H "Content-Type: application/json" ^
    -d "{\"id\":\"1\", \"name\":\"Sonika\", \"email\":\"sonika@example.com\"}"

Get all users (GET)
curl -X GET http://127.0.0.1:5000/users

Update user (PUT)
curl -X PUT http://127.0.0.1:5000/users/1 ^
    -H "Content-Type: application/json" ^
    -d "{\"name\":\"Updated Name\"}"

Delete user (DELETE)
curl -X DELETE http://127.0.0.1:5000/users/1

📌 Outcome

By completing this project, you learn:

How REST APIs work

How to build endpoints using Flask

How to handle CRUD logic

How to test APIs using cURL and Postman

Basics of API response formats (JSON)
