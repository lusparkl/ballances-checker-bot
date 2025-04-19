class Assets:
    # assets structure: [overall assets, {wallet name: [wallet overall assets, {coin: [ammount, value in $]}]}]
    def __init__(self, *, all_assets):
        self.overall_balance = round(all_assets[0], 3)
        self.wallets = all_assets[1]
    
    def create_assets_message(self):
        text = (
            f"This is your assets: \n"
            f"{self.overall_balance}$ \n \n"
        )
        for wallet_name, wallet_data in self.wallets.items():
            wallet_text = f"{wallet_name} \n"

            wallet_overall_balance = round(wallet_data[0], 3)  # Extract and round the overall balance for the wallet
            wallet_text += f"Overall balance: {wallet_overall_balance}$\n \n"

            wallet_coins = wallet_data[1]  # Extract the coins dictionary
            for name, asset_data in wallet_coins.items():
                if name == "value_in_usd":
                    name = "value in usd"
                    value = asset_data[0] 
                    value = round(value, 3)
                    wallet_text += f"{name} : {value}$\n \n"
                else:
                    value = asset_data[0]
                    wallet_text += f"{name} : {value}\n"

            text += wallet_text + "\n"

        return text