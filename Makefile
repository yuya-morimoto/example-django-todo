h:
	cat Makefile
b:
	docker-compose build
u:
	docker-compose up
in_web:
	docker exec -it dj-todo-web /bin/bash