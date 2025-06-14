import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from google_sheets import send_to_sheet
from filter import is_safe_message, extract_info

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "7586526524:AAEcET6XF4gLsS9LcUXSMX42o89o0c9B7LE"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    chat_id = update.message.chat_id
    message_id = update.message.message_id

    if not is_safe_message(text):
        # حذف الرسالة الأصلية أولاً
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        # إرسال رسالة الرفض
        await context.bot.send_message(
            chat_id=chat_id,
            text="🚫 هذا الإعلان غير مسموح به وتم حذفه.",
            reply_to_message_id=message_id
        )
        return

    data = extract_info(text)
    if data:
        send_to_sheet(data)
        await update.message.reply_text("✅ تم استلام إعلانك العقاري بنجاح.")
    else:
        await update.message.reply_text("⚠️ يرجى التأكد من تنسيق الرسالة.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
