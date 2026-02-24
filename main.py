import os
import smtplib
import datetime as dt
import random

my_email = os.environ.get("MY_EMAIL")
app_password = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
weekday = now.weekday()

date_of_birth = dt.datetime(year= 1995, month= 11, day= 16)


with open("quotes.txt") as quotes:
    quotes_list = quotes.readlines()
    selection = random.choice(quotes_list)

email_text = (f"Subject: Motivational Quote for Today \n\n"
                f"{selection}")

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="maria_deetman@hotmail.com",
                        msg=email_text
                        )
