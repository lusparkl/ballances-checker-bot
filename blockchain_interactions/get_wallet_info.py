import requests

def get_info_about_wallet(*, wallet) -> list[int, list]:
    url = f"https://production-api.mobula.io/api/1/wallet/portfolio?wallet={wallet}"
    

    try:
        responce = requests.get(url)
        data = responce.json()
        tokens = data["data"]["assets"][0]["cross_chain_balances"]
        
        if not tokens:
            return None

        total_balance =  data["data"]["total_wallet_balance"]
        tokens_values = []

        for key in tokens.keys():
            ammount = tokens[key]["balance"]
            tokens_values.append({"name": key, "ammount": ammount})
        
        return tokens_values
    except:
        print("Failed to get data from mobula")
        