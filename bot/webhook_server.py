import os
from flask import Flask, request
import telebot

# Load env first
TOKEN = os.getenv("BOT_TOKEN")

from bot.bot_initialization import bot
import bot.commands
import bot.callbacks_handling

app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "ok", 200

@app.route("/health", methods=["GET"])
def health():
    return "OK", 200