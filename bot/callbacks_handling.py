from bot.bot_initialization import bot
from bot.utils.get_client_data import get_user_id, get_chat_id, get_message_id
from bot.menu import Menu
from bot.utils.fetch_wallets import get_assets
from database.read_requests import get_all_wallets
from database.write_requests import delete_wallet

@bot.callback_query_handler()
def handle_callbacks(call):
    call_suitable_function(call)

def call_suitable_function(call):
    callback_value = call.data
    user_id = get_user_id(message=call)
    chat_id = get_chat_id(message=call.message)
    message_id = get_message_id(message=call.message)
    
    
    menu = Menu(chat_id=chat_id, user_id=user_id)

    match callback_value:
        case "assets":
            menu.delete_previous_menu(message_id=message_id)
            menu.show_all_assets()
        case "add wallet":
            menu.delete_previous_menu(message_id=message_id)
            menu.show_wallet_creation_start_message()
        case "delete wallet":
            menu.delete_previous_menu(message_id=message_id)
            menu.show_delete_wallet_menu()
        case "back to main menu":
            menu.delete_previous_menu(message_id=message_id)
            menu.show_main_menu()
        case _:
            menu.delete_previous_menu(message_id=message_id)
            delete_wallet(wallet_name=callback_value, user_id=user_id)
            menu.show_main_menu()

