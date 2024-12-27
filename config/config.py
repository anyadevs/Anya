import os
from pathlib import Path

class Config:
    APP_NAME = "AI Agent"
    VERSION = "1.0"

    API_KEY = os.getenv("API_KEY", "your_default_api_key")
    API_BASE_URL = "https://api.example.com"

    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/agent.db")
    DATA_DIR = Path("data")
    DATASETS_DIR = DATA_DIR / "datasets"

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    @staticmethod
    def ensure_directories_exist():
        Config.DATA_DIR.mkdir(exist_ok=True)
        Config.DATASETS_DIR.mkdir(exist_ok=True)
