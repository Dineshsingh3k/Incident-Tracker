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

# Create an engineer and incident
engineer = Engineer(199, "Ankit Soni", "Implementation")

incident = Incident(
    101,
    "Database connection failure",
    "High",
    engineer
)

incident.update_status("In Progress")

# Save to JSON
incidents = [incident]
save_incidents(incidents)

# Load from JSON
loaded_incidents = load_incidents()

# Display reconstructed objects
for loaded_incident in loaded_incidents:
    print(loaded_incident.display())
