from bot.bot_initialization import bot
from bot.utils.menu_markups import back_to_main_menu_markup, create_delete_wallets_menu_markup
from bot.utils.show_main_menu import show_main_menu
from bot.utils.fetch_wallets import get_assets
from bot.utils.wallet_creation import create_wallet
from bot.assets import Assets
from database.read_requests import get_all_wallets


class Menu:
    def __init__(self, *,  chat_id, user_id):
        self.chat_id = chat_id
        self.user_id = user_id
    
    def show_main_menu(self):
        show_main_menu(chat_id=self.chat_id)
    
    def show_all_assets(self):
        user_wallets = get_all_wallets(user_id=self.user_id)
        if not user_wallets:
            bot.send_message(
                chat_id=self.chat_id,
                text="Ooops You don't have wallets yet",
                reply_markup=back_to_main_menu_markup
            )
        else:
            user_assets = Assets(all_assets=get_assets(user_id=self.user_id))
            message_text = user_assets.create_assets_message()
            bot.send_message(chat_id=self.chat_id, text=message_text, reply_markup=back_to_main_menu_markup)   
    
    def show_delete_wallet_menu(self):
        user_wallets = get_all_wallets(user_id=self.user_id)
        if not user_wallets:
            bot.send_message(
                chat_id=self.chat_id,
                text="Ooops You don't have wallets yet",
                reply_markup=back_to_main_menu_markup
            )
        else:
            user_assets = Assets(all_assets=get_assets(user_id=self.user_id))
            delete_wallets_markup = create_delete_wallets_menu_markup(wallets=user_assets.wallets)
            message_text = "Here are all your wallets. Tap on the one you want to delete."
            bot.send_message(chat_id=self.chat_id, text=message_text, reply_markup=delete_wallets_markup)

    def delete_previous_menu(self, *, message_id):
        bot.delete_message(chat_id=self.chat_id, message_id=message_id)
    
    def show_wallet_creation_start_message(self):
        message = bot.send_message(chat_id=self.chat_id, text="Please, send your wallet address")
        bot.register_next_step_handler(message, create_wallet)

