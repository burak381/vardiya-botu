import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Merhaba! 👋\n"
        "Ben vardiya botuyum.\n\n"
        "Şimdilik çalışıyorum. Vardiya sistemi birazdan eklenecek."
    )

async def bugun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 Bugünün vardiya bilgisi henüz yüklenmedi."
    )

def main():
    token = os.environ.get("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN bulunamadı!")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bugun", bugun))

    print("Bot çalışıyor...")
    app.run_polling()

if __name__ == "__main__":
    main()
