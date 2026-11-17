
import json
from models.Incident import Incident


FILE_PATH = "incidents.json"


def save_incidents(incidents):
    data = [incident.to_dict() for incident in incidents]

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

    print("Incidents saved successfully")


def load_incidents():
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)

        return [Incident.from_dict(item) for item in data]

    except FileNotFoundError:
        return []
