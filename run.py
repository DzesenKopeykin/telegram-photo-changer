import os

from dotenv import load_dotenv


if __name__ == "__main__":
    print("Running...")

    load_dotenv(".env")
    print(os.environ["TELEGRAM_API_ID"])
