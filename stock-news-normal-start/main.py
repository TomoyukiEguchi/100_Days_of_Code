import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

TWILIO_ACCOUNT_SID = "AC86417573f007073bd506b0a985670542"
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY
}

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]
# print(stock_data)
stock_data_list = [value for (key, value) in stock_data.items()]
# print(stock_data_list)

# --- yesterday's closing stock price
yesterday_cls_price = stock_data_list[0]["4. close"]
print(yesterday_cls_price)

#TODO 2. - Get the day before yesterday's closing stock price

# --- the day before yesterday's closing stock price
day_bef_yesterday_cls_price = stock_data_list[1]["4. close"]
print(day_bef_yesterday_cls_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = float(yesterday_cls_price) - float(day_bef_yesterday_cls_price)
print(difference)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_difference = round((difference / float(yesterday_cls_price)) * 100)
print(percentage_difference)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if abs(percentage_difference) == 0:

    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apikey": NEWS_API_KEY,
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    news_data = news_response.json()["articles"]
    first_three_articles = news_data[0:3]
    print(first_three_articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_articles_list = [f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in first_three_articles]

#TODO 9. - Send each article as a separate message via Twilio.

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles_list:
        message = client.messages \
            .create(
            body=article,
            from_="+18305496129",
            to="+13479526998"
        )
    print(message.status)

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

