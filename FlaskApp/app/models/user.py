from app.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def save(self):
        user_data = {
            "email": self.email,
            "password": self.password
        }
        db.users.insert_one(user_data)

    @staticmethod
    def find_one(user_data):
        return db.users.find_one(user_data)

    def check_password(self, password):
        return check_password_hash(self.password, password)


