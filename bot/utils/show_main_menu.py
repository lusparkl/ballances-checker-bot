from bot.bot_initialization import bot
from bot.utils.menu_markups import main_menu_markup

def show_main_menu(*, chat_id):
    bot.send_photo(
        chat_id=chat_id,
        photo="https://img.freepik.com/premium-vector/wallet-with-money-credit-card_3482-6721.jpg",
        caption=(
            "💼 *Welcome to Crypto Wallet Checker*  \n"
            "Easily track all your crypto assets in one place!  \n"
            "No logins. No stress. Just your wallet, your assets, your control. 🚀"
        ),
        reply_markup=main_menu_markup,
        parse_mode="Markdown"
        )