# Notes + Health (Django)

A tiny but production-like Django app to learn DevOps deployment:
- Auth (login/logout)
- Private notes CRUD
- `/status` health endpoint (DB check + version)
- Admin panel

## Quickstart (local)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# edit SECRET_KEY (required for prod), DEBUG, ALLOWED_HOSTS if you want

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit:
- Notes: http://127.0.0.1:8000/
- Status: http://127.0.0.1:8000/status
- Admin: http://127.0.0.1:8000/admin/

## Postgres (optional)

Set `DATABASE_URL` in `.env` like:

`postgres://USER:PASSWORD@HOST:5432/DBNAME`

Then run migrations again:
```bash
python manage.py migrate
```

## Deployment-ready bits included
- `gunicorn` dependency
- Environment-driven settings (DEBUG, ALLOWED_HOSTS, SECRET_KEY, DATABASE_URL)
- Static files setup (`collectstatic`)
