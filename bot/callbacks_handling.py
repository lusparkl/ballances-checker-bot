from bot.bot_initialization import bot
from bot.utils.get_client_data import get_user_id, get_chat_id, get_message_id
from bot.menu import Menu
from bot.utils.fetch_wallets import get_assets

@bot.callback_query_handler()
def handle_callbacks(call):
    call_suitable_function(call)

def call_suitable_function(call):
    callback_value = call.data
    user_id = get_user_id(call.message)
    chat_id = get_chat_id(call.message)
    message_id = get_message_id(call.message)
    menu = Menu(chat_id=chat_id)

    match callback_value:
        case "assets":
            menu.delete_previous_message(message_id=message_id)
            menu.show_all_assets(assets_info=get_assets(user_id=user_id))
        case "add wallet":
            pass
        case "delete wallet":
            menu.show_delete_wallet_menu(assets_info=get_assets(user_id=user_id))
        case "back to main menu":
            menu.show_main_menu()
