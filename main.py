from manager import FreelanceManager
from utils import clear_screen

def main():
    app = FreelanceManager()
    
    while True:
        print("\n--- FREELANCE FLOW DASHBOARD ---")
        print("1. Add Project")
        print("2. View All Projects")
        print("3. Mark Project as Completed")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            clear_screen()
            app.add_project()
        elif choice == '2':
            clear_screen()
            app.view_projects()
        elif choice == '3':
            clear_screen()
            app.update_status()
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()