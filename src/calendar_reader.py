import json
from typing import List

from src.models import Event


def load_events(file_path: str) -> List[Event]:
    with open(file_path, "r", encoding="utf-8") as file:
        raw_events = json.load(file)

    events = []

    for item in raw_events:
        event = Event(
            title=item["title"],
            start=item["start"],
            end=item["end"],
            location=item["location"],
            outdoor=item.get("outdoor", False),
        )
        events.append(event)

    return events