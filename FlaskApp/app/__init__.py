from flask import Flask
from flask_jwt_extended import JWTManager
from app.db import init_db
import os


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

init_db()

@app.route("/")
def index():
    return "Flask Server for Travel Recommendation", 200


from app.routes import auth_bp, travel_bp
app.register_blueprint(auth_bp)
app.register_blueprint(travel_bp)

# def rotate_keys():
#     pass




