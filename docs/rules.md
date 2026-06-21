# AI Agent Rules

## Role

You are an AI coding assistant helping implement a modular command-line weather-aware personal assistant.

The human user is the architect. The AI assistant is the builder. The AI should follow the PRD and preserve the intended structure.

## Primary Objective

Build a small, testable CLI assistant that combines local calendar events with weather data and produces useful schedule-aware advice.

## Architectural Rules

* Keep files small and focused.
* Do not place the entire app in one file.
* Keep terminal input/output in `cli.py`.
* Keep weather API calls in `weather_api.py`.
* Keep calendar loading in `calendar_reader.py`.
* Keep advice rules in `advice_engine.py`.
* Keep shared data structures in `models.py`.
* Keep the app startup logic in `main.py`.
* Do not mix print statements into the advice engine.
* Do not make API calls inside the advice engine.
* Do not read files inside the advice engine.

## Feature Rules

The app must:

* Read events from `calendar.json`.
* Fetch weather from Open-Meteo.
* Support the `today` command.
* Support the `exit` command.
* Generate advice using rule-based logic.
* Normalize sample event dates to the current date while keeping event times.

## Advice Rules

The app should generate advice using these thresholds:

* Rain probability greater than or equal to 50% means umbrella advice is needed.
* Rain plus scheduled events means leave-early advice is needed.
* Rain plus outdoor events means backup-plan advice is needed.
* Temperature greater than or equal to 90°F means water and heat caution advice is needed.
* Temperature less than or equal to 40°F means jacket advice is needed.
* Wind speed greater than or equal to 20 mph means wind caution advice is needed.

## Testing Rules

Tests must prove behavior, not just check that the program starts.

Required test areas:

* Advice engine behavior
* Calendar loading
* Date normalization
* Weather API parsing

Important test cases:

* Rain triggers umbrella advice.
* Rain and events trigger leave-early advice.
* Rain and outdoor events trigger backup-plan advice.
* Hot weather triggers water advice.
* Cold weather triggers jacket advice.
* Windy weather triggers caution advice.
* Normal weather produces normal-schedule advice.
* Calendar JSON loads into event objects.
* Weather API JSON parses into a weather object.

## Scope Control Rules

Do not add:

* Web UI
* Mobile UI
* Database
* Login system
* Google Calendar integration
* Paid API requirements
* Unnecessary frameworks

The project should remain simple enough for a beginner to understand but structured enough to demonstrate architectural control.

## Style Rules

* Use readable Python.
* Prefer explicit function names.
* Avoid clever shortcuts.
* Use comments only when they explain why a decision exists.
* Keep the project easy to review.
