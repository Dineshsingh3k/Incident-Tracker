
class incident_service:

    def __init__(self, repository):
        self.repository = repository
        self.incidents = self.repository.load_incidents()

    def add_incident(self, incident):
        self.incidents.append(incident)
        self.repository.save_incidents(self.incidents)

    def get_incident_by_id(self, incident_id):
        for incident in self.incidents:
            if incident.incident_id == incident_id:
                return incident
        return None

    def update_incident_status(self, incident_id, new_status):
        incident = self.get_incident_by_id(incident_id)

        if incident is None:
            return False

        incident.update_status(new_status)
        self.repository.save_incidents(self.incidents)
        return True

    def list_incidents(self):
        return self.incidents

    def list_open_incidents(self):
        return [
            incident for incident in self.incidents
            if incident.status == "Open"
        ]
