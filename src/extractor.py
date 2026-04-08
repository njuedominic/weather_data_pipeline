import requests # To fetch weather data from the OpenWeather API
import os
from dotenv import load_dotenv # secure applications by keeping secrets (API keys, passwords) out of code.
load_dotenv()

class dataExtractor:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def fetch_weather_data(self, city_name, units="metrics"):
        params = {
            "q": city_name,
            "appid":self.api_key,
            "units":units
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            return{
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "timestamp": data["dt"]
            }

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {city_name}: {e}")
            return None

