import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Make sure you have pillow installed
from weather import get_current_weather, get_forecast

def display_weather(weather, forecast):
    """
    Displays the current weather and forecast in the Tkinter UI.

    Parameters:
    weather (dict): The current weather data.
    forecast (list): The 5-day forecast data.
    """
    if weather:
        location_label.config(text=weather['location'])
        temp_label.config(text=f"{weather['temperature']} °C")
        description_label.config(text=weather['description'])
        
        for i, day in enumerate(forecast):
            forecast_frames[i].config(text=f"{day['day_name']}\n{day['temp_min']}°C to {day['temp_max']}°C\n{day['description']}")
    else:
        messagebox.showerror("Error", "Unable to fetch weather data.")

def fetch_weather():
    """
    Fetches the weather data for the location entered in the Tkinter UI.
    """
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
fetch_button = tk.Button(top_frame, text="Fetch Weather", command=fetch_weather)
fetch_button.pack(side='left', padx=10, pady=10)

# Create the main frame for displaying weather information
main_frame = tk.Frame(root, bg='white')
main_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)

location_label = tk.Label(main_frame, font=('Arial', 20), bg='white')
location_label.pack(pady=10)
temp_label = tk.Label(main_frame, font=('Arial', 50), bg='white')
temp_label.pack(pady=10)
description_label = tk.Label(main_frame, font=('Arial', 20), bg='white')
description_label.pack(pady=10)

# Create frames for the 5-day forecast
forecast_frames = []
for _ in range(5):
    frame = tk.Label(main_frame, font=('Arial', 14), bg='white', justify='left')
    frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)
    forecast_frames.append(frame)

root.mainloop()