from flask import Flask
from Controller.Controller_GPT2LoRAHealthCare import prediction_blueprint
from Controller.Controller_Database import add_user_blueprint, login_blueprint

app = Flask(__name__)
app.register_blueprint(prediction_blueprint)
app.register_blueprint(add_user_blueprint)
app.register_blueprint(login_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
