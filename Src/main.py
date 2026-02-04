from telegram import Update
from telegram.ext import ApplicationBuilder , CommandHandler , ContextTypes
from config import BOT_TOKEN

async def start(update : Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi Im Spotel Send me a link to start")

bot = ApplicationBuilder().token(BOT_TOKEN).build()


bot.add_handler(CommandHandler("start",start))

bot.run_polling()