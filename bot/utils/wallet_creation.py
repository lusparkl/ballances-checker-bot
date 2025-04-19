from bot.utils.get_client_data import get_chat_id, get_user_id
from bot.utils.show_main_menu import show_main_menu
from bot.bot_initialization import bot
from database.write_requests import add_new_wallet


def create_wallet(message):
    wallet_address = message.text
    chat_id = get_chat_id(message)

    message = bot.send_message(chat_id=chat_id, text="Great! Now send name for your wallet:")
    bot.register_next_step_handler(message, get_wallet_name, wallet_address)

def get_wallet_name(message, wallet_address):
    wallet_name = message.text
    add_wallet(wallet_info=[wallet_name, wallet_address], message=message)
    

def add_wallet(*, wallet_info, message):
    wallet_name, wallet_address = wallet_info
    user_id = get_user_id(message=message)
    add_new_wallet(wallet_address=wallet_address, wallet_name=wallet_name, user_id=user_id)
    
    chat_id = get_chat_id(message=message)
    bot.send_message(chat_id=chat_id, text=f"Sucesfully added wallet {wallet_name} to your wallets🎉. Now you can see wallet assets in all assets.")
    show_main_menu(chat_id=chat_id)