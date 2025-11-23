import json
import os

FILE_NAME = "database.json"

def save_data(projects):
    """Saves the list of project objects to a JSON file."""
    data = [p.to_dict() for p in projects]
    with open(FILE_NAME, 'w') as f:
        json.dump(data, f, indent=4)
    print("✔ Data saved successfully.")

def load_data():
    """Loads data from JSON."""
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, 'r') as f:
        try:
            data = json.load(f)
            return data
        except json.JSONDecodeError:
            return []