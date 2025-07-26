# Insurance_Management_System
These are modular scripts that manages insurance products, policyholders, and associated payments made by the policy holders. The functionalities in these scripts include adding products and policyholders, managing policyholders (suspension and reactivation), processing payments, and tracking penalties for overdue payments and balances.
Files System:
All files reside in the same folder (Module 3 Assignment); there are four Python hardcoded files and five automatically generated data files, these are:

	Python Files: 
-	`insurance.py`: Provides the interface to access functionalities in all other files; it is the main entry point for the application
-	`product.py`: Provides functionalities for managing products including adding, updating, removal and display of products
-	`policyholder.py`: Manages policyholder the creation, suspension, reactivation, storage of policyholders
-	`payment.py`: Processes payment, calculates penalties, and stores payments

Auto-Generated Data Files
-	`products.json`: Automatically created to store initialized product data
-	`policyholder.json`: Stores the state of all created policyholders
-	`policyholder.txt`: Used for maintaining a readable text log of policyholders
-	`payments.pkl`: A binary file used to persist payment data using Python’s `pickle` module

Perquisites:  Python Installed

Instructions: 
-	Firstly, run `insurance.py` to launch the menu for interfacing with all class files and functionalities
-	Use the provided log=in credential below to log-in into the system
Username: admin
Password: password123
-	Choose from the options to manage policyholders, make payments, or view records
-	Data developed are saved and reloaded automatically through the modules
-	Payments include automatic due date tracking and penalty calculations for overdue or incomplete payments
-	Products and policyholders must exist before payments can be processed. Four products have already been hardcoded in `product.py` script to enable the process of testing

Features: 
-	Ensure that all modules (`product.py`, `policyholder.py`, `payment.py`, and `insurance.py`) are located in the same directory
-	The system will automatically generate and update the required data files to maintain consistency across runs
-	Scripts contain date and timestamps to records when key activities are executed (audit feature)
-	Robust user interface 

Policy Demonstration: 
Demonstration of the program was conducted by registering some policyholders who paid for products. 
Their records are saved in the auto-generated files in the directory, and these are available/visible (on the console) when the respective scripts are run
