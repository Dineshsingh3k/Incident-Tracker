from models.Incident import Incident
from models.InfrastructureIncident import InfrastructureIncident
from models.SecurityIncident import SecurityIncident
from models.Engineer import Engineer
from storage.json_repository import JsonRepository

from services.incident_service import incident_service

repository = JsonRepository()
service = incident_service(repository)

engineer = Engineer(199, "Ankit Soni", "Implementation")

incident = Incident(
    201,
    "Payment gateway unavailable",
    "Critical",
    engineer
)

service.add_incident(incident)

print("\nAll incidents:")

for item in service.list_incidents():
    item.display()

print("\nUpdating incident status:")

success = service.update_incident_status(201, "In Progress")

print("Update successful:", success)
