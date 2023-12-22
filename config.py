import os
from dotenv import load_dotenv

load_dotenv()


class TestConstants:
    BASE_URL = "https://api.sportradar.us/nfl/official"
    ACCESS_LEVEL = "trial"
    VERSION = "v7"
    LANGUAGE_CODE = "en"
    FORMAT = "json"
    API_KEY = f'{os.environ.get("APIKEY")}'
    MONGODB_URL = f"{os.environ.get('MONGODB_URL')}"
    MONGODB_DATABASE = f"{os.environ.get('MONGODB_DATABASE')}"
