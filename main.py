import os
import requests
from dotenv import load_dotenv
load_dotenv()

STOCK = ["TSLA", "MSFT"]
COMPANY_NAME = ["Tesla Inc", "Microsoft Corp"]

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


# todo: function to get individual stock price at close for specified date
# todo: function to determine percent change in stock price at close over preceding two days
# todo: function to execute if stock percent change exceeds threshold

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# todo: function get x_num of news pieces for company_name

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
# todo: function to send message with stock percent change and news article title & description

# STEP4:
# todo: function to complete steps 1-3 for all stocks in STOCK list
