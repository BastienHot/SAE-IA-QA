from Model.Model_GPT2LoRAHealthCare import GPT2LoRAHealthCare
from Service.Service_Chat import Service_Chat
from Service.Service_Chat_Message import Service_Chat_Message
from Exception.UserNotConnectedException import UserNotConnectedException

class Service_GPT2LoRAHealthCare:
    def __init__(self):
        pass

    def generate_responses(self, user_question, user_id, chat_id, user_is_connected):
        if user_is_connected == False:
            raise UserNotConnectedException("User not connected")    

        serviceChat = Service_Chat()
        serviceChatMessage = Service_Chat_Message()

        if chat_id == None:
            chat_title = self.title_chat(user_question)

            new_chat_id = serviceChat.create_chat(user_id, chat_title, user_is_connected)
            serviceChatMessage.add_user_chat_message(new_chat_id, user_question, user_is_connected)

            ia_response = GPT2LoRAHealthCare().generate_responses(user_question)
            serviceChatMessage.add_ia_chat_message(new_chat_id, ia_response)

            return {
                "chat_id": new_chat_id,
                "chat_title": chat_title,
                "ia_response": ia_response,
                "user_question": user_question
            }

        else:
            serviceChatMessage.add_user_chat_message(chat_id, user_question, user_is_connected)
            ia_response = GPT2LoRAHealthCare().generate_responses(user_question)
            serviceChatMessage.add_ia_chat_message(chat_id, ia_response)

            return {
                "chat_id": chat_id,
                "ia_response": ia_response,
                "user_question": user_question
            }

    def title_chat(self, chat_title):
        chat_title = chat_title[:19]
        chat_title += "..."
        return chat_title