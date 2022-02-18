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
    BOT_TOKEN,
    LOG_CHAT
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
        try:
            startmsg = await self.send_message(
                           chat_id=LOG_CHAT,
                           text='**Bot started🥳.**',
                           parse_mode = 'md'
                       )
            await startmsg.pin()
        except Exception as e:
            logging.exception(f"Error in sending message to log chat: {e}")
            pass

    async def stop(self, *args):
        logging.info("Bot stopped. Bye.")
        try:
            msg = await self.send_message(
                           chat_id=LOG_CHAT,
                           text='**Bot stopped!.**',
                           parse_mode = 'md'
                       )
            await msg.pin()
        except Exception as e:
            logging.exception(f"Error in sending message to log chat: {e}")
        await super().stop()


app = Bot()
app.run()
