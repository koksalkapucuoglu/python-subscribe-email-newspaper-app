# python-subscribe-email-newspaper-app
This project is a simple email subscription application. Here is a solution for this application using django, celery, celery-beat and rabbitmq in the backend

## Tech Stack

**Core Tech:** Python

**Backend Service:** Django, Django Rest Framework

**Database:** Postgre

**Task Management and Broker**: Celery, RabbitMQ, Redis

**Task Monitoring**: Flower

## Run Locally using Docker

Clone the project

```bash
  git clone https://github.com/koksalkapucuoglu/python-subscribe-email-newspaper-app.git
```

Go to the project directory

```bash
  cd python-subscribe-email-newspaper-app
```

Build

```bash
  docker-compose build
```

Setup database tables by running migrations

```bash
  docker-compose run --rm app python manage.py makemigrations
  docker-compose run --rm app python manage.py migrate
```

Create superuser to login Django admin panel

```bash
  docker-compose run --rm app python manage.py createsuperuser
```

Run project

```bash
  docker-compose up
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/koksalkapucuoglu/python-subscribe-email-newspaper-app.git
```

Go to the project directory

```bash
  cd python-subscribe-email-newspaper-app
```

Create python env

```bash
  python -m venv env
```

Activate enviroment

```bash
  source env/Scripts/activate
```

or

```bash
  env\Scripts\activate
```

Install requirements

```bash
  pip install -r requirements.txt
  pip install -r requirements_dev.txt
```

Detect django model changes

```bash
  python manage.py makemigrations
```

Apply django model changes

```bash
  python manage.py migrate
```

Create superuser to login Django admin panel

```bash
  python manage.py createsuperuser
```

Run django project

```bash
  python manage.py runserver
```