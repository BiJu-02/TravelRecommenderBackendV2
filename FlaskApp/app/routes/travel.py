from app import app
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User


def register_routes(bp):
    @bp.route("/addPref", methods=["POST"])
    @jwt_required()
    def add_pref():
        current_user_email = get_jwt_identity()
        # prepare weights and add to db

        return {"msg": "travel destination added successfully"}, 201

    @bp.route("/recommend")
    @jwt_required()
    def recommend():
        current_user_email = get_jwt_identity()
        # get current_user data(preference vector) from db and run recommendation engine(ann index search)

        return {"recommendations": ["place1", "place2", "place3"]}, 200

    
    @bp.route("/protected")
    @jwt_required()
    def protected():
        current_user_email = get_jwt_identity()
        return f"protected route works {current_user_email}", 200


    @bp.route("/")
    def travel():
        return "Flask Server for Travel Recommendation", 200