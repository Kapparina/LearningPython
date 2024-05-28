import requests
import pandas as pd
import json
from pathlib import PurePosixPath


BASE_URL = "https://rickandmortyapi.com/api/"
response = requests.get(BASE_URL)
# data = response.json()
# print(json.dumps(data))


def parse_json(_data):
    output = json.dumps(_data, indent=4)
    return output


print(parse_json(data := response.json()))

my_list = []
for d in data.values():
    my_list.append(PurePosixPath(d).name)

for i in my_list:

# table = pd.read_html(f"{BASE_URL}/character")
# print(table)