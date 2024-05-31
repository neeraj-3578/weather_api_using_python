import requests

api_key = 'b00efd22e4c5b4852c02eff727b5ba70'
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city = input("enter city: ")

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url)

weather_data = response.json()

weather = response.json()["weather"][0]["main"]
temp = response.json()["main"]["temp"]

print(weather_data)
print(f"weather in {city} is {weather}")
print(f"temperature in {city} is {temp}")
