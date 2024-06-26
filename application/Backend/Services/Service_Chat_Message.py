from Model.Database import Database
from Exceptions.UserNotConnectedException import UserNotConnectedException
from datetime import datetime

class Service_Chat_Message:
    def __init__(self):
        pass

    def get_chat_messages(self, chat_id, user_is_connected):
        db = Database()

        if user_is_connected == False:
            raise UserNotConnectedException("User not connected")    
        
        try:
            messages = db.select_chat_message_by_chat_id(chat_id)
            db.close()
        except Exception as e:
            db.close()
            raise e
        
        return messages

    def delete_chat_message(self, chat_id, user_is_connected):
        db = Database()

        if user_is_connected == False:
            raise UserNotConnectedException("User not connected")  

        try:
            db.delete_chat_message_by_chat_id(chat_id)
            db.close()  
        except Exception as e:
            db.close()
            raise e

    def add_user_chat_message(self, chat_id, chat_message, user_is_connected):
        db = Database()

        if user_is_connected == False:
            raise UserNotConnectedException("User not connected")    
        
        try:
            db.insert_chat_message(chat_id, chat_message, 0)
            db.close()
        except Exception as e:
            db.close()
            raise e

    def add_ia_chat_message(self, chat_id, chat_message):
        db = Database()

        try:
            db.insert_chat_message(chat_id, chat_message, 1)
            db.close()
        except Exception as e:
            db.close()
            raise e
        
    def get_chat_messages_by_chat_id_and_user_id(self, chat_id, user_is_connected, user_id):
        data=[]

        db = Database()

        if user_is_connected == False:
            raise UserNotConnectedException("User not connected")  
          
        try:
            messages = db.select_chat_message_by_chat_id_and_user_id(chat_id, user_id)

            for message in messages:
                data.append({
                    'chat_message_id': message[0],
                    'chat_message': message[1],
                    'chat_message_is_ia': message[2],
                    'chat_message_date': message[3]
                })

            data = sorted(data, key=lambda x: datetime.strptime(x["chat_message_date"], "%Y-%m-%d %H:%M:%S"), reverse=False)

            db.close()

        except Exception as e:
            db.close()
            raise e

        return data
