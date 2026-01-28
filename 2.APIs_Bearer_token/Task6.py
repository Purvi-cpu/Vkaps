from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/square", methods=["POST"])
def square():
    number = request.form.get("number")
    number = int(number)
    square = number**2
    return jsonify({
        "number": number,
        "Square": square
    })

if __name__ == "__main__":
    app.run(debug=True)