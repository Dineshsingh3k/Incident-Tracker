import json
import os

from models.Incident import Incident


def save_incidents(incidents):
    data = [incident.to_dict() for incident in incidents]

    with open("incidents.json", "w") as file:
        json.dump(data, file, indent=4)


def load_incidents():
    if not os.path.exists("incidents.json"):
        return []

    with open("incidents.json", "r") as file:
        data = json.load(file)

    return [Incident.from_dict(item) for item in data]