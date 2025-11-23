from models import Project
from data_storage import save_data, load_data

class FreelanceManager:
    def __init__(self):
        self.projects = []
        raw_data = load_data()
        # Convert raw dicts back to Objects
        for item in raw_data:
            self.projects.append(Project(item['id'], item['name'], item['client'], item['amount'], item['status']))

    def add_project(self):
        """Interactively add a project (used by CLI)."""
        name = input("Project name: ").strip()
        client = input("Client name: ").strip()
        amount_raw = input("Amount (numeric): ").strip()
        try:
            amount = float(amount_raw)
        except ValueError:
            print("✘ Invalid amount. Project not added.")
            return

        new_id = len(self.projects) + 1
        new_proj = Project(new_id, name, client, amount)
        self.projects.append(new_proj)
        save_data(self.projects)
        print(f"✔ Project '{name}' added!")

    def view_projects(self):
        if not self.projects:
            print("No projects found.")
            return
        print(f"{'ID':<5} {'Project':<20} {'Client':<15} {'Amount':<10} {'Status'}")
        print("-" * 60)
        for p in self.projects:
            print(f"{p.project_id:<5} {p.name:<20} {p.client:<15} ${p.amount:<9} {p.status}")

    def update_status(self):
        proj_id = input("Enter Project ID to update: ").strip()
        for p in self.projects:
            if str(p.project_id) == str(proj_id):
                print(f"Current Status: {p.status}")
                new_status = input("Enter new status (Pending/In Progress/Completed): ").strip()
                p.status = new_status
                save_data(self.projects)
                print("✔ Status updated!")
                return
        print("✘ Project ID not found.")

    def generate_report(self):
        total_income = sum(p.amount for p in self.projects if p.status == "Completed")
        pending_income = sum(p.amount for p in self.projects if p.status != "Completed")
        
        print("\n--- FINANCIAL REPORT ---")
        print(f"Total Earnings (Completed): ${total_income}")
        print(f"Projected Income (Pending): ${pending_income}")