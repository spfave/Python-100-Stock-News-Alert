

# Constants
STOCK_DELTA_THRESHOLD = 5


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
def stock_close_percent_change(stock_data):
    """  """
    pass


# todo: function to execute if stock percent change exceeds threshold