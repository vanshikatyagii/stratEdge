import numpy as np
from shopify_api import fetch_shopify_orders

def calculate_metrics():
    """Calculate key sales and store metrics."""
    orders = fetch_shopify_orders()
    if not orders:
        return "No order data available."

    sales = [order["total_price"] for order in orders]
    avg_sales = np.mean(sales)
    total_sales = np.sum(sales)

    return {"total_sales": total_sales, "avg_sales": avg_sales}

if __name__ == "__main__":
    print(calculate_metrics())
