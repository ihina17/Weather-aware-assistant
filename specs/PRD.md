# Product Requirements Document: Weather-Aware Personal Assistant

## 1. Product Summary

The Weather-Aware Personal Assistant is a command-line REPL application that reads a local schedule from `calendar.json`, fetches daily weather data from the Open-Meteo public API, and generates practical advice based on the user's events and current weather conditions.

This project is designed to demonstrate AI-assisted software orchestration. The main goal is not to build the most complex app, but to show that the human acted as the architect by defining the system structure, requirements, constraints, and tests before treating the AI agent as an implementation partner.

## 2. Target User

The target user is a student or busy individual who wants quick daily advice before leaving for class, errands, work, or outdoor activities.

## 3. Problem Statement

Users often check their calendar and the weather separately. This app combines both pieces of information and gives direct advice, such as carrying an umbrella, leaving early, bringing water, wearing a jacket, or preparing a backup plan for outdoor events.

## 4. Goals

The app should:

* Run in the terminal as a simple REPL.
* Read events from a local `calendar.json` file.
* Fetch real weather data from Open-Meteo.
* Generate advice using clear rule-based logic.
* Keep UI, weather API logic, calendar reading, data models, and advice logic in separate files.
* Include automated tests that prove the core logic works.
* Demonstrate that the AI agent was guided by architecture, not simply asked to generate a single script.

## 5. Non-Goals

The app will not include:

* A web interface.
* A mobile app.
* Login accounts.
* Database storage.
* Google Calendar integration.
* Push notifications.
* A paid weather API.
* Fully LLM-generated advice.

These features are intentionally excluded to keep the project focused on orchestration, modular design, and testable logic.

## 6. User Commands

The CLI supports two commands:

### `today`

Reads the local schedule, fetches weather, prints the user's events, prints weather conditions, and displays advice.

### `exit`

Closes the assistant.

## 7. Calendar Input Schema

The app reads events from `calendar.json`.

Each event must include:

* `title`: name of the event
* `start`: ISO datetime string
* `end`: ISO datetime string
* `location`: event location

Each event may also include:

* `outdoor`: boolean value indicating whether weather risk matters more for the event

Example:

```json
{
  "title": "Grocery Trip",
  "start": "2026-06-19T17:30:00",
  "end": "2026-06-19T18:15:00",
  "location": "Grocery Store",
  "outdoor": true
}
```

Because this is a sample local calendar, the app normalizes event dates to the current date while preserving the original event times. This makes the app useful whenever it is run, instead of always showing the static sample date.

## 8. Weather Data

The app uses Open-Meteo to fetch weather data using latitude and longitude.

The weather module returns a simplified `Weather` object with:

* temperature in Fahrenheit
* precipitation probability
* wind speed in miles per hour
* weather code

## 9. Advice Rules

The app uses rule-based advice logic.

Rules:

* If precipitation probability is 50% or higher, suggest carrying an umbrella.
* If precipitation probability is 50% or higher and the user has scheduled events, suggest leaving 10 minutes early.
* If precipitation probability is 50% or higher and an event is marked as outdoor, suggest a backup plan or rain protection.
* If temperature is 90°F or higher, suggest carrying water and avoiding long outdoor exposure.
* If temperature is 40°F or lower, suggest wearing a jacket or extra layer.
* If wind speed is 20 mph or higher, suggest securing loose items and being careful outdoors.
* If the user has events and none of the weather risk rules apply, say the weather looks manageable.
* If the user has no events, say there are no scheduled events today.

## 10. Architecture

The app is organized into small, focused modules:

* `src/main.py`: starts the program
* `src/cli.py`: handles terminal commands and printed output
* `src/calendar_reader.py`: reads and normalizes local calendar events
* `src/weather_api.py`: fetches and parses Open-Meteo weather data
* `src/advice_engine.py`: contains the rule-based advice logic
* `src/models.py`: defines the shared `Event` and `Weather` data structures

This separation keeps business logic away from print statements and makes the system easier to test.

## 11. Test Strategy

Automated tests are required for the core logic.

Tests should verify:

* Rain triggers umbrella advice.
* Rain plus scheduled events triggers leave-early advice.
* Rain plus an outdoor event triggers backup-plan advice.
* Hot weather triggers water advice.
* Cold weather triggers jacket advice.
* Windy weather triggers caution advice.
* Safe weather produces normal-schedule advice.
* Calendar events load from JSON correctly.
* Sample event dates are normalized to today.
* Open-Meteo API responses are parsed into the internal `Weather` model.

## 12. Success Criteria

The project is successful if:

* The CLI runs without errors.
* The `today` command displays schedule, weather, and advice.
* The source code is modular.
* API logic and advice logic are separate from terminal UI.
* The PRD clearly defines what the app should do and why.
* Tests cover meaningful behavior.
* The README includes a Vibe Report explaining AI steering, drift, and manual fixes.
