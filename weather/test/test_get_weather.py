
from mock import Mock, patch
import unittest
import nose
import sys
sys.path.append("..")
from weather.weather import Weather

class TestWeather(unittest.TestCase):
	weather = Weather()

	def test_getting_weather_with_valid_city(self):
		# Given
		# When
		response = self.weather.print_weather("Chicago")
		# Then
		self.assertIsNotNone(response)
		self.assertEqual(response['name'], "Chicago")
		self.assertIsNotNone(response['temperature'])
		self.assertIsInstance(response['temperature'], float)

	def test_getting_weather_with_valid_city_and_state_no_comma(self):
		# Given
		# When
		response = self.weather.print_weather("Chicago IL")

		# Then
		self.assertIsNotNone(response)
		self.assertEqual(response['name'], "Chicago")
		self.assertIsNotNone(response['temperature'])
		self.assertIsInstance(response['temperature'], float)

	def test_getting_weather_with_valid_city_and_state_with_comma(self):
		# Given
		# When
		response = self.weather.print_weather("Chicago, IL")
		#Then
		self.assertIsNotNone(response)
		self.assertEqual(response['name'], "Chicago")
		self.assertIsNotNone(response['temperature'])
		self.assertIsInstance(response['temperature'], float)

	def test_getting_weather_with_invalid_city(self):
		# Given
		# When
		response = self.weather.print_weather("asdfjkl")

		# Then
		self.assertIsNone(response)
	
	def test_getting_weather_with_empty_city(self):
		# Given
		# When
		response = self.weather.print_weather("")

		# Then
		self.assertIsNone(response)


	@patch('weather.weather.requests.get')
	def test_getting_weather_when_response_is_ok(self, mock_get):
		# Given
		expected_dict = {
			'main': {'temp': 40.19},
			'name': 'Chicago'
		}
		mock_get.return_value.status_code = 200
		mock_get.return_value.json.return_value = expected_dict

		# When
		response = self.weather.print_weather("Chicago")

		# Then
		self.assertEqual(response['name'], "Chicago")
		self.assertEqual(response['temperature'], 40.19)

	@patch('weather.weather.requests.get')
	def test_getting_weather_when_response_is_404(self, mock_get):
		# Given 
		mock_get.return_value.status_code = 404
		
		# When
		response = self.weather.print_weather("NotAValidCity")
		
		# Then
		self.assertIsNone(response)

	@patch('weather.weather.requests.get')
	def test_getting_weather_when_response_is_400(self, mock_get):
		# Given 
		mock_get.return_value.status_code = 400
		
		# When
		response = self.weather.print_weather("")
		
		# Then
		self.assertIsNone(response)

	@patch('weather.weather.requests.get')
	def test_getting_weather_when_response_is_500(self, mock_get):
		# Given 
		mock_get.return_value.status_code = 500
		
		# When
		response = self.weather.print_weather("NotAValidCity")
		
		# Then
		self.assertIsNone(response)