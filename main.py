import datetime
import market
import message


# Constants
STOCKS = ["TSLA", "MSFT"]
COMPANY_NAMES = ["Tesla Inc", "Microsoft Corp"]
STOCK_DELTA_THRESHOLD = 5

# Main
today = datetime.date.today()
for stock in STOCKS:
    stock_close_delta = market.stock_close_percent_change(stock)
    if abs(stock_close_delta) >= STOCK_DELTA_THRESHOLD:
        company = COMPANY_NAMES[STOCKS.index(stock)]
        message.message_user(company, stock_close_delta)
