import requests
from config import Config

def fetch_shopify_orders():
    """Fetch Shopify order data."""
    url = f"{Config.SHOPIFY_STORE_URL}/admin/api/2023-10/orders.json"
    headers = {"X-Shopify-Access-Token": Config.SHOPIFY_ACCESS_TOKEN}

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        orders = response.json().get("orders", [])
        return [
            {
                "customer_id": order["customer"]["id"] if order.get("customer") else None,
                "total_price": float(order.get("total_price", 0)),
                "num_items": sum(item["quantity"] for item in order.get("line_items", [])),
                "fulfillment_status": 1 if order.get("fulfillment_status") == "fulfilled" else 0,
                "order_created_at": order["created_at"],
            }
            for order in orders
        ]
    else:
        print("❌ Error fetching orders:", response.text)
        return []
