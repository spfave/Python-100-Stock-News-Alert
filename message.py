import os
import news
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Functions
# todo: function to execute if stock percent change exceeds threshold
def message_user(company, stock_delta):
    """  """

    news_stories = news.news_top_headlines(company)
    for news_story in news_stories[:1]:
        message = generate_stock_message(company, stock_delta, news_story)
        send_stock_message_sms(message)


# todo: function to send message with stock percent change and news article title & description
def generate_stock_message(company, stock_delta, news_story):
    """ """

    bluf = f"{company}: 🔺{stock_delta}%" if stock_delta > 0 else f"{company}: 🔻{stock_delta}%"
    headline = f"Headline: {news_story['title']}"
    brief = f"Brief: {news_story['description']}"
    link = f"Link: {news_story['url']}"

    return f"{bluf}\n{headline}\n{brief}\n{link}"


def send_stock_message_sms(message):
    """  """

    client = Client(os.getenv("twilio_sid"), os.getenv("twilio_token"))
    message = client.messages.create(
        body=message,
        from_=os.getenv("twilio_number"),
        to=os.getenv("phone_number"))

    print(message.status)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
