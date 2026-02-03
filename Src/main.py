from telethon import TelegramClient,events
from config import *
import yt_dlp
import os

bot = TelegramClient('Spotel',api_id,api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage(pattern='/start'))
async def start(events):
    await events.respond('Hi Im Spotel Lets Start send link')

