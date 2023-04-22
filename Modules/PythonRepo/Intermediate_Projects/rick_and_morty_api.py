import requests
import pandas as pd

BASE_URL = "https://rickandmortyapi.com/api/"
endpoint = "character"

def main_request(_url = BASE_URL, _endpoint = endpoint, x = 1):
    r = requests.get(_url + _endpoint + f"?page={x}")
    return r.json()

def get_pages(response):
    return response["info"]["pages"]

def parse_json(response):
    charlist = []
    for item in response["results"]:
        char = {
            "id": item["id"],
            "name": item["name"],
            "num_ep": len(item["episode"]),
        }

        charlist.append(char)
    return charlist

mainlist = []
data = main_request(BASE_URL, endpoint)
for x in range(1, get_pages(data) + 1):
    print(x)
    mainlist.extend(parse_json(main_request(BASE_URL, endpoint, x)))

mainlist_df = pd.DataFrame(mainlist)
mainlist_df.to_csv("../../MiscFiles/charlist.csv", index=False)