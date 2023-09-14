h:
	cat Makefile
b:
	docker-compose build
u_setup:
	docker-compose --profile setup up --remove-orphans
u_local:
	docker-compose --profile local up --remove-orphans
in_web:
	docker exec -it dj-todo-web /bin/bash