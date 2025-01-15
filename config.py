import json


def get_config() -> dict:
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        print(
            "config.json not found. make sure you rename config.json.example to config.json")
        exit(1)
