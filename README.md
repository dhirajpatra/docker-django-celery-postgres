
# Docker based Django Celery Redis PostgreSql Application

## Overview

This is a demo application developed to explain how celery work with Django and PostgreSql as database. I have to used Redis as well as Nginx for reverse proxy. I kept the whole application inside Docker with microservices architecture so that you can run and further develop easily without any constraint of your local environment.

It just create a simple task and to calculate the result takes it as background job by celery. So when it is available and upadted into the postgresql database. Next API call would display the result.

Folder structure:

One level
.
├── README.md
├── backend
├── docker
├── docker-compose.yml
└── requirements.txt

two level

```
.
├── README.md
├── backend
│   ├── assignments
│   ├── backend
│   ├── db.sqlite3
│   └── manage.py
├── docker
│   ├── backend
│   └── nginx
├── docker-compose.yml
└── requirements.txt


three level


├── README.md
├── backend
│   ├── assignments
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── admin.cpython-311.pyc
│   │   │   ├── apps.cpython-311.pyc
│   │   │   ├── models.cpython-311.pyc
│   │   │   ├── serializers.cpython-311.pyc
│   │   │   ├── tasks.cpython-311.pyc
│   │   │   ├── urls.cpython-311.pyc
│   │   │   └── views.cpython-311.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tasks.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── backend
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── celery.cpython-311.pyc
│   │   │   ├── settings.cpython-311.pyc
│   │   │   ├── urls.cpython-311.pyc
│   │   │   └── wsgi.cpython-311.pyc
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   └── manage.py
├── docker
│   ├── backend
│   │   ├── Dockerfile
│   │   ├── server-entrypoint.sh
│   │   └── worker-entrypoint.sh
│   └── nginx
│       └── default.conf
├── docker-compose.yml
└── requirements.txt

```

## Technologies Used

- Python
- Django
- Celery
- Redis
- PostgreSQL
- Nginx
- Docker

## Prerequisites

- Docker and Docker Compose installed
- Basic understanding of Python and Django

## Getting Started

1. Fork or Clone the repository:

   ```bash
   git clone https://github.com/dhirajpatra/docker-django-celery-postgres
   ```

2. Create a `.env` file:
   - Copy the `.env.example` file to `.env`.
   - Fill in the necessary environment variables.

3. Start the application:

   ```bash
   docker-compose up -d
   ```

4. Access the application:
   - Visit `http://localhost:80` in your browser (or the specified port).

## Project Structure

- Explain the main directories and files in your project.

## Running Celery Worker

- Start the worker:

   ```bash
   docker-compose exec app celery -A <your_app_name> worker -l info
   ```

## Monitoring Celery Tasks (Optional):

- If using Flower:
  - Access Flower dashboard: `http://localhost:5555`

## Running Tests

- Yet to complete the test suite.

## Contributing

- You can fork this repo and update in your repo. After that you can make a pull request to merge with this repo.

## Troubleshooting

- Continue working on it. If you found any kindly let me know.

## Additional Notes

- There are plenty of online articles some of them you can find in my free blog as well https://dhirajpatra.blogspot.com to learn Django, Redis, Postgresql, Nginx and Docker. Lets begin :)

## License

- MIT.
