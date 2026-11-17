
import unittest

from models.Engineer import Engineer
from models.Incident import Incident
from services.incident_service import incident_service


class FakeRepository:

    def __init__(self):
        self.data = []

    def load_incidents(self):
        return self.data

    def save_incidents(self, incidents):
        self.data = incidents


class TestIncidentService(unittest.TestCase):

    def setUp(self):
        self.repository = FakeRepository()
        self.service = incident_service(self.repository)

        self.engineer = Engineer(
            199,
            "Ankit Soni",
            "Implementation"
        )

    def test_add_incident(self):
        incident = Incident(
            101,
            "Database failure",
            "High",
            self.engineer
        )

        self.service.add_incident(incident)

        self.assertEqual(
            len(self.service.list_incidents()),
            1
        )

    def test_get_existing_incident(self):
        incident = Incident(
            101,
            "Database failure",
            "High",
            self.engineer
        )

        self.service.add_incident(incident)

        result = self.service.get_incident_by_id(101)

        self.assertIsNotNone(result)
        self.assertEqual(result.incident_id, 101)

    def test_get_missing_incident(self):
        result = self.service.get_incident_by_id(999)

        self.assertIsNone(result)

    def test_update_missing_incident(self):
        result = self.service.update_incident_status(999, "In Progress")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
