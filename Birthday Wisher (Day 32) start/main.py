# import smtplib
#
# my_email = "tonigundersson@gmail.com"
# password = "happynewyearandgodjul!"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="tomoyuki.eguchi@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )
#

import smtplib
import datetime as dt
from random import choice


MY_EMAIL = "tonigundersson@gmail.com"
PASSWORD = "happynewyearandgodjul!"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", "r") as quote_file:
        quote_list = quote_file.readlines()
        quote = choice(quote_list)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="tomoyuki.eguchi@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
