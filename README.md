
# Docker based Django Celery Redis PostgreSql Application

## Overview

This is a demo application developed to explain how celery work with Django and PostgreSql as database. I have to used Redis as well as Nginx for reverse proxy. I kept the whole application inside Docker with microservices architecture so that you can run and further develop easily without any constraint of your local environment.

It just create a simple task and to calculate the result takes it as background job by celery. So when it is available and upadted into the postgresql database. Next API call would display the result.

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

- Outline guidelines for contributing to the project.

## Troubleshooting

- Address common issues and their solutions.

## Additional Notes

- Provide any further tips or considerations for beginners.

## License

- State the project's license.
