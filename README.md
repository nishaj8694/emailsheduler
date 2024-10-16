# Dynamic Email Scheduler with JWT Authentication
Welcome to the Dynamic Email Scheduler project. This project leverages Django, Celery, and Redis to allow users to schedule emails at a specific time. Additionally, it includes JWT authentication using Django REST Framework.

# Features
Email Scheduling: Users can create and schedule emails to be sent at a specified time.
JWT Authentication: Secure user authentication using JSON Web Tokens (JWT) with Django REST Framework.

# Prerequisites
  Python 3.x
  Django
  Django REST Framework
  Celery
  Redis
  django-celery-results

# Installation
Clone the Repository
      git clone https://github.com/yourusername/machineTest.git
      cd machineTest
Create Virtual Environment
        python -m venv venv
        source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies
        pip install -r requirements.txt

Configure Django Settings
        Update settings.py with your database configuration, Celery settings, and JWT settings.

Run Migrations
        python manage.py migrate

Create Superuser
         python manage.py createsuperuser

Start the Development Server
         python manage.py runserver

Start Redis Server
        redis-server

Start Celery Worker
        celery -A your_project_name worker --loglevel=info

# usage
Register and Login
        Use the provided endpoints to register and obtain a JWT token.

Schedule an Email
        Use the authenticated endpoint to create an email and set the desired sending time
