from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.currencybeacon.com/v1"
API_KEY = "61c537dd8304b5af5250b9d50c364fab"
printer = PrettyPrinter()

def get_all_currencies():
    endpoint = "/currencies/fiat"
    url = BASE_URL + endpoint + "?api_key=" + API_KEY
    data = get(url).json()

    data = list(data.items())
    data.sort()
    print(type(data))
    printer.pprint(data)


def currency_code():
    code = input("Enter a currency code: ")
    endpoint = f"/currencies/{code}.json"
    url = BASE_URL + API_VERSION + DATE + endpoint
    data = get(url).json()

    printer.pprint(data)

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency["currencyName", ""]
        _id = currency["id"]
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")

get_all_currencies()