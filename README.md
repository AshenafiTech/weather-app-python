# weather-app-python
# Weather Forecast App

This is a simple weather forecast application built using Python and Tkinter. It fetches current weather and 5-day forecast data from the OpenWeatherMap API.

## Features
- Display current weather
- Display 5-day weather forecast

## Requirements
- Python 3.x
- Pillow
- Requests

## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/AshenafiTech/weather-forecast-app.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd weather-forecast-app
    ```

3. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration
1. **Set the OpenWeatherMap API key as an environment variable**:
    ```sh
    export OPENWEATHERMAP_API_KEY='your_actual_api_key'
    ```

## Usage
1. **Run the application**:
    ```sh
    python weather_app/app.py
    ```

2. **Enter a location and click the button to fetch weather data**.