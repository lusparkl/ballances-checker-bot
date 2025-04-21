import bot.commands
import bot.callbacks_handling
from bot.bot_initialization import bot
from flask import Flask, request
import telebot
import os

app = Flask(__name__)
TOKEN = os.getenv("BOT_TOKEN")

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "ok", 200