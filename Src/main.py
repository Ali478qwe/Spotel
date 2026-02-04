
from telegram import Update
from telegram.ext import (ApplicationBuilder , CommandHandler , ContextTypes
                           , MessageHandler , filters) 
from config import BOT_TOKEN
from link_finder import *
import re


async def start(update : Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi Im Spotel Send me a link to start")



async def process_link(update : Update,context : ContextTypes.DEFAULT_TYPE):
    message = update.message
    text = message.text
    user_id = message.from_user.id
    result = find_link(text)
    if result == link_t.MoreOneLink:
        await message.reply_text("just sent one link🔗")
    elif result == link_t.Null:
        await message.reply_text("This link wasnt recognized❌")
    elif result == link_t.LinkNotfound:
        await message.reply_text("link not found🗿")
    else:
        await message.reply_text(f"you send link?\n{user_id}✔\n{result}")


    


bot = ApplicationBuilder().token(BOT_TOKEN).build()

def main():
    bot.add_handler(CommandHandler("start",start))
    bot.add_handler(MessageHandler(filters.TEXT,process_link))
    bot.run_polling()

if __name__ == "__main__":
    main()


