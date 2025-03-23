import pandas as pd
from sklearn.ensemble import IsolationForest
from shopify_api import fetch_shopify_orders

def analyze_sales():
    """Detect anomalies in sales trends."""
    orders = fetch_shopify_orders()
    if not orders:
        return "No order data available."

    df = pd.DataFrame(orders)

    # Feature selection
    X = df[["total_price", "num_items", "fulfillment_status"]]

    model = IsolationForest(contamination=0.1, random_state=42)
    df["anomaly"] = model.fit_predict(X)

    anomalies = df[df["anomaly"] == -1]
    return anomalies[["customer_id", "total_price"]]

if __name__ == "__main__":
    print(analyze_sales())
