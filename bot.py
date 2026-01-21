import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("✅ Bot is running")

def main():
    if not TOKEN:
        print("❌ BOT_TOKEN not found")
        return

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    print("🤖 Bot started")
    updater.idle()

if __name__ == "__main__":
    main()
