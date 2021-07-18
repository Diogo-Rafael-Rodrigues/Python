import smtplib
import datetime as dt
import random

my_email = "testedeapi5151@gmail.com"
password = "Testedeapi"

now = dt.datetime.now()
day_of_week = now.weekday()


def motivational_email():
    with open("quotes.txt") as data:
        all_quote = data.readlines()
        quote = random.choice(all_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="testedeapi5151@outlook.com", msg=f"Subject:Hello\n\n{quote}")
        connection.close()


if day_of_week == 0:
    motivational_email()
