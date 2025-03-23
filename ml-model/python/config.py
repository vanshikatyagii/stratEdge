import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL")
    SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
    SHOPIFY_PASSWORD = os.getenv("SHOPIFY_PASSWORD")
    FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
    
print("SHOPIFY_STORE_URL:", Config.SHOPIFY_STORE_URL)
print("SHOPIFY_ACCESS_TOKEN:", Config.SHOPIFY_ACCESS_TOKEN)