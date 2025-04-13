from database.initialization import db_client

def add_new_wallet(*, wallet_address, wallet_name, user_id):
    responce = (db_client.table("wallets")
                .insert({"wallet_address": wallet_address, "wallet_name": wallet_name, "user_id": user_id})
                .execute())