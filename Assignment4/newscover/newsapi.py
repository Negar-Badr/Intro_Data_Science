# newscover/newsapi.py
import requests
from datetime import datetime, timedelta
import re

def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    if not news_keywords:
        raise ValueError("news_keywords must be provided.")

    # Check for invalid keywords using a regular expression
    invalid_keywords = [kw for kw in news_keywords if not re.match("^[a-zA-Z]+$", kw)]
    if invalid_keywords:
        raise ValueError(f"Invalid keyword(s): {', '.join(invalid_keywords)}")
    
    # Format the dates for the lookback period
    today = datetime.today()
    from_date = today - timedelta(days=lookback_days)
    
    # Construct the API URL
    url = "https://newsapi.org/v2/everything"
    
    # Prepare the request parameters
    params = {
        'q': ' OR '.join(news_keywords),
        'from': from_date.strftime('%Y-%m-%d'),
        'to': today.strftime('%Y-%m-%d'),
        'language': 'en',
        'apiKey': api_key
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    # Parse the response JSON
    articles = response.json().get('articles', [])
    return articles