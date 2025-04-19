from database.initialization import db_client

def is_user_exists(*, user_id):
    response = (
        db_client.table("users")
        .select("*")
        .eq("id", user_id)
        .execute()
    )

    return True if response.data else False

def get_all_wallets(*, user_id):
    responce = (
        db_client.table("wallets")
        .select("wallet_name", "wallet_address")
        .eq("user_id", user_id)
        .execute()
    )

    return responce.data