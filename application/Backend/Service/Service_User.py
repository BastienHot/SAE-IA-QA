from Model.Database import Database
import bcrypt
from Exception.UserExistsException import UserExistsException
from Exception.UserNotFoundException import UserNotFoundException

class Service_User:

    def __init__(self):
        pass

    def add_user(self, username, password):
        db = Database()

        if db.user_exists(username):
            db.close()
            raise UserExistsException("L'utilisateur existe déjà.")

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        db.add_user(username, hashed_password)
        db.close()

        return "Le compte a été créé avec succès."

    def verify_user(self, username, password):
        db = Database()
        user_info = db.get_user(username)
        
        if user_info is None:
            db.close()
            raise UserNotFoundException("Utilisateur non trouvé")

        hashed_password_from_db = user_info[1]
        
        if hashed_password_from_db.startswith("b'") and hashed_password_from_db.endswith("'"):
            hashed_password_from_db = hashed_password_from_db[2:-1].encode('utf-8')
        elif isinstance(hashed_password_from_db, str):
            hashed_password_from_db = hashed_password_from_db.encode('utf-8')

        password_match = bcrypt.checkpw(password.encode('utf-8'), hashed_password_from_db)
        
        db.close()
        
        return password_match