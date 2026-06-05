from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/dashboard")
def dashboard():

    data = {
        "suppliers": 25,
        "orders": 348,
        "delivery": 92
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)