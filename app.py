import os
from flask import Flask, render_template, request, jsonify
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

app = Flask(__name__)

# Replace with your Telegram Bot token
TELEGRAM_BOT_TOKEN = 'AAGRqkzh87gqsXA_PN3JGVaCiMoysM0eW6M'
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Define your try-on API URL
tryon_api_url = "https://huggingface.co/spaces/Nymbo/Virtual-Try-On"  # Ensure this URL is correct

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Your existing upload function code...
    return jsonify({'success': True, 'message': 'Image uploaded successfully!'})

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle incoming Telegram updates."""
    update = Update.de_json(request.get_json(force=True), bot)
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    application.process_update(update)
    return 'ok'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Welcome! Send me the image of yourself followed by the image of the dress you'd like to try on.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages."""
    incoming_msg = update.message.text
    chat_id = update.message.chat.id

    if 'try on' in incoming_msg.lower():
        await context.bot.send_message(chat_id, "Please send me the image of yourself followed by the image of the dress you'd like to try on.")
    else:
        await context.bot.send_message(chat_id, "Sorry, I didn't understand that. Please say 'try on' to get started.")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle photo uploads."""
    chat_id = update.message.chat.id
    photo_file = update.message.photo[-1].get_file()
    
    # Download the photo
    photo_path = f'./photos/{chat_id}.jpg'
    await photo_file.download(photo_path)

    # Here you can call your try-on logic with the downloaded photo
    await context.bot.send_message(chat_id, "Processing your try-on request. Please wait.")
    
    # Add your logic to handle the try-on with the downloaded image
    # Example: Call your upload or try-on logic here

# Create the application and add handlers
application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

if __name__ == '__main__':
    app.run(debug=True)
