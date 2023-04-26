import sys
import pyperclip as clipboard
import json


SAVED_DATA = "clipboard.json"

def save_data(_file_path, _data):
    with open(_file_path, "w") as f:
        json.dump(_data, f)


def load_data(_file_path):
    try:
        with open(_file_path, "r") as f:
            _data = json.load(f)
            return _data
    except FileNotFoundError:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)

    elif command == "load":
        key = input("Enter a key: ")

        if key in data:
            clipboard.copy(data[key])
            print("Key value copied to clipboard.")
        else:
            print("Key does not exist.")

    elif command == "list":
        if len(data.keys()) < 1:
            print("No values to list.")
        else:
            print(json.dumps(data, indent=4))

    elif command == "clear":
        key = input("Enter a key to be deleted: ")
        print(f"Deleting {key} from persistent clipboard...")
        data.pop(key)
        save_data(SAVED_DATA, data)
    else:
        print("Unknown command.")

else:
    print("Please provide a command.")