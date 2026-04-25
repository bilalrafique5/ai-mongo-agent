# 🚀 AI MongoDB Agent

![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a393?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-Async-green?style=for-the-badge&logo=mongodb)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python)
![Gemini AI](https://img.shields.io/badge/Gemini-AI-blue?style=for-the-badge&logo=google)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 📌 Overview

AI-powered MongoDB query system that converts **natural language into MongoDB operations** using **Gemini AI + FastAPI + MongoDB (Motor)**.

---

## ⚡ Features

- 🤖 Natural language → MongoDB query conversion  
- 📊 Dynamic schema detection  
- 🔍 AI-based collection selection  
- 🔐 JWT authentication system  
- ⚡ Fully async backend (FastAPI + Motor)  
- 🧩 Modular and scalable architecture  

---

## 🏗️ Tech Stack

- FastAPI  
- MongoDB (Motor)  
- Gemini AI (Google GenAI)  
- JWT (JOSE)  
- Passlib (Argon2)  
- Pydantic  

---

## 🚀 API Features

### 🔐 Authentication
- Register user  
- Login (JWT token generation)  

### 👤 Person CRUD
- Create / Read / Update / Delete  
- Search by name  
- Filter by starting letter  

### 🤖 AI Query Engine
- Natural language → MongoDB filter  
- Schema detection  
- Collection auto-selection  

---

## 📡 AI Query Example

```http
POST /AI/query
````

### Request

```json
"Find all persons with age greater than 25"
```

### Response

```json
{
  "collection": "persons",
  "filter": {
    "age": { "$gt": 25 }
  },
  "result": []
}
```

---

## 🔐 Authentication APIs

### Register

```http
POST /auth/register
```

### Login

```http
POST /auth/login
```

### Response

```json
{
  "access_token": "jwt_token_here",
  "token_type": "bearer"
}
```

---

## 🧩 Project Structure

```
app/
 ├── agents/
 ├── crud/
 ├── routes/
 ├── schemas/
 ├── utils/
 ├── database.py
 ├── config.py
 └── main.py
```

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/your-username/ai-mongo-agent.git
cd ai-mongo-agent
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🔑 Environment Variables

```env
MONGO_URI=
DATABASE_NAME=
GEMINI_API_KEY=
SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## 📈 Future Improvements

* Role-based access control (RBAC)
* Query caching layer
* Advanced prompt engineering
* Docker deployment
* Logging & monitoring

---

## 👨‍💻 Author

**Bilal Rafique**
🔗 [https://linkedin.com/in/bilal-rafique5](https://linkedin.com/in/bilal-rafique5)

---

