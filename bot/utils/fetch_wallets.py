from blockchain_interactions.get_wallet_info import get_info_about_wallet
from database.read_requests import get_all_wallets

def get_assets(*, user_id):
    wallets = get_all_wallets(user_id=user_id)
    assets = get_data_about_all_wallets(wallets=wallets)
    return assets

def get_data_about_all_wallets(*, wallets):
    # assets structure: [overall assets, {wallet name: [wallet overall assets, {coin: [amount, value in $]}]}]
    overall_balance = 0
    wallets_list = {}
    for wallet in wallets:
        wallet_name, wallet_address = wallet["wallet_name"], wallet["wallet_address"]
        wallet_assets = get_info_about_wallet(wallet_address=wallet_address)
        wallet_balance = wallet_assets[0]

        overall_balance += wallet_balance

        # Transform wallet_assets[1] into the expected dictionary format
        coins_dict = {}
        for asset in wallet_assets[1]:
            for name, details in asset.items():
                # Ensure details is a list with [amount, value in $]
                if isinstance(details, list) and len(details) == 2:
                    coins_dict[name] = details
                else:
                    coins_dict[name] = [details, 0]  # Default to 0 for value in $ if missing

        wallets_list[wallet_name] = [wallet_balance, coins_dict]

    return [overall_balance, wallets_list]

