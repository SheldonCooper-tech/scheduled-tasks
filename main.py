import requests
import os


def telegram_bot_send_text(bot_message):
    bot_token = os.environ["TG_BOT_TOKEN"]
    bot_chatID = os.environ["TG_CHAT_ID"]
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


config = {
    "lat": os.environ["LAT"],
    "lon": os.environ["LON"],
    "appid": os.environ["OWM_APP_KEY"],
    "cnt": 4,
}
end_point = "https://api.openweathermap.org/data/2.5/forecast"
five_day_forecast = requests.get(end_point, params=config)
five_day_forecast.raise_for_status()
weather_data = five_day_forecast.json()

chances_to_use_umbrella = 0
for forecast in weather_data["list"]:
    if forecast["weather"][0]["id"] < 700:
        chances_to_use_umbrella += 1
if chances_to_use_umbrella > 0:
    telegram_bot_send_text("Bring an umbrella!")
