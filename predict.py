import joblib
import pandas as pd
import os

# ✅ Load trained model properly
model_path = "models/anomaly_model.pkl"

if not os.path.exists(model_path):
    raise FileNotFoundError("❌ Model file not found. Train the model first.")

model = joblib.load(model_path)

if not hasattr(model, "predict"):
    raise TypeError("❌ Loaded object is not a trained model. Retrain and save it again.")

# ✅ Define function to predict anomalies
def predict_sales_anomalies(data):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Expected input data as a Pandas DataFrame.")

    required_columns = ["total_price", "num_items", "fulfillment_status"]
    
    # ✅ Ensure required columns exist
    for col in required_columns:
        if col not in data.columns:
            raise ValueError(f"Missing required column: {col}")

    # ✅ Ensure all columns are numeric
    data[required_columns] = data[required_columns].apply(pd.to_numeric, errors="coerce").fillna(0)

    # ✅ Make predictions (returns -1 for anomaly, 1 for normal)
    predictions = model.predict(data[required_columns])

    # ✅ Convert results to readable format
    data["anomaly"] = ["Anomaly" if p == -1 else "Normal" for p in predictions]

    return data[["total_price", "num_items", "fulfillment_status", "anomaly"]]
