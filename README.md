This repository contains my practice code as I learn Django and I’m currently following tutorials by [Tech with Rathan](https://www.youtube.com/watch?v=3gpo9piG12E&t=4095s),and using this space to apply what I’ve learned through small projects, experiments, and exercises. 

## Django Basics 

**Django** is an open-source Python web framework used to build **fast, scalable, and secure** web applications. It follows the **MVT (Model-View-Template)** architecture and provides built-in tools that reduce development time.

---

## 🧰 What is a Framework?
A **framework** is a collection of software modules, tools, and reusable components used to build applications.

### ✔ Why frameworks are used?
- Avoid repetitive code  
- Reduce errors  
- Provide structure and best practices  
- Speed up development  

---

## 🚀 Why Django?
- Highly **scalable**
- Clean, simple, and **fast**
- Uses **DRY principle** (Don’t Repeat Yourself)
- Secure (prevents SQL injection, XSS, CSRF attacks)
- Comes with batteries-included features (ORM, admin, sessions, authentication)

---

# ⚙️ Django Setup

## 1. Create Virtual Environment
```bash
python -m venv env
```
## 2. Install Django
```bash
pip install django
```
## 3. Create a Django Project
```bash
django-admin startproject project_name
```
This creates a folder structure as follows :-
project/
│── manage.py
│── project_name/
    │── __init__.py
    │── settings.py
    │── urls.py
    │── asgi.py
    │── wsgi.py

# Explanation of Django files :
## 1. manage.py
Command line utility that lets one interact with the django project . To execute the Development server ,command is:-
```bash
python manage.py runserver
```
To create a new app, command is:-
```bash
python manage.py startapp <appname>
```
To change password, command is:- 
```bash
python manage.py changepassword <Your user name>
```
and many more.. 

## 2. __init__.py
It is a python package .
## 3. wsgi.py
It is Used to deploy our applications on production server like apache and Ingenir(WSGI - Web Server Gateway Interface)
## 4. asgi.py
Asynchronous Server Gateway Interface, it works similar to wsgi but with additional functionalities. 

## 5. urls.py 
(URL - Universe Resource Locator) It contains all the endpoints that one should have for a project .

## 6. Settings.py 
Most imp file in Django project.It is used to add all the configurations of django project. Following are the various Default Configurations:-
| Setting                      | Description                                              |
| ---------------------------- | -------------------------------------------------------- |
| **BASE_DIR**                 | Path to the project’s root directory                     |
| **SECRET_KEY**               | Used for generating hashes and tokens — keep it secret!  |
| **DEBUG**                    | `True` during development, `False` in production         |
| **ALLOWED_HOSTS**            | List of allowed domains/server names                     |
| **INSTALLED_APPS**           | List of apps enabled for the project                     |
| **MIDDLEWARE**               | Layer between request & response for security/processing |
| **ROOT_URLCONF**             | Points to main `urls.py`                                 |
| **TEMPLATES**                | Template engine configuration (HTML files)               |
| **WSGI_APPLICATION**         | WSGI entry point for deployment                          |
| **DATABASES**                | DB configuration (default: SQLite)                       |
| **AUTH_PASSWORD_VALIDATORS** | Password validation rules                                |
| **LANGUAGE_CODE**            | Default language (e.g., 'en-us')                         |
| **TIME_ZONE**                | Project timezone                                          |
| **STATIC_URL**               | URL path for static files (CSS/JS)                       |
| **MEDIA_URL / MEDIA_ROOT**   | Used for handling uploaded files                         |

## 🧠 How Django Works – MVT Architecture

Django follows the **Model–View–Template (MVT)** design pattern.

---

### 🟦 **Model (M)**
- Represents the **database layer**
- Defines the structure of your data
- Interacts with the database using Django ORM
- **File:** `models.py`

---

### 🟩 **View (V)**
- Contains **business logic**
- Takes data from the Model and sends it to the Template
- Handles requests and returns responses
- **File:** `views.py`

---

### 🟧 **Template (T)**
- Frontend layer (**HTML/CSS/JS**)
- Displays data sent from the View
- **File example:** `templates/index.html`

---








