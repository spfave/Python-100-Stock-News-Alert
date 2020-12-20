import os
import requests
from dotenv import load_dotenv
load_dotenv()


# Functions
def stock_close_percent_change(stock) -> float:
    """ Calculates percent change of stock close price over last two market days """

    close_prices = stock_close_prices(stock)

    last_close_percent_change = round(
        (close_prices[0]/close_prices[1]-1)*100, 1)
    return last_close_percent_change


def stock_close_prices(stock):
    """  """

    stock_data = stock_day_data(stock)
    close_prices = [float(day_data["4. close"])
                    for day_data in stock_data["Time Series (Daily)"].values()]

    return close_prices


def stock_day_data(stock):
    """ Retrieve daily stock data using Alpha Vantage api """

    url_stocks = "https://www.alphavantage.co/query"
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey": os.getenv("API_KEY_STOCKS"),
    }  # default - outputsize: compact, datatype: json

    response = requests.get(url=url_stocks, params=parameters)
    response.raise_for_status()

    stock_data = response.json()
    return stock_data
