from flask import Flask
from Controller.Controller_GPT2LoRAHealthCare import prediction_blueprint

app = Flask(__name__)
app.register_blueprint(prediction_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
