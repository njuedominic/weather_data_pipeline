### Kenya Weather Data Pipeline

#### Overview
An ETL Pipeline that extracts data from Openweather for five major towns in the Nairobi Metropolitan Area using the OpenWeather API and persists it into a CSV file for further downstream Analysis.

#### Architecture
1. Extract - Python requests to fetch JSON data from OpenWeather
2. Transform - Pandas to flatten the JSON into tabular structure
3. Load - Appending or overwriting a CSV file

#### Local Set up
#### Data Dictionary


