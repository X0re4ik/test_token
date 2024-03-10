# 
development-services:
	docker-compose -f ./devops/services/docker-compose.services.yml up -d



a-init:
	alembic init migrations

a-revision:
	alembic revision --autogenerate -m "$(M)"

a-upgrade:
	alembic upgrade head