from flask import Flask, render_template, request
import requests

app = Flask(__name__)
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODES = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Depositing rime fog", 51: "Light drizzle", 53: "Moderate drizzle",
    55: "Dense drizzle", 56: "Light freezing drizzle", 57: "Dense freezing drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain", 66: "Light freezing rain",
    67: "Heavy freezing rain", 71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
    77: "Snow grains", 80: "Slight rain showers", 81: "Moderate rain showers",
    82: "Violent rain showers", 85: "Slight snow showers", 86: "Heavy snow showers",
    95: "Thunderstorm", 96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
}


def get_weather(city):
    geo_response = requests.get(GEOCODING_URL, params={"name": city, "count": 1, "language": "en", "format": "json"}, timeout=10)
    geo_response.raise_for_status()
    places = geo_response.json().get("results", [])
    if not places:
        return None

    place = places[0]
    params = {
        "latitude": place["latitude"],
        "longitude": place["longitude"],
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,weather_code,wind_speed_10m",
        "daily": "weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset",
        "timezone": "auto",
        "forecast_days": 5,
    }
    response = requests.get(FORECAST_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    current = data.get("current", {})
    daily = data.get("daily", {})
    forecast = []
    for i, day in enumerate(daily.get("time", [])):
        code = daily.get("weather_code", [None] * len(daily["time"]))[i]
        forecast.append({
            "date": day,
            "condition": WEATHER_CODES.get(code, "Unknown conditions"),
            "max": daily.get("temperature_2m_max", [None] * len(daily["time"]))[i],
            "min": daily.get("temperature_2m_min", [None] * len(daily["time"]))[i],
            "sunrise": daily.get("sunrise", [None] * len(daily["time"]))[i],
            "sunset": daily.get("sunset", [None] * len(daily["time"]))[i],
        })
    return {
        "name": place.get("name", city),
        "region": ", ".join(x for x in [place.get("admin1"), place.get("country")] if x),
        "temperature": current.get("temperature_2m"),
        "feels_like": current.get("apparent_temperature"),
        "humidity": current.get("relative_humidity_2m"),
        "wind": current.get("wind_speed_10m"),
        "precipitation": current.get("precipitation"),
        "condition": WEATHER_CODES.get(current.get("weather_code"), "Unknown conditions"),
        "is_day": current.get("is_day", 1),
        "updated": current.get("time", ""),
        "forecast": forecast,
    }


@app.route("/", methods=["GET", "POST"])
def index():
    city = request.form.get("city", "Gurugram").strip() if request.method == "POST" else request.args.get("city", "Gurugram").strip()
    weather = None
    error = None
    if city:
        try:
            weather = get_weather(city)
            if weather is None:
                error = f"We couldn't find '{city}'. Try another city name."
        except requests.RequestException:
            error = "Weather data is temporarily unavailable. Check your internet connection and try again."
        except (KeyError, TypeError, ValueError):
            error = "We couldn't read the weather response. Please try again."
    else:
        error = "Please enter a city name."
    return render_template("index.html", weather=weather, city=city, error=error)


if __name__ == "__main__":
    app.run(debug=True)
