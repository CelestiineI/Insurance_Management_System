from product import main as manage_products # Import product management functions
from policyholder import policyholder_menu as manage_policyholders # Import policyholder management functions
from payment import main as manage_payments # Import payment processing functions

# Step 1: Define the Insurance class
# This class will serve as the main entry point for the program
class Insurance:
    def __init__(self):
        print("Welcome to the Insurance Management System")
        self.is_logged_in = False  # Initialize login status

    def login(self):
        # Simulate a login process; use below credentials for testing
        # In a real application, process would check against a database or secure storage
        admin_username = "admin"
        admin_password = "password123"

        # Prompt for login credentials
        print("Please log in to access the system.")
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")

        if username == admin_username and password == admin_password:
            self.is_logged_in = True
            print("Login successful!")
        else:
            print("Invalid credentials. Please try again.")
            self.login()
        if not self.is_logged_in:
            print("You must log in to access the system.")
            return  

    def logout(self):
    # Simulate a logout process
        self.is_logged_in = False
        print("You have been logged out.")  
         
# Step 2: Define the run method to display the main menu
# This method will be called to start the program
    def run(self):
        while True:
            if not self.is_logged_in:
                self.login()    
                continue
            
            # Display the main menu     
            print("\nInsurance Management System")
            print("1. Manage Products")
            print("2. Manage Policyholders")
            print("3. Process Payments")
            print("4. Logout")

            choice = input("Choose an option (1-4): ")

            if choice == '1':
                manage_products()  # Call the product management function

            elif choice == '2':
                manage_policyholders()  # Call the policyholder management function

            elif choice == '3':
                manage_payments()  # Call the payment processing function

            elif choice == '4':
                self.logout()  # Call the logout function
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__": # This ensures the main function runs only when the script is executed directly
    # Create an instance of the Insurance class and run the program
    insurance = Insurance()
    insurance.run()