# Dynamic Email Scheduler with JWT Authentication
Welcome to the Dynamic Email Scheduler project. This project leverages Django, Celery, and Redis to allow users to schedule emails at a specific time. Additionally, it includes JWT authentication using Django REST Framework.

# Features
Email Scheduling: Users can create and schedule emails to be sent at a specified time.<br>
JWT Authentication: Secure user authentication using JSON Web Tokens (JWT) with Django REST Framework.

# Prerequisites
  Python 3.<br>
  Django<br>
  Django REST Framework<br>
  Celery<br>
  Redis<br>
  django-celery-results<br>

# Installation
Clone the Repository<br>
      git clone https://github.com/yourusername/machineTest.git<br>
      cd machineTest<br>

Create Virtual Environment<br>
        python -m venv venv<br>
        source venv/bin/activate  # On Windows: venv\Scripts\activate<br>

Install Dependencies<br>
        pip install -r requirements.txt<br>

Configure Django Settings<br>
        Update settings.py with your database configuration, Celery settings, and JWT settings.<br>

Run Migrations<br>
        python manage.py migrate<br>

Create Superuser<br>
         python manage.py createsuperuser<br>

Start the Development Server<br>
         python manage.py runserver<br>

Start Redis Server<br>
        redis-server<br>

Start Celery Worker<br>
        celery -A machineTest worker --loglevel=info<br>

# usage
Register and Login<br>
        Use the provided endpoints to register and obtain a JWT token.<br>

Schedule an Email<br>
        Use the authenticated endpoint to create an email and set the desired sending time
