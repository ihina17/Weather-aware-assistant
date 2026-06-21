import json
from datetime import date, datetime
from typing import List

from src.models import Event


def move_event_to_today(date_time_text: str) -> str:
    """
    Keep the time from the calendar file, but replace the date with today's date.
    """
    original_datetime = datetime.fromisoformat(date_time_text)
    today = date.today()

    updated_datetime = original_datetime.replace(
        year=today.year,
        month=today.month,
        day=today.day,
    )

    return updated_datetime.isoformat()


def load_events(file_path: str) -> List[Event]:
    with open(file_path, "r", encoding="utf-8") as file:
        raw_events = json.load(file)

    events = []

    for item in raw_events:
        event = Event(
            title=item["title"],
            start=move_event_to_today(item["start"]),
            end=move_event_to_today(item["end"]),
            location=item["location"],
            outdoor=item.get("outdoor", False),
        )
        events.append(event)

    return events