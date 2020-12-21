import os
import requests
from dotenv import load_dotenv
load_dotenv()


# Functions
def news_top_headlines(company):
    """ Retrieve daily stock data using Alpha Vantage api """

    url_news = "https://newsapi.org/v2/everything"
    parameters = {
        "qInTitle": company,
        "pagesize": 3,
        "apikey": os.getenv("API_KEY_NEWS"),
    }

    response = requests.get(url=url_news, params=parameters)
    response.raise_for_status()

    news_stories = response.json()["articles"]
    return news_stories
