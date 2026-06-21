import requests

from src.models import Weather


OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"


def parse_weather(data: dict) -> Weather:
    current = data.get("current", {})
    hourly = data.get("hourly", {})

    probabilities = hourly.get("precipitation_probability", [])
    max_precipitation_probability = max(probabilities) if probabilities else 0

    return Weather(
        temperature_f=current.get("temperature_2m", 0),
        precipitation_probability=max_precipitation_probability,
        wind_speed_mph=current.get("wind_speed_10m", 0),
        weather_code=current.get("weather_code"),
    )


def fetch_weather(latitude: float, longitude: float) -> Weather:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,weather_code",
        "hourly": "precipitation_probability",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "timezone": "auto",
        "forecast_days": 1,
    }

    response = requests.get(OPEN_METEO_URL, params=params, timeout=10)
    response.raise_for_status()

    return parse_weather(response.json())