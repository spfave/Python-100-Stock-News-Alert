import os
import requests
import datetime
from pytz import timezone
from dotenv import load_dotenv
load_dotenv()
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


# Functions
def is_market_day(date) -> bool:
    """  """
    pass


def previous_market_day(date):
    """  """
    new_date = date-datetime.timedelta(day=1)
    if is_market_day(new_date):
        return new_date
    else:
        previous_market_day(new_date)


def last_market_close_days():
    """  """
    eastern = timezone("US/Eastern")
    # US market close time tz=US/Eastern
    market_close = datetime.time(hour=16, tzinfo=eastern)
    todaytime = datetime.datetime.now(tz=eastern)

    if is_market_day(todaytime.date()) and todaytime.time() > market_close:
        close_day1 = todaytime.date()
    else:
        close_day1 = previous_market_day(todaytime.date())
    close_day2 = previous_market_day(close_day1)

    return (close_day1, close_day2)


# todo: function to determine percent change in stock price at close over preceding two days
def stock_close_percent_change(stock) -> float:
    """ Calculates percent change of stock close price over last two market days """

    close_days = last_market_close_days()
    close_prices = stock_close_prices(stock, close_days)

    close_percent_change = round((close_prices[0]/close_prices[1]-1)*100, 1)
    return close_percent_change


def stock_close_prices(stock, dates):
    """  """

    stock_data = stock_day_data(stock)
    close_prices = [
        stock_data["Time Series (Daily)"][str(date)]["close"] for date in dates]

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


# def get_slice_stock_daily_data(stock_symbol, dates: tuple):
#     """  """

#     stock_data = get_stock_daily_data(stock_symbol)
#     stock_data["Time Series (Daily)"] = {
#         date: stock_data["Time Series (Daily)"][date] for date in dates}

#     return stock_data
