import requests

BASE_URL = "http://randomfox.ca/floof"
response = requests.get(BASE_URL)
fox = response.json()

print(fox["image"])