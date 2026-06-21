from src.weather_api import parse_weather


def test_parse_weather_extracts_weather_data():
    fake_api_response = {
        "current": {
            "temperature_2m": 84.5,
            "wind_speed_10m": 12.3,
            "weather_code": 3,
        },
        "hourly": {
            "precipitation_probability": [10, 20, 70, 30]
        },
    }

    weather = parse_weather(fake_api_response)

    assert weather.temperature_f == 84.5
    assert weather.wind_speed_mph == 12.3
    assert weather.precipitation_probability == 70
    assert weather.weather_code == 3