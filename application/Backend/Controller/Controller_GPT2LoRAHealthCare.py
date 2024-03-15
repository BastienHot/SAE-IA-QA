from flask import Blueprint, request, jsonify
from Model.Model_GPT2LoRAHealthCare import GPT2LoRAHealthCare

prediction_blueprint = Blueprint('prediction', __name__)

@prediction_blueprint.route('/predict', methods=['POST'])
def predict():
    question = request.json['question']
    predictions = GPT2LoRAHealthCare.generate_responses(question)

    return jsonify(predictions)
