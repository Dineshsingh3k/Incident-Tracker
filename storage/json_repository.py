
import json
from models.Incident import Incident


class JsonRepository:

    def __init__(self, file_path="incidents.json"):
        self.file_path = file_path

    def save_incidents(self, incidents):
        data = [incident.to_dict() for incident in incidents]

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load_incidents(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)

            return [Incident.from_dict(item) for item in data]

        except FileNotFoundError:
            return []
