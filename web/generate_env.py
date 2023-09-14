import os
from django.core.management.utils import get_random_secret_key

def generate_env():
    """
    Generate default env file

    Generate file name is ".env"
    Regenerate django secret key
    """

    # Check exist .evn file
    is_exist_env_file: bool = os.path.exists('.env')
    if is_exist_env_file:
        print('Already exists ".env"')
    else:
        secret_key: str = get_random_secret_key()
        writelines: list[str] = [
            'ALLOWED_HOSTS=*\n'
            f'SECRET_KEY={secret_key}'
        ]
        with open('.env', mode='w', newline='\n') as f:
            f.writelines(writelines)

if __name__ == "__main__":
    generate_env()