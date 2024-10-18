# DYNASAS DJANGO REST API TASK

This project is a RESTful API built using Django and Django REST Framework (DRF).


## Prerequisites

Ensure you have the following installed before setting up the project:

- Python 3.x
- Django 5.x (or your preferred version)
- Django REST Framework (DRF)
- PostgreSQL
- pip (Python package installer)
- Git

## Setup Instructions

Follow the steps below to set up and run the application.

### 1. Clone the Repository

```bash
git clone https://github.com/vinayakyan/dynasas.git
cd dynasas

### 2. Setup the virtual environment
py -m venv venv  # For Linux/MacOS: python3 -m venv venv
venv\Scripts\activate  #For Linux/MacOS: source venv/bin/activate

### 3. Install Dependencies
cd blog_project
pip install -r requirements.txt

### 4. Run migrations
py manage.py migrate #for Linux/MacOS: python3 manage.py migrate

### 5. Running the Application
py manage.py runserver

### 6. API endpoints
    1. /v1/user/ - POST request to create a new user with username, password and email
    2. /token/ - POST request to get the token of user
    3. /v1/posts/ - POST request to create a new post
    4. /v1/posts/ - GET request to retrieve all the posts
    5. v1/posts/<pk>/ - GET request to retrieve the post by id.
    6. v1/posts/<pk>/ - PUT request to update the post by id.
    7. v1/posts/<pk>/ - DELETE request to delete the post by id.

