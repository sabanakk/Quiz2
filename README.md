# Quiz2


# 🧑‍💼 Employee Management System API

A full-featured backend API built with **Django**, **Django REST Framework**, and **PostgreSQL** for managing employees, attendance, and performance reviews. Includes JWT authentication, Swagger API docs, throttling, data visualization (Chart.js), and database seeding with Faker.

---

## 🚀 Features

- CRUD operations for Employees, Attendance, and Performance
- JWT authentication with token refresh
- Filtering, searching, and pagination
- Rate limiting with DRF throttling
- Swagger API documentation with `drf-yasg`
- Chart.js performance visualization
- Seed fake data with `Faker`

---

## ⚙️ Setup Instructions

### 1. Clone the Repository


git clone https://github.com/sabanakk/quiz2.git

### 2. Create and Activate a Virtual Environment
py -m venv venv

To activate : venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Configure Database (PostgreSQL Recommended)
backend/settings.py:

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdbname',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### 5. Run Migrations
python manage.py makemigrations

python manage.py migrate

### 6. Seed the Database (Fake Data)
python manage.py seed

### 7. Create Superuser (optional)
python manage.py createsuperuser

### 8. Start the Development Server
python manage.py runserver

### JWT Authentication

Get Token

### POST /api/token/
json

{
  "username": "yourusername",
  "password": "yourpassword"
}

Use the Token

In request headers:

Authorization: Bearer <your_token>

🔗 API Endpoints

Method	URL	Description

GET	/api/employees/	List all employees

POST	/api/employees/	Add a new employee

GET	/api/attendance/	List attendance records

POST	/api/attendance/	Add attendance record

GET	/api/performance/	List performance reviews

POST	/api/performance/	Add performance review

GET	/api/chart/	View Chart.js performance

GET	/swagger/	Swagger API docs

POST	/api/token/	Get JWT token

POST	/api/token/refresh/	Refresh JWT token

### 📊 Chart View
Visit:
http://localhost:8000/api/chart/

Renders a performance chart using Chart.js.

### 👤 Maintainer
GitHub: @sabanakk

### 📄 License
Licensed under the MIT License.
