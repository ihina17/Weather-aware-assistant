# Product Requirements Document: Weather-Aware Personal Assistant

## Product Summary

The Weather-Aware Personal Assistant is a command-line application that reads a local schedule from `calendar.json`, fetches weather data from Open-Meteo, and generates practical advice for the user.

The goal is to demonstrate AI-assisted system orchestration, not just basic coding.

## Target User

The target user is a student or busy individual who wants quick schedule-aware weather advice before starting the day.

## Problem

People often check their calendar and weather separately. This app combines both sources and gives direct advice, such as carrying an umbrella, leaving early, or preparing for hot weather.

## Core Features

### Read Local Calendar

The app reads events from `calendar.json`.

Each event includes:

- title
- start
- end
- location
- outdoor

### Fetch Weather

The app fetches weather from Open-Meteo using latitude and longitude.

Weather data includes:

- temperature
- precipitation probability
- wind speed
- weather code

### Generate Advice

The app uses rule-based logic to generate advice.

Examples:

- If rain probability is 50% or higher, suggest carrying an umbrella.
- If rain is likely and the user has events, suggest leaving early.
- If an outdoor event exists and rain is likely, suggest a backup plan.
- If temperature is 90°F or higher, suggest carrying water.
- If temperature is 40°F or lower, suggest wearing a jacket.
- If wind speed is 20 mph or higher, suggest caution outdoors.

### CLI Interface

The app runs in the terminal.

Supported commands:

- `today`: shows schedule, weather, and advice
- `exit`: closes the app

## Non-Goals

This project does not include:

- Login accounts
- A web interface
- Real Google Calendar integration
- Mobile notifications
- AI-generated natural language responses

## Architecture

The system is split into focused modules:

- `main.py`: starts the app
- `cli.py`: handles terminal interaction
- `calendar_reader.py`: reads local schedule data
- `weather_api.py`: fetches and parses weather data
- `advice_engine.py`: generates advice
- `models.py`: defines shared data structures

## Success Criteria

The project is successful if:

- The CLI runs without errors.
- The app reads `calendar.json`.
- The app fetches real weather data.
- The app generates schedule-aware advice.
- Automated tests prove the core advice logic works.
- The codebase is modular and easy to understand.