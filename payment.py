import pickle   #For serializing and deserializing Python objects
import json       #For handling JSON data
import os        #For file operations
from datetime import datetime, timedelta #For handling dates and times
from product import initialize_products, display_products, products, get_product_cost   #For product management
from policyholder import policyholders, is_policyholder_active, load_policyholders #For policyholder management

PAYMENT_FILE = "payments.pkl" # File to store payment data, this file will be automatically created if it doesn't exist

# Step 1: Define the Payment class
class Payment:
    def __init__(self, policyholder, product_name, amount_paid, payment_date=None):
        self.policyholder = policyholder
        self.product_name = product_name.title()
        self.amount_paid = amount_paid
        self.payment_date = payment_date or datetime.now()
        self.due_date = self.payment_date + timedelta(days=30)
        self.penalty = 0.0

    #Method to calculate penalty if payment is overdue
    # This method checks if the payment is overdue and calculates the penalty based on the amount paid
    def calculate_penalty(self):
        product_cost = get_product_cost(self.product_name)
        if datetime.now() > self.due_date and self.amount_paid < product_cost:
            overdue_days = (datetime.now() - self.due_date).days
            self.penalty = round(0.02 * (product_cost - self.amount_paid) * overdue_days, 2)
        else:
            self.penalty = 0.0
        return self.penalty

    def __str__(self):
        self.calculate_penalty()
        product_cost = get_product_cost(self.product_name)
        balance = product_cost - self.amount_paid
        status_line = f"💰 Balance Remaining: ${balance:.2f}" if balance > 0 else "✅ Fully Paid"

        return (f"Payment by {self.policyholder} for {self.product_name}:\n"
                f"  Amount Paid: ${self.amount_paid:.2f}\n"
                f"  Due Date: {self.due_date.strftime('%Y-%m-%d')}\n"
                f"  Penalty: ${self.penalty:.2f}\n"
                f"  {status_line}")

# Load existing payments from file
def load_payments():
    global payments
    if os.path.exists(PAYMENT_FILE):
        with open(PAYMENT_FILE, "rb") as f:
            payments.extend(pickle.load(f))

# Save current payments to file
def save_payments():
    with open(PAYMENT_FILE, "wb") as f:
        pickle.dump(payments, f)

#Step 2: Initialize payments list
# This list will hold all payment objects
payments = []   # List to hold payment objects
load_payments() # Load existing payments from payments.pkl file

def process_payment(): # Function to process a payment
    load_policyholders()    # Load policyholders to check if the policyholder exists
    policyholder = input("Enter policyholder name: ").title()
    
    if not is_policyholder_active(policyholder):
        print("❌ Policyholder not found or is suspended.")
        return

    display_products()  # Display available products for payment
    product_name = input("Enter product name to pay for: ").title()
    cost = get_product_cost(product_name)
    
    if cost is None:
        print("❌ Invalid product.")
        return

    try:
        amount_paid = float(input(f"Enter amount to pay (Product costs ${cost:.2f}): "))
        if amount_paid <= 0:
            print("❌ Payment must be positive.")
            return
    except ValueError:
        print("❌ Invalid amount.")
        return

# Create a new payment object and add it to the payments list
    payment = Payment(policyholder, product_name, amount_paid)
    payments.append(payment)
    save_payments()
    print("✅ Payment recorded.")
    print(payment)

# Function to check reminders and penalties for overdue payments
def check_reminders_and_penalties():
    if not payments:
        print("No payments found.")
        return

    print("\n Reminders and Penalties:")
    for p in payments:
        p.calculate_penalty()
        if datetime.now() > p.due_date and p.amount_paid < get_product_cost(p.product_name):
            print(f"⏰ Reminder: {p.policyholder} has overdue payment for {p.product_name}.")
        print(p)

# Step 3: Main menu for payment processing
def payment_menu():
    initialize_products()
    load_policyholders()
    while True:
        print("""
Payment Menu:
1. Make Payment
2. Show All Payments & Penalties
3. Display Products
4. Exit
""")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            process_payment()
        elif choice == "2":
            check_reminders_and_penalties()
        elif choice == "3":
            display_products()
        elif choice == "4":
            print("Exiting payment system.")
            break
        else:
            print("❌ Invalid option. Try again.")

def main():
    payment_menu()

if __name__ == "__main__":
    main()

