from database.initialization import db_client

def add_new_wallet(*, wallet_address, wallet_name, user_id):
    responce = (db_client.table("wallets")
                .insert({"wallet_address": wallet_address, "wallet_name": wallet_name, "user_id": user_id})
                .execute())

def delete_wallet(*, wallet_name, user_id):
    responce = (db_client.table("wallets")
                .delete()
                .eq("wallet_name", wallet_name)
                .eq("user_id", user_id)
                .execute())

def add_new_user(*, user_id):
    responce = (db_client.table("users")
                .insert({"id": user_id})
                .execute())