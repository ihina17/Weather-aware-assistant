# AI Agent Rules

## Role

You are an AI coding assistant helping build a modular command-line weather-aware personal assistant.

## Main Constraint

The human user is acting as the architect. The AI assistant should implement the system according to the PRD and preserve the intended architecture.

## Coding Rules

- Keep files small and focused.
- Do not put all logic in `main.py`.
- Keep CLI output separate from business logic.
- Keep weather API logic separate from advice logic.
- Use readable function names.
- Avoid unnecessary complexity.
- Do not add a web interface.
- Do not add login or database features.
- Use `calendar.json` as the schedule source.
- Use automated tests for the core logic.

## Testing Rules

Tests should prove the app behavior, not just check that files exist.

Important test cases:

- Rain probability triggers umbrella advice.
- Hot weather triggers water advice.
- Cold weather triggers jacket advice.
- Calendar events load correctly from JSON.
- Weather API JSON is parsed correctly.

## Style Rules

- Prefer simple Python.
- Avoid large frameworks.
- Use clear comments only when they explain why something exists.
- Keep the app understandable for a beginner.