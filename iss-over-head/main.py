import time
import requests
from datetime import datetime
import smtplib

MY_LAT = -27.098579
MY_LONG = -48.917801
MY_EMAIL = "your-e-mail@exemple.com"
MY_PASSWORD = "you.password"


def email_sender():
    with smtplib.SMTP("smtp.google.example") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:LOOK UP\n\n THE ISS IS ABOVE YOU IN THE SKY!")


def is_the_iss_above():
    response_api = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_api.raise_for_status()
    data = response_api.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_longitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5:
        return True

def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True


while True:
    time.sleep((60))
    if is_the_iss_above() and is_night_time():
        email_sender()
