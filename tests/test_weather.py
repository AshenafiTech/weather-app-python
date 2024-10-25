import unittest
from unittest.mock import patch
from weather_app.weather import get_current_weather, get_forecast

class TestWeatherFunctions(unittest.TestCase):

    @patch('weather_app.weather.requests.get')
    def test_get_current_weather(self, mock_get):
        # Mock the API response
        mock_response = {
            'main': {'temp': 20, 'humidity': 50},
            'wind': {'speed': 5},
            'weather': [{'description': 'clear sky'}],
            'name': 'London'
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Call the function
        weather = get_current_weather('London')

        # Assertions
        self.assertIsNotNone(weather)
        self.assertEqual(weather['temperature'], 20)
        self.assertEqual(weather['humidity'], 50)
        self.assertEqual(weather['wind_speed'], 5)
        self.assertEqual(weather['description'], 'clear sky')
        self.assertEqual(weather['location'], 'London')

    @patch('weather_app.weather.requests.get')
    def test_get_forecast(self, mock_get):
        # Mock the API response with adjusted timestamps
        mock_response = {
            'list': [
                {'dt': 1609459200, 'main': {'temp': 15}, 'weather': [{'description': 'cloudy'}]},  # 2021-01-01
                {'dt': 1609545600, 'main': {'temp': 17}, 'weather': [{'description': 'sunny'}]},   # 2021-01-02
                {'dt': 1609632000, 'main': {'temp': 16}, 'weather': [{'description': 'rainy'}]},   # 2021-01-03
                {'dt': 1609718400, 'main': {'temp': 14}, 'weather': [{'description': 'cloudy'}]},  # 2021-01-04
                {'dt': 1609804800, 'main': {'temp': 13}, 'weather': [{'description': 'sunny'}]},   # 2021-01-05
                {'dt': 1609891200, 'main': {'temp': 12}, 'weather': [{'description': 'rainy'}]}    # 2021-01-06
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Call the function
        forecast = get_forecast('London')

        # Assertions
        self.assertIsNotNone(forecast)
        self.assertEqual(len(forecast), 5)
        self.assertEqual(forecast[0]['day_name'], 'Friday')  # 2021-01-01 is a Friday
        self.assertEqual(forecast[0]['temp_min'], 15)
        self.assertEqual(forecast[0]['temp_max'], 15)
        self.assertEqual(forecast[0]['description'], 'cloudy')

if __name__ == '__main__':
    unittest.main()