from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)



def rotate_keys():
    pass


from app import routes