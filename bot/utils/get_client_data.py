def get_chat_id(message):
    return message.chat.id

def get_user_id(*, message):
    return message.from_user.id

def get_message_id(*, message):
    return message.message_id