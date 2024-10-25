import requests
from datetime import datetime
from config import api_key, api_url_current, api_url_forecast

def get_current_weather(location):
    """
    Fetches the current weather for a given location.

    Parameters:
    location (str): The location for which to fetch the weather.

    Returns:
    dict: A dictionary containing temperature, humidity, wind speed, description, and location.
    """
    response = requests.get(f'{api_url_current}?q={location}&appid={api_key}&units=metric')
    if response.status_code == 200:
        data = response.json()
        current_weather = {
            "temperature": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed'],
            "description": data['weather'][0]['description'],
            "location": data['name']
        }
        return current_weather
    else:
        return None

def get_forecast(location):
    """
    Fetches the 5-day weather forecast for a given location.

    Parameters:
    location (str): The location for which to fetch the forecast.

    Returns:
    list: A list of dictionaries containing date, day name, min and max temperatures, and description.
    """
    response = requests.get(f'{api_url_forecast}?q={location}&appid={api_key}&units=metric')
    if response.status_code == 200:
        data = response.json()
        forecast_dict = {}
        for item in data['list']:
            date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
            if date not in forecast_dict:
                forecast_dict[date] = {
                    "temps": [],
                    "descriptions": []
                }
            forecast_dict[date]["temps"].append(item['main']['temp'])
            forecast_dict[date]["descriptions"].append(item['weather'][0]['description'])
        
        # Process forecast to get daily ranges and main weather type
        forecast = []
        for date, values in forecast_dict.items():
            day_name = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
            forecast.append({
                "date": date,
                "day_name": day_name,
                "temp_min": min(values["temps"]),
                "temp_max": max(values["temps"]),
                "description": max(set(values["descriptions"]), key=values["descriptions"].count)
            })
        
        # Return only the next 5 days
        return forecast[:5]
    else:
        return None