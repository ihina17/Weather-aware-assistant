import json

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