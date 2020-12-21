import os
import requests
from dotenv import load_dotenv
load_dotenv()
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


# Functions
# todo: function get x_num of news pieces for company_name
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


print(news_top_headlines("Tesla"))
