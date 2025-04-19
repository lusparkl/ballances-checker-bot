import requests

def get_info_about_wallet(*, wallet_address) -> list[int, list]:
    url = f"https://production-api.mobula.io/api/1/wallet/portfolio?wallet={wallet_address}"

    try:
        response = requests.get(url)
        data = response.json()
        tokens = data["data"].get("assets", [])

        if not tokens:
            return [0, []]

        total_balance = data["data"].get("total_wallet_balance", 0)
        tokens_values = []

        for asset in tokens:
            name = asset["asset"].get("name", "Unknown")
            amount = asset.get("token_balance", 0)
            price = asset.get("price", 0)
            amount_in_usd = amount * price if price > 0 else 0
            tokens_values.append({"name": name, "amount": amount, "value_in_usd": amount_in_usd})

        return [total_balance, tokens_values]
    except Exception as e:
        print(f"Failed to get data from Mobula API: {e}")
        return [0, []]
