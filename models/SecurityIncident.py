from models.Incident import Incident


class SecurityIncident(Incident):

    def __init__(self, incident_id, description, priority, security_level):
        super().__init__(incident_id, description, priority)
        self.security_level = security_level

    def display(self):
        super().display()
        print(f"Security Level: {self.security_level}")