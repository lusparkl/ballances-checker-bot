from bot.bot_initialization import bot
from bot.utils.get_client_data import get_user_id

@bot.callback_query_handler()
def handle_callbacks(call):
    call_suitable_function(call)

def call_suitable_function(call):
    callback_value = call.data
    user_id = get_user_id(call.message)

    match callback_value:
        case "assets":
            pass
        case "add wallet":
            pass
        case "all wallets":
            pass
        case "delete wallet":
            pass

def show_user_assets(*, chat_id, user_id):
    assets = get_all_user_assets(user_id)
    pass

def get_all_user_assets(user_id):
    pass

def add_new_wallet(user_id):
    pass

def show_all_user_wallets(user_id):
    pass

def delete_user_wallet(user_id):
    pass