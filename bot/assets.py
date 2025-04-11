class Assets:
    # assets structure: [overall assets, {wallet name: [wallet overall assets, {coin: [ammount, value in $]}]}]
    def __init__(self, *, all_assets):
        self.overall_balance = all_assets[0]
        self.wallets = all_assets[2]
    
    