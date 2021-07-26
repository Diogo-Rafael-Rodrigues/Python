import requests
from twilio.rest import Client
import os

# ------- weather -------- #
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY") # env var.

# --------- twilio ----------- #
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

MY_LAT = 48.856613
MY_LONG = 2.352222


parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "exclude": "current,minutely,daily",
        "appid": api_key,
    }
response_api = requests.get(url=OWN_Endpoint, params=parameters)
response_api.raise_for_status()
weather_data = response_api.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = client.messages \
        .create(
        body="It`s going to rain today, remember to bring an umbrella",
        from_="twilio service number",
        to='your phone number'
    )
    print(message.status)


