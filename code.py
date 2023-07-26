import asyncio
from pyrogram import Client

api_id = 19394864
api_hash = "ffe2782108803dfc5fc84043266419a8"


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
