from bot.bot_initialization import bot
from bot.utils.menu_markups import main_menu_markup, back_to_main_menu_markup, create_delete_wallets_menu_markup
from bot.assets import Assets

class Menu:
    def __init__(self, *,  chat_id):
        self.chat_id = chat_id
    
    def show_main_menu(self):
        bot.send_photo(
        chat_id=self.chat_id,
        photo="https://img.freepik.com/premium-vector/wallet-with-money-credit-card_3482-6721.jpg",
        text=(
            "💼 *Welcome to Crypto Wallet Checker*  \n"
            "Easily track all your crypto assets in one place!  \n"
            "No logins. No stress. Just your wallet, your assets, your control. 🚀"
        ),
        reply_markup=main_menu_markup,
        parse_mode="Markdown"
        )
    
    def show_all_assets(self, *, assets_info):
        user_assets = Assets(assets_info)
        message_text = user_assets.create_assets_message()

        bot.send_message(chat_id=self.chat_id, text=message_text, reply_markup=back_to_main_menu_markup)
    
    def show_delete_wallet_menu(self, assets_info):
        user_assets = Assets(assets_info)
        delete_wallets_markup = create_delete_wallets_menu_markup(wallets=user_assets.wallets)
        message_text = "Here are all your wallets. Tap on the one you want to delete."

        bot.send_message(chat_id=self.chat_id, text=message_text, reply_markup=delete_wallets_markup)

    def delete_previous_message(self, *, message_id):
        bot.delete_message(chat_id=self.chat_id, message_id=message_id)
    
    

