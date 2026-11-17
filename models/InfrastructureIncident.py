from models.Incident import Incident


class InfrastructureIncident(Incident):

    def __init__(self, incident_id, description, priority, affected_service):
        super().__init__(incident_id, description, priority)
        self.affected_service = affected_service

    def display(self):
        super().display()
        print(f"Affected Service : {self.affected_service}")