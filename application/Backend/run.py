from flask import Flask
from Controller.Controller_GPT2LoRAHealthCare import prediction_blueprint
from Controller.Controller_Database import signup_blueprint, login_blueprint, user_chat_history_blueprint, delete_chat_blueprint

app = Flask(__name__)
app.register_blueprint(prediction_blueprint)
app.register_blueprint(signup_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(user_chat_history_blueprint)
app.register_blueprint(delete_chat_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
