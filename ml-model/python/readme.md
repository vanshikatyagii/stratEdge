**StratEdge** 
BI360 is an AI-powered Business Intelligence (BI) tool that integrates with Shopify to analyze store performance. It helps merchants track sales trends, detect anomalies, analyze customer feedback, and generate AI-powered store insights.


**ML Model Features**
 Shopify API Integration – Fetches real-time store data (orders, sales, customer feedback).
 Anomaly Detection – Uses Isolation Forest to detect unusual sales patterns.
 Sales Insights – Provides metrics like total sales, order trends, and low-selling products.
 AI-Generated Store Insights – Summarizes total sales, users, ratings, and trends.
 Customer Sentiment Analysis – Identifies positive/negative feedback trends.
 Flask API – Offers endpoints for fetching data, predictions, and system status.

**Checking if API is Running
Method: GET**
URL: http://127.0.0.1:5000/
{
    "message": "BI360 API is running!"
}

**Checking status
Method: GET**
URL: http://127.0.0.1:5000/status
{
  "data_fetching": "Completed",
  "model_training": "Completed",
  "prediction": "In Progress"
}

**Getting store details
Method: GET**
URL: http://127.0.0.1:5000/store_details
{
  "address1": null,
  "address2": null,
  "ai_description": "StratEdgeTest specializes in en and operates in the INR region. It has a total of 0 orders and 0 customers. The total sales amount is $37.0, with an average order value of $0.74. Current customer satisfaction rating is Not Available stars.",
  "auto_configure_tax_inclusivity": null,
  "checkout_api_supported": true,
  "city": null,
  "country": "IN",
  "country_code": "IN",
  "country_name": "India",
  "county_taxes": true,
  "created_at": "2025-03-22T14:04:44-04:00",
  "currency": "INR",
  "customer_email": "rishabhranjanishwar@gmail.com",
  "domain": "stratedge-test.myshopify.com",
  "eligible_for_payments": false,
  "email": "rishabhranjanishwar@gmail.com",
  "enabled_presentment_currencies": [
    "INR"
  ],
  "finances": true,
  "google_apps_domain": null,
  "google_apps_login_enabled": null,
  "has_discounts": false,
  "has_gift_cards": false,
  "has_storefront": true,
  "iana_timezone": "America/New_York",
  "id": 62935269443,
  "latitude": null,
  "longitude": null,
  "marketing_sms_consent_enabled_at_checkout": false,
  "money_format": "Rs. {{amount}}",
  "money_in_emails_format": "Rs. {{amount}}",
  "money_with_currency_format": "Rs. {{amount}}",
  "money_with_currency_in_emails_format": "Rs. {{amount}}",
  "multi_location_enabled": true,
  "myshopify_domain": "stratedge-test.myshopify.com",
  "name": "StratEdgeTest",
  "password_enabled": true,
  "phone": null,
  "plan_display_name": "Development",
  "plan_name": "affiliate",
  "pre_launch_enabled": false,
  "primary_locale": "en",
  "primary_location_id": 70771474499,
  "province": null,
  "province_code": null,
  "requires_extra_payments_agreement": false,
  "setup_required": false,
  "shop_owner": "Rishabh Ranjan Ishwar",
  "source": null,
  "tax_shipping": null,
  "taxes_included": false,
  "timezone": "(GMT-05:00) America/New_York",
  "transactional_sms_disabled": true,
  "updated_at": "2025-03-22T15:24:04-04:00",
  "weight_unit": "kg",
  "zip": null
}



