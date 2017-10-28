import os
import requests

API_KEY = os.environ['OPEN_WEATHER_KEY']
BASE_URL= "http://api.openweathermap.org/data/2.5/"

class Weather():
	@staticmethod
	def ask_city():
		return input("Where are you?\n")

	@staticmethod
	def print_weather(city):
		res = requests.get("{}weather?q={}&units=imperial&APPID={}".format(BASE_URL, city, API_KEY))

		if res.status_code == requests.codes.ok:
			res = res.json()
			print("{} weather:\n{} degrees Fahrenheit".format(res['name'], res['main']['temp']))
			return {
					'name': res['name'], 
					'temperature': res['main']['temp'] 
					}
		else:
			if res.status_code in (400, 404):
				print("The city you entered could not be found or is invalid.")
				return None
			else:
				res.raise_for_status()
				return None

if __name__ == "__main__":
	weather = Weather()
	weather.print_weather(weather.ask_city())
