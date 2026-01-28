from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token

auth_bp = Blueprint("auth", __name__,url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if data.get("username")!= "admin" or data.get("password") != "admin123":
        return jsonify({"msg":"Invalid credentials"})
    
    access_token = create_access_token(identity=data["username"])
    refresh_token = create_refresh_token(identity=data["username"])
    return jsonify(
        access_token = access_token,
        refresh_token = refresh_token
    )
