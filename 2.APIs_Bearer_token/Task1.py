from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from dotenv import load_dotenv
import os
app = Flask(__name__)

load_dotenv()
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if data["username"] != "admin" or data["password"] != "admin123":
        return jsonify({"msg":"Bad credentials"}),401
    access_token = create_access_token(identity=data["username"])
    return jsonify(access_token=access_token)

@app.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify(
        username = current_user,
        message = "Access granted using Bearer Token"
    )

if __name__ =="__main__":
    app.run(debug=True)