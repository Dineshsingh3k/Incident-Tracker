class Engineer:

    def __init__(self, engineer_id, name, team):
        self.engineer_id = engineer_id
        self.name = name
        self.team = team

    def to_dict(self):
        return {
            "engineer_id": self.engineer_id,
            "name": self.name,
            "team": self.team,
        }

    def display(self):
        print(
            f"Engineer: {self.name} | "
            f"Team: {self.team}"
        )

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["engineer_id"],
            data["name"],
            data["team"],
        )