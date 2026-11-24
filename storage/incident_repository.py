
from abc import ABC, abstractmethod


class IncidentRepository(ABC):

    @abstractmethod
    def save_incidents(self, incidents):
        pass

    @abstractmethod
    def load_incidents(self):
        pass
