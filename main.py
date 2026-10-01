import os
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

nest_asyncio.apply()

# Environment variable থেকে টোকেন নেওয়া হবে
TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olymp Trade সিগন্যাল বটে আপনাকে স্বাগতম! ট্রেডিং সিগন্যাল পেতে /signal লিখুন।")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 **Olymp Trade Signal:**\nAsset: EUR/USD\nAction: CALL (BUY) ⬆️️\nTimeframe: 1 Minute")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)
