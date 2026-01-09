import os
import requests
from weather import geocode_city, get_forecast
from gpt import ...

def main():
    city = input("Which city are you in? ").strip()
    if not city:
        print("Please enter a city.")
        return

    geo = geocode_city(city)
    if not geo:
        print("Sorry, I couldn't find the weather.")
        return

    forecast = get_forecast(
        geo['latitude'],
        geo['longitude'],
        timezone=geo.get('timezone', 'auto'),
    )

    city_label = f"{geo['name']}, {geo['country']}"
    weather_now = forecast.get("current", forecast)

    answer = ask_gpt(weather_now, city_label)

    print(answer)