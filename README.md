# 🌦️ SkyCast — Weather Information Website

A beginner-friendly weather website built with **HTML, CSS, Python, and Flask**. Search for a city to see its current weather and a five-day forecast.

## Features

- Search weather by city name
- Current temperature and feels-like temperature
- Weather condition, humidity, wind speed, and precipitation
- Five-day forecast with daily high/low temperatures
- Responsive layout for phones and computers
- Helpful messages for unknown cities or network/API errors
- Uses Open-Meteo's free APIs; no API key is required

## Tech stack

- **Frontend:** HTML5, CSS3
- **Backend:** Python, Flask
- **HTTP requests:** Requests
- **Weather data:** Open-Meteo Geocoding API and Forecast API

## Run locally

1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```bash
   .venv\Scripts\activate
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the app:

   ```bash
   python app.py
   ```

7. Open `http://127.0.0.1:5000` in your browser.

An internet connection is required to fetch live weather data.

## Project structure

```text
weather-information-website/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Publish on GitHub

1. Sign in to [GitHub](https://github.com/).
2. Create a new **public** repository named `weather-information-website`.
3. Upload the files and folders from this project (or push the folder using Git).
4. Keep this README so visitors know what the project does and how to run it.
5. Add a screenshot of your running website to the repository to make it more attractive.

### Optional: push with Git

After creating an empty GitHub repository, run these commands inside this folder (replace the placeholder with your repository URL):

```bash
git init
git add .
git commit -m "Build SkyCast weather website"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## Data source and attribution

Weather data is provided by [Open-Meteo](https://open-meteo.com/). Check its current terms and attribution requirements before public deployment.

## Ideas for future improvements

- Add a Celsius/Fahrenheit toggle
- Add weather icons and hourly forecasts
- Add a location-based weather option with browser permission
- Add tests for API errors and city searches
- Deploy the Flask app to a Python-compatible hosting provider

---
Made as a learning project. Customize the design and features as you learn!
