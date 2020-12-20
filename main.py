import datetime
import market
import message


# Constants
STOCKS = ["TSLA", "MSFT"]
COMPANY_NAMES = ["Tesla Inc", "Microsoft Corp"]
STOCK_DELTA_THRESHOLD = 5

# Main
# todo: function/script to complete steps 1-3 for all stocks in STOCK list
today = datetime.date.today()
for stock in STOCKS:
    stock_close_delta = market.stock_close_percent_change(stock)
    if abs(stock_close_delta) >= STOCK_DELTA_THRESHOLD:
        message.message_user(stock, stock_close_delta)


# date_back_start = str(today-datetime.timedelta(days=1))
# date_back_end = str(today-datetime.timedelta(days=2))

# stock_data = get_slice_stock_daily_data(
#     "MSFT", (date_back_start, date_back_end))

# print(stock_data)
