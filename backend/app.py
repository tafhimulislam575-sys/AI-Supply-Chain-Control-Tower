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

    supplier_risk = []

    for _, row in df.iterrows():

        score = round(
            (row["on_time"] / row["orders"]) * 100,
            2
        )

        if score >= 90:
            status = "GREEN"

        elif score >= 80:
            status = "YELLOW"

        else:
            status = "RED"

        supplier_risk.append({
            "supplier": row["supplier"],
            "score": score,
            "status": status
        })

    return jsonify({
        "suppliers": total_suppliers,
        "orders": int(total_orders),
        "delivery": delivery_rate,
        "risk_analysis": supplier_risk
    })

if __name__ == "__main__":
    app.run(debug=True)