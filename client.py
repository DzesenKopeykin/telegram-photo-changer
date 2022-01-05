from pyrogram import Client
from pyrogram.types import Message

from settings import TELEGRAM_API_HASH, TELEGRAM_API_ID


client = Client("telegram_client", TELEGRAM_API_ID, TELEGRAM_API_HASH)


@client.on_message()
def message_handler(client: Client, message: Message) -> None:
    if message.from_user.is_self:
        return
    client.send_message(
        chat_id=message.chat.id, reply_to_message_id=message.message_id, text="😜"
    )


client.run()
