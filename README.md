# Rick and Morty Character API

## Description

This project is a Django-based REST API service that synchronizes and serves character data from the Rick and Morty
show. It utilizes the official Rick and Morty GraphQL API as a data source and implements asynchronous data fetching
using Celery for periodic updates.

## Features

- Automatic synchronization with the Rick and Morty API
- REST API endpoints for character data
- Random character selection endpoint
- Asynchronous task processing with Celery
- Task monitoring with Flower
- Docker containerization

## Tech Stack

- Python 3.11
- Django
- Django REST Framework
- Celery
- Flower
- PostgreSQL
- Redis
- Docker & Docker Compose
- httpsx for async API requests

## Installation

### Using Docker

1. Clone the repository:

```bash
git clone https://github.com/zave52/rick-and-morty.git
cd rick_and_morty_api
```

2. Create .env from .env.sample file in the project root and configure your environment variables:

```bash
DEBUG=True
SECRET_KEY=your-secret-key
POSTGRES_DB=rick_and_morty
POSTGRES_USER=your-username
POSTGRES_PASSWORD=your-password
POSTGRES_HOST=db
POSTGRES_PORT=5432
CELERY_BROKER_URL=your-redis-url
CELERY_RESULT_BACKEND=your-redis-url
```

3. Build and run the containers:

```bash
docker-compose up --build
```

4. Create admin user & Create schedule for running sync in DB
