
from telegram import Update
from telegram.ext import (ApplicationBuilder , CommandHandler , ContextTypes
                           , MessageHandler , filters) 
from config import BOT_TOKEN
import re

async def start(update : Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi Im Spotel Send me a link to start")

def find_link(text):
    if not text:
        return False
    
    links = re.findall(r"https?://\S+",text)

    if len(links) != 1:
        return -1
    
    link = links[0]

    return link.strip()


async def process_link(update : Update,context : ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    message = update.message
    text = message.text
    result = find_link(text)
    if result == -1:
        await message.reply_text("just sent one link🔗")
    elif result.isalpha():
        await message.reply_text(f"you send link?\n{user_id}✔\n{result}")
    else:
        await message.reply_text("This link wasnt recognized❌")

    


bot = ApplicationBuilder().token(BOT_TOKEN).build()

def main():
    bot.add_handler(CommandHandler("start",start))
    bot.add_handler(MessageHandler(filters.TEXT,process_link))
    bot.run_polling()

if __name__ == "__main__":
    main()


