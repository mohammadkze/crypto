import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Settings:
    API_URL = os.getenv("API_URL")
    API_KEY = os.getenv("API_KEY")

settings = Settings()
