class Assets:
    # assets structure: [overall assets, {wallet name: [wallet overall assets, {coin: [ammount, value in $]}]}]
    def __init__(self, *, all_assets):
        self.overall_balance = all_assets[0]
        self.wallets = all_assets[2]
    
    def create_assets_message(self):
        text =(
        f"This is your assets: \n"
        "*{user_assets.overall_balance}*$ \n \n"
        )
        for wallet in self.wallets:
            wallet_name = wallet[0]
            wallet_text = f"{wallet_name} \n"
            
            wallet_coins = wallet[1]
            for name, asset_data in wallet_coins.items:
                ammount = asset_data[0]
                price = asset_data[1]
                wallet_text += f"{name} : {ammount}   {price}$ \n"
    
        return text