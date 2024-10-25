import os

# Load API key from environment variable
api_key = os.getenv('OPENWEATHERMAP_API_KEY')
if not api_key:
    raise ValueError("No API key found. Please set the OPENWEATHERMAP_API_KEY environment variable.")

api_url_current = 'https://api.openweathermap.org/data/2.5/weather'
api_url_forecast = 'https://api.openweathermap.org/data/2.5/forecast'