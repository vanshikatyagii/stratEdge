import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from shopify_api import fetch_shopify_orders
from shopify_store_metrics import calculate_metrics

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def analyze_feedback():
    orders = fetch_shopify_orders()
    if not orders:
        return "No data available."

    feedback_scores = []
    positive_count, negative_count = 0, 0
    
    for order in orders["orders"]:
        if "note" in order and order["note"]:
            score = sia.polarity_scores(order["note"])
            feedback_scores.append(score)
            
            if score["compound"] > 0:
                positive_count += 1
            else:
                negative_count += 1
    
    metrics = calculate_metrics()
    total_sales = metrics["total_sales"]
    avg_sales = metrics["avg_sales"]

    # Generate AI insights
    insights = {
        "total_reviews": len(feedback_scores),
        "positive_reviews": positive_count,
        "negative_reviews": negative_count,
        "total_sales": total_sales,
        "avg_sales": avg_sales,
        "recommendation": (
            "Focus on high-rated products, improve product descriptions, and engage with customers "
            "to enhance user experience. Consider offering discounts on low-selling products."
        ),
    }

    return {"feedback_analysis": feedback_scores, "insights": insights}


if __name__ == "__main__":
    print(analyze_feedback())
