from models.Incident import Incident
from models.InfrastructureIncident import InfrastructureIncident
from models.SecurityIncident import SecurityIncident
from models.Engineer import Engineer
from storage.json_repository import (load_incidents, save_incidents)

from services.incident_service import (
    add_incident,
    list_incidents,
    list_open_incidents,
    update_incident_status,
    get_incident_by_id
)

incidents = load_incidents()

engineer1 = Engineer(199, "John Doe", "Network Engineer")

incident1 = Incident(1, "Server down", "High", engineer1)

print(incident1.to_dict())

incident1.update_status("In Progress")

incidents.append(incident1)
save_incidents(incidents)   