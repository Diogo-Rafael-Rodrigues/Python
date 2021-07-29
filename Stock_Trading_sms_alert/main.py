import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_KEY")
NEWS_API_KEY = os.environ.get("NEWS_KEY")
TWILIO_SID = os.environ.get("ACC_SID")
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response_api = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response_api.raise_for_status()
stock_data = response_api.json()["Time Series (Daily)"]  # returns a Dictionary
stock_data = [value for (key, value) in stock_data.items()]  # coverts to a list
yesterday_data = stock_data[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = stock_data[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

diff_percent = round(difference / float(yesterday_closing_price)) * 100

if diff_percent > 5:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    response_news_api = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response_news_api.raise_for_status()
    articles = response_news_api.json()['articles']

    articles_list = articles[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}." 
                          \
                          f" \nBrief: {article['description']}"
                          for article in articles_list]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="Twilio number",
            to="your number"

        )
