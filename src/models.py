from dataclasses import dataclass
from typing import Optional


@dataclass
class Event:
    title: str
    start: str
    end: str
    location: str
    outdoor: bool = False


@dataclass
class Weather:
    temperature_f: float
    precipitation_probability: int
    wind_speed_mph: float
    weather_code: Optional[int] = None