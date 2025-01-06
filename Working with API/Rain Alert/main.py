import requests
from twilio.rest import Client
owm_endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "__API_KEY__"

account_sid = "__YOUR_TWILIO_ACCOUNT_ID__"
auth_token = "__YOUR_TWILIO_AUTH_TOKEN__"

parameters = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(owm_endpoint, params= parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)