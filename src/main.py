import yaml
import pandas as pd
from extractor import dataExtractor
from db_manager import DBManager

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def run_pipeline():
    # 1. Initialization
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    extractor = dataExtractor()
    db = DBManager()
    weather_data = []

    # 2. Extract
    print("🛰️ Extracting data from OpenWeather...")
    for city in config['locations']:
        result = extractor.fetch_weather_data(city, config['settings']['units'])
        if result:
            weather_data.append(result)

    # 3. Transform & Local Backup (CSV)
    df = pd.DataFrame(weather_data)
    df.to_csv(config['settings']['output_path'], index=False)
    print(f"📁 Local CSV backup created.")

    # 4. Load to PostgreSQL
    print("🐘 Loading data into DigitalOcean PostgreSQL...")
    db.load_data(df)

if __name__ == "__main__":
    run_pipeline()