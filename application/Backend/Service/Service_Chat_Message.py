from Model.Database import Database
from Exception.UserNotConnectedException import UserNotConnectedException

class Service_Chat_Message:
    def __init__(self):
        pass

    def get_chat_messages(self, chat_id, user_is_connected):
        db = Database()
        if user_is_connected == False:
            raise UserNotConnectedException("User not connected")    
        messages = db.select_chat_message_by_chat_id(chat_id)
        db.close()
        return messages

    def delete_chat_message(self, chat_id, user_is_connected):
        db = Database()
        if user_is_connected == False:
            raise UserNotConnectedException("User not connected")    
        db.delete_chat_message_by_chat_id(chat_id)
        db.close()

    def add_user_chat_message(self, chat_id, chat_message, user_is_connected):
        db = Database()
        if user_is_connected == False:
            raise UserNotConnectedException("User not connected")    
        db.insert_chat_message(chat_id, chat_message, 0)
        db.close()

    def add_ia_chat_message(self, chat_id, chat_message):
        db = Database()
        db.insert_chat_message(chat_id, chat_message, 1)
        db.close()
