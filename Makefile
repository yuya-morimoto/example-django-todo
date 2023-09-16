h:
	cat Makefile
b:
	docker-compose --profile setup build && \
	docker-compose --profile local build
u_setup:
	docker-compose --profile setup up --remove-orphans
u_local:
	docker-compose --profile local up --remove-orphans
b_u_local:
	docker-compose --profile local up --remove-orphans --build
start_local:
	docker exec -it dj-todo-web /bin/bash -c "poetry run task start_local"
in_web:
	docker exec -it dj-todo-web /bin/bash