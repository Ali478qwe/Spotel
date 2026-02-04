from telethon import TelegramClient, events
import yt_dlp
import os
from config import *


bot = TelegramClient(None, api_id, api_hash)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hi! I am Spotel. Send me a link to start.')

async def main():
    
    await bot.start(bot_token=bot_token)
    print("Bot is running...")
    

    await bot.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())