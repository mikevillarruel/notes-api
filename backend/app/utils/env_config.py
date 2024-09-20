import os


class EnvConfig:
    DB_URL: str = os.getenv('DB_URL', '').strip()
