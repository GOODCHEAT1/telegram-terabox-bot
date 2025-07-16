import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from terabox_api import TeraBoxClient
import os
from dotenv import load_dotenv

load_dotenv()

TERABOX_EMAIL = os.getenv("TERABOX_EMAIL")
TERABOX_PASS = os.getenv("TERABOX_PASS")
BOT_TOKEN = os.getenv("BOT_TOKEN")

client = TeraBoxClient(TERABOX_EMAIL, TERABOX_PASS)

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to TeraBox Bot!")

async def list_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    files = client.list_files()
    reply = "\n".join([f"{f['name']} (ID: {f['id']})" for f in files])
    await update.message.reply_text(reply or "📂 No files found.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("list", list_files))

app.run_polling()
