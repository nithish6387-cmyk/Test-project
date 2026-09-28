from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "service": "backend"
    })


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "admin123":
        return jsonify({
            "success": True,
            "message": "Login successful"
        })

    return jsonify({
        "success": False,
        "message": "Invalid username or password"
    }), 401


@app.route("/api/users", methods=["GET"])
def users():
    return jsonify({
        "users": [
            {
                "name": "Nithish",
                "email": "nithish@example.com"
            },
            {
                "name": "Test User",
                "email": "test@example.com"
            }
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)