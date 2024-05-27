import requests
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Make sure you have pillow installed
import os

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = '12cf45c81b8b0b9e4b38b41bd12afae3'
api_url_current = 'https://api.openweathermap.org/data/2.5/weather'
api_url_forecast = 'https://api.openweathermap.org/data/2.5/forecast'

def get_current_weather(location):
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

def display_weather(weather, forecast):
    if weather:
        location_label.config(text=weather['location'])
        temp_label.config(text=f"{weather['temperature']} °C")
        description_label.config(text=weather['description'])
        
        for i, day in enumerate(forecast):
            forecast_frames[i].config(text=f"{day['day_name']}\n{day['temp_min']}°C to {day['temp_max']}°C\n{day['description']}")
    else:
        messagebox.showerror("Error", "Unable to fetch weather data.")

def fetch_weather():
    location = location_entry.get()
    current_weather = get_current_weather(location)
    forecast = get_forecast(location)
    
    display_weather(current_weather, forecast)

# Tkinter setup
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("600x400")

# Create the top frame for the location input and button
top_frame = tk.Frame(root, bg='white')
top_frame.pack(side='top', fill='x', padx=10, pady=10)

location_entry = tk.Entry(top_frame, font=('Arial', 14))
location_entry.pack(side='left', padx=10, pady=10, fill='x', expand=True)

fetch_button = tk.Button(top_frame, text="Get Weather", font=('Arial', 14), command=fetch_weather)
fetch_button.pack(side='left', padx=10, pady=10)

# Create the main frame for weather information
main_frame = tk.Frame(root, bg='white')
main_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)

location_label = tk.Label(main_frame, font=('Arial', 24), bg='white')
location_label.pack(pady=10)

temp_label = tk.Label(main_frame, font=('Arial', 48), bg='white')
temp_label.pack(pady=10)

description_label = tk.Label(main_frame, font=('Arial', 14), bg='white')
description_label.pack(pady=10)

# Create the forecast frame for 5-day forecast
forecast_frame = tk.Frame(root, bg='white')
forecast_frame.pack(side='top', fill='x', padx=10, pady=10)

forecast_frames = []
for i in range(5):
    frame = tk.Label(forecast_frame, font=('Arial', 12), bg='white', relief='groove', bd=2)
    frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)
    forecast_frames.append(frame)

root.mainloop()
