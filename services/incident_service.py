import json


def add_incident(incidents, incident_id, description, priority):
    new_incident = {
        "id": incident_id,
        "description": description,
        "priority": priority,
        "status": "Open",
    }

    incidents.append(new_incident)

    print("Incident added successfully")


def list_incidents(incidents):
    for incident in incidents:
        print(
            f"ID : {incident['id']} | "
            f"Description : {incident['description']} | "
            f"Priority : {incident['priority']} | "
            f"Status : {incident['status']}"
        )


def list_open_incidents(incidents):
    for incident in incidents:
        if incident["status"] == "Open":
            print(incident)


def update_incident_status(incidents, incident_id, new_status):
    for incident in incidents:
        if incident["id"] == incident_id:
            incident["status"] = new_status
            print("Incident updated")
            return

    print("Incident not found")


def get_incident_by_id(incidents, incident_id):
    try:
        id = int(incident_id)
        for incident in incidents:
            if incident["id"] == id:
                return incident

        return None
    except ValueError:
        print("Invalid incident id. It must be a numeric value")