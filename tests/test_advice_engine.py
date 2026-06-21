from src.advice_engine import generate_advice
from src.models import Event, Weather


def test_suggests_umbrella_when_rain_is_likely():
    events = [
        Event(
            title="Walk to Store",
            start="2026-06-19T17:00:00",
            end="2026-06-19T18:00:00",
            location="Store",
            outdoor=True,
        )
    ]

    weather = Weather(
        temperature_f=75,
        precipitation_probability=80,
        wind_speed_mph=5,
    )

    advice = generate_advice(events, weather)

    assert "Carry an umbrella because rain is likely." in advice


def test_suggests_water_when_hot():
    events = []
    weather = Weather(
        temperature_f=95,
        precipitation_probability=10,
        wind_speed_mph=5,
    )

    advice = generate_advice(events, weather)

    assert "It is hot. Carry water and avoid staying outside too long." in advice


def test_suggests_jacket_when_cold():
    events = []
    weather = Weather(
        temperature_f=35,
        precipitation_probability=10,
        wind_speed_mph=5,
    )

    advice = generate_advice(events, weather)

    assert "It is cold. Wear a jacket or extra layer." in advice