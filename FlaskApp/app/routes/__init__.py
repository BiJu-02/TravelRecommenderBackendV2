from flask import Blueprint

auth_bp = Blueprint('auth', __name__)
travel_bp = Blueprint('travel', __name__)

from app.routes import auth, travel
auth.register_routes(auth_bp)
travel.register_routes(travel_bp)