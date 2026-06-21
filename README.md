# Weather-Aware Personal Assistant

## Overview

The Weather-Aware Personal Assistant is a command-line REPL app that reads a local schedule from `calendar.json`, fetches weather data from Open-Meteo, and generates practical advice based on the user's day.

The project was built for the "Don't Code, Orchestrate" assignment. The focus is on architecture, AI steering, modular design, and guardrails rather than simply writing a working script.

## Features

* Reads local calendar events from JSON
* Automatically adjusts sample calendar events to today's date while preserving event times
* Fetches weather from the Open-Meteo public API
* Generates rule-based schedule-aware advice
* Runs as a terminal REPL
* Separates UI, API, calendar, model, and advice logic
* Includes automated tests for core behavior
* Includes a PRD and AI agent rules file

## Commands

Run the app:

```bash
python -m src.main
```

Inside the app:

```text
today
```

Shows schedule, weather, and advice.

```text
exit
```

Closes the assistant.

## How to Install

```bash
pip install -r requirements.txt
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

## Architecture

The project is intentionally modular.

* `main.py` starts the app.
* `cli.py` handles terminal input and output.
* `calendar_reader.py` reads and normalizes schedule data.
* `weather_api.py` fetches and parses weather data.
* `advice_engine.py` contains the rule-based advice logic.
* `models.py` defines the shared data structures.

This separation keeps the business logic testable and prevents the project from becoming one large script.

## Testing Strategy

The tests focus on behavior that matters to the assignment rubric.

The test suite checks that:

* Rain triggers umbrella advice.
* Rain plus scheduled events triggers leave-early advice.
* Rain plus outdoor events triggers backup-plan advice.
* Hot weather triggers water advice.
* Cold weather triggers jacket advice.
* Windy weather triggers caution advice.
* Normal weather produces normal-schedule advice.
* Calendar events load correctly from JSON.
* Sample event dates are adjusted to today's date.
* Weather API responses are parsed correctly.

## Vibe Report

### Where did the AI's vibe drift?

The AI's vibe drifted in two main ways.

First, early file creation had naming mistakes such as `calender_reader.py` instead of `calendar_reader.py` and `calender.json` instead of `calendar.json`. These small errors broke imports and file loading even though the overall idea of the project was correct.

Second, the first version used static sample dates from `calendar.json`, which made the app feel less like a daily assistant because it always showed the original sample date. I corrected this by steering the design so the calendar reader normalizes sample event dates to the current date while preserving the scheduled times.

### When did I use the Builder Hammer?

I used the Builder Hammer when debugging the terminal errors, checking the folder structure, renaming files, fixing the pytest configuration, and confirming that the tests passed.

I also used manual review to make sure the tests were meaningful. Instead of only testing whether the app starts, I added tests for the actual advice logic, including rain, outdoor events, hot weather, cold weather, wind, and normal weather.

### Most Successful Steering Prompt

The most successful steering prompt was:

"Build this as a modular CLI app. Keep weather fetching, calendar reading, advice logic, and terminal interaction in separate files. Follow the PRD and write tests for the advice rules."

This prompt worked because it gave the AI architectural boundaries instead of just asking for code.

### How the PRD Preserved Intent

The PRD helped preserve the app's intent by defining the "what" and "why" before focusing on implementation details. It specified the user problem, commands, data schema, advice rules, non-goals, and module responsibilities. This reduced vibe drift because each file had a clear purpose.

### What I Learned

I learned that AI-generated code can move quickly, but the human still has to control the system design. The AI can build pieces, but the architect has to manage structure, naming, scope, tests, and alignment with the requirements. Small mistakes can break the app, so tests and clear file responsibilities are important guardrails.
