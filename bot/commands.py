from bot.bot_initialization import bot
from bot.menu import Menu
from bot.utils.get_client_data import get_chat_id, get_user_id 
from database.read_requests import is_user_exists
from database.write_requests import add_new_user

@bot.message_handler(commands=["start"])
def start_bot(message):
    chat_id = get_chat_id(message=message)
    user_id = get_user_id(message=message)
    if not is_user_exists(user_id=user_id):
        add_new_user(user_id=user_id)
    menu = Menu(chat_id=chat_id, user_id=user_id)
    menu.show_main_menu()