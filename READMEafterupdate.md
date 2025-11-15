# DevOps Bootcamp Flask Application

This project is a simple Flask web application built as part of the DevOps Bootcamp assignment.  
The app allows users to register with name, email, and bio, and allows adding posts associated with each user.  
The backend uses **Flask + SQLAlchemy + MySQL (via Docker)**.

---

## 📌 Features

### 👤 User Management

- Add new users (name, email, bio)
- Prevent duplicate emails
- Display all registered users

### 📝 Post System

- Add posts linked to a specific user
- Display all posts ordered by newest first

### 🗄 Database

- MySQL database running in Docker
- SQLAlchemy ORM models:
  - **User**: id, name, email, bio
  - **Post**: id, title, content, user_id, created_at

### 🌐 Frontend

- HTML templates rendered using Jinja2
- Simple forms for adding users and posts

---

## 🛠 Technologies Used

- Python 3
- Flask
- SQLAlchemy
- MySQL
- Docker / Docker Compose
- HTML + Jinja2

---

## 📂 Project Structure
