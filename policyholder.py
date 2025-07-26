import json # for JSON handling
import os   # for file operations

POLICYHOLDER_FILE = 'policyholders.json' # File to store policyholders
policyholders = []  # List to hold policyholder objects

#Step 1: Define the Policyholder class
# The class is used to manage policyholders, including their name, age, policy number, and active status
class Policyholder:
    def __init__(self, name, age, policy_number, active=True): # Initialize with name, age, policy number, and active status
        self.name = name.title()
        self.age = age
        self.policy_number = policy_number
        self.active = active

    def suspend(self):  # Method to suspend the policyholder
        self.active = False

    def reactivate(self): # Method to reactivate the policyholder
        self.active = True

    def to_dict(self):  # Convert the object to a dictionary for JSON serialization
        return {
            "name": self.name,
            "age": self.age,
            "policy_number": self.policy_number,
            "active": self.active
        }

    @staticmethod # Static method to create a Policyholder from a dictionary
    def from_dict(data):
        return Policyholder(
            data["name"],
            data["age"],
            data["policy_number"],
            data["active"]
        )

    def __str__(self):  # String representation of the Policyholder object
        status = "Active" if self.active else "Suspended"
        return f"{self.name} (Age: {self.age}, Policy #: {self.policy_number}, Status: {status})"

# Step 2: Functions to manage policyholders

def save_policyholders():   # Save the current list of policyholders to a JSON file
    with open(POLICYHOLDER_FILE, 'w') as f:
        json.dump([p.to_dict() for p in policyholders], f, indent=4)

def load_policyholders():   # Load policyholders from the JSON file
    global policyholders
    if os.path.exists(POLICYHOLDER_FILE):
        with open(POLICYHOLDER_FILE, 'r') as f:
            data = json.load(f)
            policyholders = [Policyholder.from_dict(p) for p in data]

def is_policyholder_active(name): # Check if a policyholder is active
    load_policyholders()  
    for p in policyholders:
        if p.name.lower() == name.lower():
            return p.active
    return False  # If not found

def add_policyholder(): # Function to add a new policyholder
    name = input("Enter name: ").title()
    age = input("Enter age: ")
    policy_number = input("Enter policy number: ")
    policyholder = Policyholder(name, age, policy_number)
    policyholders.append(policyholder)
    save_policyholders()
    print("✅ Policyholder added.")

def display_policyholders():    # Function to display all policyholders
    if not policyholders:
        print("No policyholders found.")
    else:
        print("\n All Policyholders:")
        for p in policyholders:
            print(p)

def suspend_policyholder(): # Function to suspend a policyholder
    name = input("Enter policyholder name to suspend: ").title()
    for p in policyholders:
        if p.name == name:
            p.suspend()
            save_policyholders()
            print("✅ Policyholder suspended.")
            return
    print("❌ Policyholder not found.")

def reactivate_policyholder():  # Function to reactivate a suspended policyholder
    name = input("Enter policyholder name to reactivate: ").title()
    for p in policyholders:
        if p.name == name:
            p.reactivate()
            save_policyholders()
            print("✅ Policyholder reactivated.")
            return
    print("❌ Policyholder not found.")

def policyholder_menu():    # Main menu for policyholder management
    load_policyholders()
    while True:
        print("""
Policyholder Menu:
1. Add Policyholder
2. Display All Policyholders
3. Suspend Policyholder
4. Reactivate Policyholder
5. Exit
""")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_policyholder()
        elif choice == "2":
            display_policyholders()
        elif choice == "3":
            suspend_policyholder()
        elif choice == "4":
            reactivate_policyholder()
        elif choice == "5":
            print("Exiting policyholder system.")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__": # This ensures the main function runs only when the script is executed directly
    policyholder_menu() # Start the policyholder management system

