from abc import ABC, abstractmethod
from dataclasses import dataclass
import requests
import json
from pathlib import PurePosixPath

BASE_URL = r"https://rickandmortyapi.com/api/"

@dataclass
class API:
    base_url: str


class Requestor:

    def api_request(self, _base_url: str | API, _endpoint: str):
        response = requests.get(str(PurePosixPath(_base_url, _endpoint)))
        return response


class Parser:

    def parse_json(self, data: json):
        return json.dumps(data, indent=4)


rick_morty = API("https://rickandmortyapi.com/api/")
request = 