import datetime as dt
import smtplib
import random

with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()
my_email = "emailtest789456123@gmail.com"
password = "wresvssvntmrgnut"
day_of_week = dt.datetime.now().weekday()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="emailtest789456123@yahoo.com",
        msg="fSubject:Hello\n\n"
    )

if day_of_week == 0:
    print(random.choice(quotes))

