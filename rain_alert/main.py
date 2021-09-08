import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""
account_sid = "AC86417573f007073bd506b0a985670542"
auth_token = ""

parameters = {
    "lat": 35.689487,
    "lon": 139.691711,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☔️",
        from_="+18305496129",
        to="+13479526998"
    )
    print(message.status)