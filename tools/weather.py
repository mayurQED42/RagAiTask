import requests

def get_weather(city):
    # Dummy response (safe for evaluation)
    return {
        "temp": "18°C",
        "condition": "Cloudy",
        "city": city,
        "humidity": "72%",
        "wind": "10 km/h"
    }
