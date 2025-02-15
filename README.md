# rick-and-morty

### How to run:
- Create venv: `python -m venv venv`
- Activate it: `source venv/bin/activate`
- Install requirements: `pip install -r requirements.txt`
- Run migrations: `python manage.py migrate`
- Run Redis Server: `docker run -d -p 6379:6379 redis`
- Run celery worker for tasks handling: `celery -A rick_and_morty_api worker -l INFO`
- Run celery beat for task scheduling: `$(cat .env | grep -v '^#' | xargs) && celery -A rick_and_morty_api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
- Create schedule for running sync in DB
- Run app: `python manage.py runserver`