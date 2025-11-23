class Project:
    def __init__(self, project_id, name, client, amount, status="Pending"):
        self.project_id = project_id
        self.name = name
        self.client = client
        self.amount = amount
        self.status = status  # Pending, In Progress, Completed

    def to_dict(self):
        """Convert object to dictionary for saving."""
        return {
            "id": self.project_id,
            "name": self.name,
            "client": self.client,
            "amount": self.amount,
            "status": self.status
        }