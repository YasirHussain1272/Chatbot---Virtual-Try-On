# Virtual Try-On Telegram Chatbot

This project implements a Telegram chatbot that allows users to virtually try on different dresses. Users can upload their own image and an image of the dress they want to try, and the chatbot will process the images using the virtual try-on API and send back the result.

## Features
- Users can send images of themselves and dresses via Telegram.
- The bot processes the images and generates a virtual try-on using the Hugging Face API.
- Interact with the bot using simple commands like `/start` or by typing "try on".
- Flask backend to handle webhooks and API integration.

## Tech Stack
- **Flask**: Used as the backend framework to serve the app and handle incoming Telegram webhook requests.
- **Telegram Bot API**: Communicates with Telegram users.
- **Hugging Face API**: Used to perform virtual try-ons.
- **Python**: Core language for the bot's implementation.

## Prerequisites

To run this project, you will need the following:
- Python 3.8+
- Telegram bot token (you can create a bot using the BotFather on Telegram)
- Hugging Face API URL for virtual try-on
- A local or cloud environment (Heroku, Railway, etc.) to deploy the Flask app

### Install Dependencies

First, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/virtual-tryon-telegram-bot.git
cd virtual-tryon-telegram-bot

# Install Python dependencies
pip install -r requirements.txt
