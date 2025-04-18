from blockchain_interactions.get_wallet_info import get_info_about_wallet
from database.read_requests import get_all_wallets

def get_assets(*, user_id):
    wallets = get_all_wallets(user_id=user_id)
    assets = get_data_about_all_wallets(wallets=wallets)
    return assets

def get_data_about_all_wallets(*, wallets):
    # assets structure: [overall assets, {wallet name: [wallet overall assets, {coin: [ammount, value in $]}]}]
    overall_balance = 0
    wallets_list = {}
    for wallet in wallets:
        wallet_name, wallet_address = wallets[0], wallets[1]
        wallet_assets = get_info_about_wallet(wallet_address=wallet_address)
        wallet_balance = wallet_assets[0]

        overall_balance += wallet_balance
        wallets_list[wallet_name] = wallet_assets

    return [overall_balance, wallets_list]

