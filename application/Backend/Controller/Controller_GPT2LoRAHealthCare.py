from flask import Blueprint, request, jsonify
from Service.Service_GPT2LoRAHealthCare import Service_GPT2LoRAHealthCare

prediction_blueprint = Blueprint('prediction', __name__)

@prediction_blueprint.route('/predict', methods=['POST'])
def predict():
    gpt2LoRAHealthCare = Service_GPT2LoRAHealthCare()

    question = request.json['user_question']
    user_id = request.json['user_id']
    chat_id = request.json['chat_id']
    user_is_connected = request.json['user_is_connected']
    
    predictions = gpt2LoRAHealthCare.generate_responses(question, user_id, chat_id, user_is_connected)

    return jsonify(predictions)
