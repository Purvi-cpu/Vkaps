from flask import Blueprint, jsonify 
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint("users", __name__, url_prefix="/users")

@user_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify(
        user = current_user,
        message = "Bearer token access"
    )