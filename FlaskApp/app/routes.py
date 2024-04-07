from app import app
from flask import jsonify, make_response, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

@app.route("/")
def index():
    return "Flask Server for Travel Recommendation"


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    print(username, password)
    # authenticate username and password with db call
    # if not auth return "wrong username or password", 401

    access_token = create_access_token(identity=username)

    resp = make_response(jsonify({"msg": "Login Sucessful", "access_token": access_token}))
    # resp.set_cookie("access_token", access_token)

    return resp


@app.route("/logout", methods=["GET"])
def logout():
    pass


@app.route("/addPref", methods=["POST"])
@jwt_required()
def add_pref():
    pass

@app.route("/recommend")
@jwt_required()
def recommend():
    current_user = get_jwt_identity()
    print(current_user)
    # get current_user data(preference vector?!) from db and run recommendation engine?!

    return {"place1": "ehe", "place2": "heh"}