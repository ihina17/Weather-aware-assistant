from typing import List

from src.models import Event, Weather


def generate_advice(events: List[Event], weather: Weather) -> List[str]:
    advice = []

    if not events:
        advice.append("You have no scheduled events today.")
    else:
        advice.append(f"You have {len(events)} scheduled event(s) today.")

    if weather.precipitation_probability >= 50:
        advice.append("Carry an umbrella because rain is likely.")

        if events:
            advice.append("Leave 10 minutes early because rain may slow travel.")

        outdoor_events = [event for event in events if event.outdoor]
        for event in outdoor_events:
            advice.append(
                f"'{event.title}' is outdoors, so consider a backup plan or rain protection."
            )

    if weather.temperature_f >= 90:
        advice.append("It is hot. Carry water and avoid staying outside too long.")

    if weather.temperature_f <= 40:
        advice.append("It is cold. Wear a jacket or extra layer.")

    if weather.wind_speed_mph >= 20:
        advice.append("It is windy. Secure loose items and be careful outdoors.")

    if len(advice) == 1 and events:
        advice.append("Weather looks manageable. Follow your normal schedule.")

    return advice