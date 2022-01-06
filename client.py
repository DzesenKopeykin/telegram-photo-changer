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


@client.on_message()
def message_handler(client: Client, message: Message) -> None:
    if message.from_user.is_self:
        return
    client.send_message(
        chat_id=message.chat.id, reply_to_message_id=message.message_id, text="😜"
    )
