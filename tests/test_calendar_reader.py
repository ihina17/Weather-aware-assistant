import json
from datetime import date

from src.calendar_reader import load_events


def test_load_events_reads_calendar_json(tmp_path):
    calendar_file = tmp_path / "calendar.json"

    sample_events = [
        {
            "title": "Class",
            "start": "2026-06-19T10:00:00",
            "end": "2026-06-19T11:30:00",
            "location": "Campus",
            "outdoor": False,
        }
    ]

    calendar_file.write_text(json.dumps(sample_events), encoding="utf-8")

    events = load_events(str(calendar_file))

    assert len(events) == 1
    assert events[0].title == "Class"
    assert events[0].location == "Campus"
    assert events[0].outdoor is False


def test_load_events_moves_sample_dates_to_today(tmp_path):
    calendar_file = tmp_path / "calendar.json"

    sample_events = [
        {
            "title": "Class",
            "start": "2026-06-19T10:00:00",
            "end": "2026-06-19T11:30:00",
            "location": "Campus",
            "outdoor": False,
        }
    ]

    calendar_file.write_text(json.dumps(sample_events), encoding="utf-8")

    events = load_events(str(calendar_file))

    today_text = date.today().isoformat()

    assert events[0].start.startswith(today_text)
    assert events[0].end.startswith(today_text)
    assert events[0].start.endswith("10:00:00")
    assert events[0].end.endswith("11:30:00")