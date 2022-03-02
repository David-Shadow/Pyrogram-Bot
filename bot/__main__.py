import os
import logging
import logging.config
from shutil import rmtree

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN
)
plugins = dict(root="bot/plugins")

class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name="bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers = 50,
            plugins=plugins
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username
        logging.info(f"{me.first_name} started with Pyrogram v{__version__} (Layer {layer}) started on @{me.username}.")

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")


app = Bot()
app.run()
