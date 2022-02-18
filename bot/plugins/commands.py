import os
import logging

logger = logging.getLogger(__name__)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import FloodWait

from config import LOG_CHAT, ADMINS

#################### Start Message #################### 
@Client.on_message(filters.command(["start"]) & filters.private &~ filters.edited)
async def start_cmd(bot, cmd):
    ment = cmd.from_user.mention
    txt = f'Hey {ment}!\nThis is a basic Pyrogram Bot developed by @DavidCordona'
    buttons = [
        [
            InlineKeyboardButton("「🧑‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 🧑‍💻」", url = "https://t.me/DavidCordona")
        ],
        [
            InlineKeyboardButton("「💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 💬」", url = "https://t.me/TPE_Discussion")
        ]
    ]
    await cmd.reply(
        text = txt,
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True
    )

#################### Upload Logs File ####################
@Client.on_message(filters.command(["logs", "log"]) & filters.user(ADMINS) &~ filters.edited)
async def upload_logs(bot, cmd):
    try:
        await cmd.reply_document('Logs.log', quote = True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
    except Exception as e:
        await cmd.reply(str(e))

#################### Help Command ####################
@Client.on_message(filters.command(["help"]) & filters.private &~ filters.edited)
async def help_cmd(bot, cmd):
    txt = 'All available commands are:
    txt += '\n/start - start the bot'
    txt += '\n/logs, /log - [only for ADMINS]'
    txt += '\n/help - get this message'
    await cmd.reply(txt, quote = True)



