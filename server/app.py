from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Server is running"

@app.route("/greet", methods=["POST"])
def greet():
    data = request.get_json()
    name = data.get("name", "stranger")
    
    return jsonify({
        "message": f"Hello, {name}!",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)