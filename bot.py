from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '🤖 Bot is alive!'

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# تشغيل الخادم Flask في الخلفية
threading.Thread(target=run_flask).start()


import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from google_sheets import send_to_sheet
from filter import is_safe_message, extract_info

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "7586526524:AAEcET6XF4gLsS9LcUXSMX42o89o0c9B7LE"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if not is_safe_message(text):
        await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
        return

    data = extract_info(text)
    if data:
        send_to_sheet(data)
    else:
        await update.message.reply_text("⚠️  يرجى التأكد من رقم رخصة فال او اكتب (طلب) في رسالت اعلانك.")
        await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
