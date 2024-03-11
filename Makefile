
# ---------- pip ----------
pip-env:
	python3.10 -m venv .venv

pip-freeze:
	pip freeze -l > requirements.txt

pip-install:
	pip install -r requirements.txt

# ---------- app ----------
development-services:
	docker-compose -f ./devops/services/docker-compose.services.yml up -d

development-server:
	flask --app src.main run --host=0.0.0.0 --port=7000 --debug
# ---------- alembic ----------
a-init:
	alembic init migrations

a-revision:
	alembic revision --autogenerate -m "$(M)"

a-upgrade:
	alembic upgrade head