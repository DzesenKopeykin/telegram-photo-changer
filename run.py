from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client

from client import client


def change_photo(client: Client) -> None:
    image = Image.new("RGB", (1024, 1024), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Ubuntu-Regular.ttf", 20)
    draw.text((10, 10), "Hello World", font=font, fill=(255, 255, 255))
    
    fp = BytesIO()
    image.save(fp, "png")
    fp.name = "1.png"

    photos = client.get_profile_photos("me", limit=1)
    client.delete_profile_photos(photos[0].file_id)
    client.set_profile_photo(photo=fp)


if __name__ == "__main__":
    with client:
        change_photo(client)
