import requests

def get_info_about_wallet(*, wallet_address) -> list[int, list]:
    url = f"https://production-api.mobula.io/api/1/wallet/portfolio?wallet={wallet_address}"

    try:
        responce = requests.get(url)
        data = responce.json()
        tokens = data["data"]["assets"]
        
        if not tokens:
            return None

        total_balance =  data["data"]["total_wallet_balance"]
        tokens_values = []

        for asset in tokens:
            name = asset["asset"]["name"]
            ammount = asset["token_balance"]
            ammount_in_usd = ammount * asset["price"]
            tokens_values.append({name: [ammount, ammount_in_usd]})
        
        return [total_balance, tokens_values]
    except:
        print("Failed to get data from mobula")
        