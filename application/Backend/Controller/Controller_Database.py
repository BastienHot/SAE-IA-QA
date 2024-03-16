from flask import Blueprint, request, jsonify
from Service.Service_User import Service_User
from Exception.UserExistsException import UserExistsException
from Exception.UserNotFoundException import UserNotFoundException

add_user_blueprint = Blueprint('addUser', __name__)
login_blueprint = Blueprint('login', __name__)

@add_user_blueprint.route('/add_user', methods=['POST'])
def add_user():
    service_user = Service_User()

    try:
        username = request.json['username']
        password = request.json['password']

        message = service_user.add_user(username, password)
        return jsonify({'message': message}), 200

    except UserExistsException as e:
        return jsonify({'message': str(e)}), 409


@login_blueprint.route('/login', methods=['POST'])
def login():
    service_user = Service_User()
    
    username = request.json['username']
    password = request.json['password']
    
    try:
        user_verified = service_user.verify_user(username, password)
        if user_verified:
            return jsonify({'message': 'Connexion réussie.'}), 200
        else:
            return jsonify({'message': 'Mot de passe incorrect.'}), 401
    except UserNotFoundException:
        return jsonify({'message': 'Utilisateur non trouvé.'}), 404