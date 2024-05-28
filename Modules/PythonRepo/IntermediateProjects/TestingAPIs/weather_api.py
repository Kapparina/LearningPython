import requests


API_KEY = "56d8361e7a0b3de20e1be26e0d123bc8"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print(f"Weather: {weather}")
    print(f"Temperature: {temperature} degrees celsius")
else:
    print(response.status_code)