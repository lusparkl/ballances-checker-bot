import telebot
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(token)