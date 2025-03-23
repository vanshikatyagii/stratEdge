import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from shopify_api import fetch_shopify_orders

def cluster_feedback():
    orders = fetch_shopify_orders()
    reviews = [order["note"] for order in orders["orders"] if order.get("note")]

    if not reviews:
        return "No customer reviews available."

    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(reviews)

    kmeans = KMeans(n_clusters=3, random_state=42)
    labels = kmeans.fit_predict(X)

    return list(zip(reviews, labels))

if __name__ == "__main__":
    print(cluster_feedback())
