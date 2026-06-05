from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/dashboard")
def dashboard():

    df = pd.read_csv("data/suppliers.csv")

    total_suppliers = len(df)

    total_orders = df["orders"].sum()

    delivery_rate = round(
        (df["on_time"].sum() / total_orders) * 100,
        2
    )

    return jsonify({
        "suppliers": int(total_suppliers),
        "orders": int(total_orders),
        "delivery": delivery_rate
    })

if __name__ == "__main__":
    app.run(debug=True)