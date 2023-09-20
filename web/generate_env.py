import os

from django.core.management.utils import get_random_secret_key


def generate_env() -> None:
    """
    Generate default env file

    Generate file name is ".env"
    Regenerate django secret key
    """

    # Check exist .evn file
    is_exist_env_file: bool = os.path.exists(".env")
    if is_exist_env_file:
        print('Already exists ".env"')
    else:
        secret_key: str = get_random_secret_key()
        writelines: list[str] = [
            "ALLOWED_HOSTS=*\n",
            "INTERNAL_IPS=127.0.0.1",
            f"SECRET_KEY={secret_key}\n",
            "\n",
            "# Database\n",
            "DB_NAME=db\n",
            "DB_USER=admin\n",
            "DB_PASSWORD=password\n",
            "DB_HOST=dj-todo-db\n",
            "DB_PORT=5432",
            "\n",
            "# Redis\n",
            "REDIS_LOCATION=redis://redis:6379",
        ]
        with open(".env", mode="w", newline="\n") as f:
            f.writelines(writelines)


if __name__ == "__main__":
    generate_env()
