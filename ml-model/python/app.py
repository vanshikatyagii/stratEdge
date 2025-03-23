from flask import Flask, jsonify, request
from predict import predict_sales_anomalies
from status import get_status 
from shopify_store_details import fetch_store_details
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "StratEdge API is running!"})

@app.route("/status", methods=["GET"])
def check_status():
    """Check the status of data fetching, model training, and predictions."""
    return jsonify(get_status())

@app.route("/predict_sales", methods=["POST"])
def predict_sales():
    try:
        data = request.get_json()
        print("Received data:", data)  # 🛠 Debugging Line

        if not isinstance(data, list):
            return jsonify({"error": "Expected a list of dictionaries"}), 400

        df = pd.DataFrame(data)
        print("Converted DataFrame columns:", df.columns)  # 🛠 Debugging Line

        predictions = predict_sales_anomalies(df)
        return jsonify(predictions.to_dict(orient="records"))
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
@app.route("/store_details", methods=["GET"])
def store_details():
    """Fetch AI-generated store description (Shown on dropdown click)."""
    store_info = fetch_store_details()
    return jsonify(store_info)

if __name__ == "__main__":
    app.run(debug=True)
