from pyrogram import Client
from pyrogram.types import Message

import settings


client = Client(
    session_name=settings.SESSION_NAME,
    workdir=settings.SESSION_DIR,
    api_id=settings.TELEGRAM_API_ID,
    api_hash=settings.TELEGRAM_API_HASH,
    phone_number=settings.SESSION_PHONE,
)
