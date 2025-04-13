from bot.bot_initialization import bot
from bot.menu import Menu

@bot.message_handler(commands=["start"])
def start_bot(message):
    pass