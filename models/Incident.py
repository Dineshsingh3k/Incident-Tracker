from models.Engineer import Engineer

class Incident:

    def __init__(
        self, incident_id, description,
        priority, assigned_engineer
    ):
        self.incident_id = incident_id
        self.description = description
        self.priority = priority
        self.assigned_engineer = assigned_engineer
        self._status = "Open"

    @property
    def status(self):
        return self._status

    def update_status(self, new_status):
        allowed_statuses = ["Open", "In Progress", "Resolved"]

        if new_status not in allowed_statuses:
            raise ValueError("Invalid incident status")

        self._status = new_status

    def to_dict(self):
        return {
            "incident_id": self.incident_id,
            "description": self.description,
            "priority": self.priority,
            "status": self._status,
            "assigned_engineer": self.assigned_engineer.to_dict(),
        }

    def display(self):
        print(f"Incident ID: {self.incident_id}")
        print(f"Description: {self.description}")
        print(f"Priority: {self.priority}")
        print(f"Status: {self._status}")
        print("Assigned Engineer:")
        self.assigned_engineer.display()

    @classmethod
    def from_dict(cls, data):
        engineer = Engineer.from_dict(data["assigned_engineer"])

        incident = cls(
            data["incident_id"],
            data["description"],
            data["priority"],
            engineer,
        )
        incident.update_status(data["status"])

        return incident