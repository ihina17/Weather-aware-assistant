from src.advice_engine import generate_advice
from src.calendar_reader import load_events
from src.weather_api import fetch_weather


DEFAULT_LATITUDE = 29.6516
DEFAULT_LONGITUDE = -82.3248


def print_events(events):
    print("\nSchedule:")
    for event in events:
        print(f"- {event.title}: {event.start} to {event.end} at {event.location}")


def print_weather(weather):
    print("\nWeather:")
    print(f"- Temperature: {weather.temperature_f}°F")
    print(f"- Rain chance: {weather.precipitation_probability}%")
    print(f"- Wind speed: {weather.wind_speed_mph} mph")


def run_cli():
    print("Weather-Aware Personal Assistant")
    print("Type 'today' to get advice.")
    print("Type 'exit' to quit.")

    while True:
        command = input("\n> ").strip().lower()

        if command == "exit":
            print("Goodbye.")
            break

        if command == "today":
            events = load_events("calendar.json")
            weather = fetch_weather(DEFAULT_LATITUDE, DEFAULT_LONGITUDE)
            advice = generate_advice(events, weather)

            print_events(events)
            print_weather(weather)

            print("\nAdvice:")
            for item in advice:
                print(f"- {item}")

        else:
            print("Unknown command. Try 'today' or 'exit'.")