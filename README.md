# Weather-Aware Personal Assistant

## Overview

This is a CLI-based personal assistant that reads a local schedule from `calendar.json`, fetches weather data from Open-Meteo, and generates practical advice based on the user's day.

## Features

- Reads local calendar events from JSON
- Fetches weather from a public API
- Generates rule-based advice
- Runs as a terminal REPL
- Includes automated tests
- Uses a modular folder structure

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python -m src.main
```

Then type:

```text
today
```

To quit:

```text
exit
```

## How to Run Tests

```bash
python -m pytest
```

## Project Structure

```text
weather-aware-assistant/
├── README.md
├── calendar.json
├── requirements.txt
├── pytest.ini
├── specs/
│   └── PRD.md
├── docs/
│   └── rules.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── cli.py
│   ├── calendar_reader.py
│   ├── weather_api.py
│   ├── advice_engine.py
│   └── models.py
└── tests/
    ├── test_advice_engine.py
    ├── test_calendar_reader.py
    └── test_weather_api.py
```

## Vibe Report

### Where did the AI's vibe drift?

The AI's vibe drifted when file names were created incorrectly, such as using `calender` instead of `calendar`. This caused import and file-not-found errors. The architecture itself stayed focused, but the implementation needed correction to match the planned file names.

### When did I use the Builder Hammer?

I used the Builder Hammer when I manually inspected the terminal errors, checked the folder structure, renamed files, fixed `pytest.ini`, and confirmed that the tests actually passed. These fixes were necessary because the AI-generated structure only worked when the file names and Python path matched exactly.

### Most Successful Steering Prompt

The most successful steering prompt was:

"Build this as a modular CLI app. Keep weather fetching, calendar reading, advice logic, and terminal interaction in separate files. Follow the PRD and write tests for the advice rules."

### What I Learned

I learned that AI can generate a working project quickly, but the human still has to manage structure, naming, testing, and debugging. Small mistakes like misspelled filenames can break the whole app. The PRD and rules file helped keep the project organized and aligned with the assignment.