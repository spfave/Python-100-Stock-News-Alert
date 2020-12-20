import datetime
import market
import message


# Constants
STOCKS = ["TSLA", "MSFT"]
COMPANY_NAMES = ["Tesla Inc", "Microsoft Corp"]

# Main
# todo: function/script to complete steps 1-3 for all stocks in STOCK list
date = datetime.date.today()
date_back_start = str(date-datetime.timedelta(days=1))
date_back_end = str(date-datetime.timedelta(days=2))

stock_data = get_slice_stock_daily_data(
    "MSFT", (date_back_start, date_back_end))


print(stock_data)
