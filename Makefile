setup:
	pip install -r requirements.txt
docker-run:
	docker-compose -f infra/docker/docker-compose.yml up
docker-destroy:
	docker-compose -f infra/docker/docker-compose.yml down --remove-orphans
	docker-compose -f infra/docker/docker-compose.yml rm -f
docker-build:
	docker-compose -f infra/docker/docker-compose.yml build