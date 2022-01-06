import os

from dotenv import load_dotenv


load_dotenv(".env")

# Telegram app
TELEGRAM_API_ID = os.environ["TELEGRAM_API_ID"]
TELEGRAM_API_HASH = os.environ["TELEGRAM_API_HASH"]

# Telegram session
SESSION_DIR = os.getenv("SESSION_DIR", "sessions/")
SESSION_NAME = os.getenv("SESSION_NAME", "telegram_client")
SESSION_PHONE = os.getenv("SESSION_PHONE")
