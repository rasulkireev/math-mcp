serve:
	docker-compose up -d --build
	docker compose logs -f backend
