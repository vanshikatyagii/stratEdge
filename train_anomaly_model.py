import pandas as pd
import joblib
import os
import requests
from sklearn.ensemble import IsolationForest
from dotenv import load_dotenv
from config import Config
from status import update_status  # ✅ Import status tracking

# Load environment variables
load_dotenv()

# Update status - Model Training Started
update_status("model_training", "In Progress")

# Fetch data from Shopify API
def fetch_shopify_orders():
    url = f"{Config.SHOPIFY_STORE_URL}/admin/api/2023-10/orders.json"
    headers = {"X-Shopify-Access-Token": Config.SHOPIFY_ACCESS_TOKEN}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        update_status("data_fetching", "Completed")  # ✅ Update status
        return response.json().get("orders", [])
    else:
        update_status("data_fetching", "Failed")
        print("❌ Error fetching orders:", response.text)
        return []

# Fetch and process data
df = pd.DataFrame(fetch_shopify_orders())

if df.empty:
    update_status("model_training", "Failed: No Data")
    print("❌ No data available for training.")
    exit()

# ✅ Ensure the required columns exist
df["num_items"] = df.get("num_items", 0)  # Fill missing column
df["fulfillment_status"] = df["fulfillment_status"].astype(str).factorize()[0]  # Convert categorical to numeric

features = ["total_price", "num_items", "fulfillment_status"]
X_train = df[features]

# ✅ Train Isolation Forest Model
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(X_train)

# ✅ Ensure models directory exists
os.makedirs("models", exist_ok=True)

# ✅ Save trained model
joblib.dump(model, "models/anomaly_model.pkl")

update_status("model_training", "Completed")  # ✅ Update status
print("✅ Model trained and saved successfully!")
