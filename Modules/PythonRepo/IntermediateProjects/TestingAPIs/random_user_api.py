import requests

response = requests.get("https://randomuser.me/api")

gender = response.json()["results"][0]["gender"]
print(gender)

first_name = response.json()["results"][0]["name"]["first"]
last_name = response.json()["results"][0]["name"]["last"]
title = response.json()["results"][0]["name"]["title"]
age = response.json()["results"][0]["dob"]["age"]
print(f"{title}. {first_name} {last_name} is {age} years old.")