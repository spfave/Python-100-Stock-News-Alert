import os
import requests
import datetime
from dotenv import load_dotenv
load_dotenv()

STOCKS = ["TSLA", "MSFT"]
COMPANY_NAMES = ["Tesla Inc", "Microsoft Corp"]

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def get_stock_daily_data(stock_symbol):
    """ Retrieve daily stock data using Alpha Vantage api """

    url_stocks = "https://www.alphavantage.co/query"
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_symbol,
        "apikey": os.getenv("API_KEY_STOCKS"),
    }  # default outputsize: compact, datatype: json

    response = requests.get(url=url_stocks, params=parameters)
    response.raise_for_status()

    stock_data = response.json()
    return stock_data


def get_slice_stock_daily_data(stock_symbol, dates: tuple):
    """  """

    stock_data = get_stock_daily_data(stock_symbol)
    stock_data["Time Series (Daily)"] = {
        date: stock_data["Time Series (Daily)"][date] for date in dates}

    return stock_data


# todo: function to determine percent change in stock price at close over preceding two days
# todo: function to execute if stock percent change exceeds threshold

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# todo: function get x_num of news pieces for company_name

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
# todo: function to send message with stock percent change and news article title & description

# Main
# todo: function/script to complete steps 1-3 for all stocks in STOCK list
date = datetime.date.today()
date_back_start = str(date-datetime.timedelta(days=1))
date_back_end = str(date-datetime.timedelta(days=2))

stock_data = get_slice_stock_daily_data(
    "MSFT", (date_back_start, date_back_end))


print(stock_data)
