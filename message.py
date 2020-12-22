import os
import smtplib
import news
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()


# Functions
def message_user(company, stock_delta):
    """  """

    news_stories = news.news_top_headlines(company, num_stories=3)
    for news_story in news_stories:
        message = generate_stock_message(company, stock_delta, news_story)
        send_stock_message_email(message)


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


def send_stock_message_email(message):
    """  """

    (bluf, body) = message.split("\n", 1)
    email_msg = f"Subject: Stock Alert: {bluf}\n\n{body}".encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=os.getenv("my_email"),
                         password=os.getenv("email_password"))
        connection.sendmail(
            from_addr=os.getenv("my_email"),
            to_addrs=os.getenv("to_email"),
            msg=email_msg,
        )
