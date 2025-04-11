from telebot.util import quick_markup

main_menu_markup = quick_markup({
    "My assets": {"callback_data": "assets"},
    "Add wallet": {"callback_data": "add wallet"},
    "Delete wallet": {"callback_data": "delete wallet"}
})

back_to_main_menu_markup = quick_markup({"Back": {"callback_data": "back to main menu"}})

def create_delete_wallets_menu_markup(*, wallets):
    buttons_data = {}
    for name in wallets.keys():
        buttons_data[name] = {"callback_data": f"delete user wallet {name}"}
    markup = quick_markup(buttons_data)

    return markup