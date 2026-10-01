import os
import random
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

nest_asyncio.apply()

# Render-এর Environment Variable থেকে টোকেন নেওয়া হবে
TOKEN = os.environ.get("BOT_TOKEN")

# /start কমান্ডের উত্তর
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "Olymp Trade সিগন্যাল বটে আপনাকে স্বাগতম!\n"
        "ট্রেডিং সিগন্যাল পেতে /signal লিখুন।"
    )
    await update.message.reply_text(welcome_text)

# /signal কমান্ডের উত্তর
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assets = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "EUR/JPY"]
    actions = ["CALL (BUY) ⬆️", "PUT (SELL) ⬇️"]
    timeframes = ["1 Minute", "2 Minutes", "5 Minutes"]

    selected_asset = random.choice(assets)
    selected_action = random.choice(actions)
    selected_timeframe = random.choice(timeframes)

    signal_text = (
        f"📊 **Olymp Trade Signal:**\n"
        f"Asset: {selected_asset}\n"
        f"Action: {selected_action}\n"
        f"Timeframe: {selected_timeframe}"
    )
    await update.message.reply_text(signal_text, parse_mode="Markdown")

# বট অ্যাপ্লিকেশন তৈরি
app = ApplicationBuilder().token(TOKEN).build()

# কমান্ড হ্যান্ডলার যোগ করা
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)
