import json


def load_config():
    """
    Load project configuration.
    """

    with open("config/config.json", "r") as file:
        config = json.load(file)

    return config