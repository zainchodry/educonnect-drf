# 🎓 EduConnect – Smart Course & Enrollment Management API

EduConnect is a modern Django REST Framework (DRF) based API project designed to simulate a real-world e-learning platform. It helps instructors manage courses and allows students to enroll, learn, and review those courses. This project improves your backend logic and builds a strong portfolio-worthy project.

---

## 📌 Key Features

- 🔐 Secure authentication system
- 👩‍🏫 Instructor-only course creation and management
- 🧑‍🎓 Student course enrollment
- 🌟 Course review and feedback system
- ⚙️ Role-based permissions
- 📃 Easily extendable API-based structure

---

## 🛠️ Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- SQLite (for development) / PostgreSQL (for production-ready)
- Token-based authentication
- Optional: Swagger/Postman for API documentation

---

## 📁 Project Structure

educonnect/
│
├── accounts/ # For user model (Instructor, Student)
├── courses/ # For courses, enrollments, reviews
├── educonnect/ # Project settings and URLs
├── templates/ # (If you add browsable frontend later)
├── manage.py # Django CLI entry point
├── requirements.txt # Dependencies
└── README.md # This file



---

## 🔗 API Endpoints Overview

> You can test these APIs using **Postman**, **Insomnia**, or **Swagger UI** (if integrated).

### 🔐 Authentication

| Method | Endpoint         | Description             |
|--------|------------------|-------------------------|
| POST   | /api/register/   | Register new user       |
| POST   | /api/login/      | Login and get token     |

---

### 📚 Courses

| Method | Endpoint             | Description                        | Access        |
|--------|----------------------|------------------------------------|---------------|
| GET    | /api/courses/        | List all courses                   | Public        |
| POST   | /api/courses/        | Create a new course                | Instructor    |
| PUT    | /api/courses/<id>/   | Update a course                    | Instructor    |
| DELETE | /api/courses/<id>/   | Delete a course                    | Instructor    |

---

### 🧑‍🎓 Enrollments

| Method | Endpoint             | Description                        | Access    |
|--------|----------------------|------------------------------------|-----------|
| GET    | /api/enrollments/    | List my enrolled courses           | Student   |
| POST   | /api/enrollments/    | Enroll in a course                 | Student   |

---

### 📝 Reviews

| Method | Endpoint             | Description                        | Access    |
|--------|----------------------|------------------------------------|-----------|
| GET    | /api/reviews/        | List my reviews                    | Student   |
| POST   | /api/reviews/        | Review a course                    | Student   |

---

## ⚙️ Getting Started

Follow the instructions below to run this project locally:

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/zainchodry/educonnect-drf.git
cd educonnect-drf


#2️⃣ Setup Virtual Environment

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate



#3️⃣ Install Dependencies
pip install -r requirements.txt



#4 Run the Server
python3 manage.py runserver

