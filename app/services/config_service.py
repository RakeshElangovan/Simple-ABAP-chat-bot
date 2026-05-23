import os
from dotenv import load_dotenv


load_dotenv()


class ConfigService:

    @staticmethod
    def get(key, default=None):
        return os.getenv(key, default)
