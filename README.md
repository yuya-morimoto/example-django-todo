![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/zero-hack-org/example-django-todo)
![GitHub repo size](https://img.shields.io/github/repo-size/zero-hack-org/example-django-todo)
<br/>
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
<br/>
![Twitter Follow](https://img.shields.io/twitter/follow/y_morimoto_dev?style=social)

## example-django-todo

Django4.2 example todo application

### Usage

#### 1. Build container

```bash
# or make b
ocker-compose --profile setup build && docker-compose --profile local build
```

#### 2. Generate .env

```bash
# or make u_setup
docker-compose --profile setup up --remove-orphans
```

#### 3. Up container

```bash
# or make u_local
docker-compose --profile local up --remove-orphans
```

### 4. DB migrate & Create super user

```bash
docker exec -it dj-todo-web /bin/bash -c "poetry run python manage.py migrate"

docker exec -it dj-todo-web /bin/bash -c "poetry run createsuperuser"
```

### 4. Start local server

```bash
# or make start_local
docker exec -it dj-todo-web /bin/bash -c "poetry run task start_local"
```

### Useful links

- Discuss code changes of project via [yuya-morimoto@zero-hack.jp](yuya-morimoto@zero-hack.jp).

### License

This project is licensed under the Apache-2.0 License, see the [LICENSE](./LICENSE) file for details
