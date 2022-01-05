import os

from dotenv import load_dotenv
from pyrogram import Client


if __name__ == "__main__":
    print("Running...")

    load_dotenv(".env")
    api_id = os.environ["TELEGRAM_API_ID"]
    api_hash = os.environ["TELEGRAM_API_HASH"]

    with Client("telegram_client", api_id, api_hash) as client:
        client.send_message("me", "Hi!!!")
