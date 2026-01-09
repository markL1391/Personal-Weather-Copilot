import requests

# Open-Meteo endpoints.
GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

def geocode_city(city: str) -> dict:
    """
      Resolve a city name to geographical coordinates using Open-Meteo Geocoding API.

      Args:
          city (str): Name of the city (e.g. "Berlin")

      Returns:
          dict: Dictionary containing name, country, latitude, longitude and timezone.
                Returns empty dict if no result is found.
      """

    params = {
        "name": city,
        "count": 1,         # Only take the best match.
        "language": "en",
        "format": "json",
    }
    res = requests.get(GEOCODE_URL, params=params, timeout=20)
    res.raise_for_status()
    data = res.json()

    results = data.get("results")
    if not results:
        return {}

    r = results[0]
    return  {
        "name": r.get("name"),
        "country": r.get("country"),
        "latitude": r.get("latitude"),
        "longitude": r.get("longitude"),
        "timezone": r.get("timezone"),
    }

def get_forecast(lat: float, lon: float, timezone: str ="auto") -> dict:
    """
        Fetch current weather data for a given location.

        Args:
            lat (float): Latitude of the location
            lon (float): Longitude of the location
            timezone (str): Timezone identifier or 'auto'

        Returns:
            dict: Weather forecast data from Open-Meteo API
        """

    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,precipitation,wind_speed_10m",
        "timezone": timezone,
    }

    res = requests.get(FORECAST_URL, params=params, timeout=20)
    res.raise_for_status()
    return res.json()

# Local test block (only runs when executing this file directly).
if __name__ == "__main__":
    city = "Berlin"
    geo = geocode_city(city)
    print("Geocode result:")
    print(geo)

    if geo:
        forecast = get_forecast(
            geo['latitude'],
            geo['longitude'],
            timezone=geo.get('timezone', 'auto'),
            )
        print("\nCurrent weather: ")
        print(forecast.get("current"))