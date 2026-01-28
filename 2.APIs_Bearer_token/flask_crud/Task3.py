from flask import Flask,  request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "email": "alice@gmail.com"},
    {"id": 2, "name": "Bob", "email": "bob@gmail.com"}
]


@app.route("/get/<int:user_id>", methods = ["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user)

@app.route("/post/<int:user_id>", methods = ["POST"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"message": "User not found"}), 404
    data = request.get_json()
    user["username"]= data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user), 200

@app.route("/add", methods=["POST"])
def add_user():
    data = request.json
    new_user = {
        "id" : len(users),
        "name" : data["name"],
        "email" : data["email"]
    }
    users.append(new_user)
    return jsonify(new_user)

@app.route("/del/<int:user_id>", methods = ["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__=="__main__":
    app.run(debug=True)
   