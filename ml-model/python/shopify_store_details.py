import requests
from config import Config
from shopify_store_metrics import calculate_metrics

def fetch_store_details():
    """Fetch Shopify store details."""
    url = f"{Config.SHOPIFY_STORE_URL}/admin/api/2023-10/shop.json"
    headers = {"X-Shopify-Access-Token": Config.SHOPIFY_ACCESS_TOKEN}

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        store_data = response.json().get("shop", {})
        
        metrics = calculate_metrics()
        total_sales = metrics["total_sales"]
        avg_sales = metrics["avg_sales"]

        # AI-generated insights
        store_data["ai_description"] = (
            f"{store_data.get('name', 'This store')} specializes in {store_data.get('primary_locale', 'various products')} "
            f"and operates in the {store_data.get('currency', 'global market')} region. "
            f"It has a total of {store_data.get('orders_count', 0)} orders and {store_data.get('customer_count', 0)} customers. "
            f"The total sales amount is ${total_sales}, with an average order value of ${avg_sales:.2f}. "
            f"Current customer satisfaction rating is {store_data.get('customer_review_score', 'Not Available')} stars."
        )
        return store_data
        
    else:
        print("❌ Error fetching store details:", response.text)
        return None
