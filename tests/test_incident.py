
import unittest

from models.Engineer import Engineer
from models.Incident import Incident


class TestIncident(unittest.TestCase):

    def setUp(self):
        self.engineer = Engineer(
            199,
            "Ankit Soni",
            "Implementation"
        )

        self.incident = Incident(
            101,
            "Database connection failure",
            "High",
            self.engineer
        )

    def test_incident_initial_status(self):
        self.assertEqual(self.incident.status, "Open")

    def test_update_incident_status(self):
        self.incident.update_status("In Progress")

        self.assertEqual(
            self.incident.status,
            "In Progress"
        )

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            self.incident.update_status("New")


if __name__ == "__main__":
    unittest.main()
