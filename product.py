from datetime import datetime   #For handling dates and times

#Step 1 Define the Product class
#The class is used to manage insurance products, including their name, price, and dates of creation and updates
class Product:
    def __init__(self, name, price):    # Initialize with name and price
        self.name = name.title()  
        self.price = price
        self.date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Store the date when the product was added, in the format YYYY-MM-DD HH:MM:SS
        self.date_updated = None # Store the date when the product was last updated, initially None

    def __str__(self): # String representation of the Product object
        updated = f", Updated: {self.date_updated}" if self.date_updated else ""
        return f"Product(Name: {self.name}, Price: ${self.price:.2f}, Added: {self.date_added}{updated})"

products = []   #List to hold product objects
products_initialized = False  # Flag to avoid re-initialization

# Function to get the cost of a product by its name
# This function is used in payment.py to retrieve the cost of a product for payment processing
def get_product_cost(name):
    for product in products:
        if product.name.strip().lower() == name.strip().lower(): #Compare names in a case-insensitive manner and ignore leading/trailing spaces
            return product.price
    return None

# Function to initialize products with predefined values
# This function is called in product.py to ensure products are available for management
def initialize_products():
    global products, products_initialized
    if not products_initialized:
        predefined_products = [
            ("Plan A", 150.00),
            ("Plan B", 250.00),
            ("Plan C", 350.00),
            ("Plan D", 450.00),
        ]
        for name, price in predefined_products:
            products.append(Product(name, price))
        products_initialized = True

# Function to add a new product
def update_product(name, new_name=None, new_price=None):
    for product in products:
        if product.name.strip().lower() == name.strip().lower():
            if new_name:
                product.name = new_name.title()
            if new_price is not None:
                product.price = new_price
            product.date_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
    return False

# Function to remove a product by name
def remove_product(name):
    global products
    products = [p for p in products if p.name.strip().lower() != name.strip().lower()]

# Function to display all products
def display_products():
    if not products:
        print("No products available.")
    else:
        for product in products:
            print(product)

#Step 2: Main function to manage products
# This function is called in insurance.py to provide a menu for product management  
# This function is called in product.py to provide a menu for product management
def main():
    initialize_products()

    while True:
        print("\nProduct Management Menu:") 
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. Display Products")
        print("5. Exit")

        choice = input("Choose an option (1–5): ").strip()  #

# Validate user inputs
        if choice == "1":   # Add a new product
            name = input("Enter product name: ").title()
            while True:
                try:
                    price = float(input("Enter product price: "))
                    break
                except ValueError:
                    print("Please enter a numerical value for price.")
            products.append(Product(name, price))
            print(f"Product ({name} of price ${price:.2f}) added successfully.")

        elif choice == "2": # Update an existing product
            name = input("Enter product name to update: ").title()
            new_name = input("Enter new product name (leave blank to keep current): ")
            new_price_input = input("Enter new product price (leave blank to keep current): ")

            try:
                new_price = float(new_price_input) if new_price_input else None 
                if update_product(name, new_name, new_price):
                    print("Product updated successfully.")
                else:
                    print("Product not found.")
            except ValueError:
                print("Invalid price entered. Product not updated.")

        elif choice == "3": # Remove a product
            name = input("Enter product name to remove: ").title()
            remove_product(name)
            print("Product removed.")

        elif choice == "4": # Display all products
            print("\nAvailable Products:")
            display_products()

        elif choice == "5":
            print("Exiting product menu.")
            break

        else:
            print("Invalid option. Please choose 1–5.")

if __name__ == "__main__":
    main()

