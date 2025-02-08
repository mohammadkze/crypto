import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_URL = os.getenv("API_URL", "https://sandbox-api.coinmarketcap.com")
    API_KEY = os.getenv("API_KEY")

settings = Settings()
