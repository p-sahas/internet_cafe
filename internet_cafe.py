import random
from datetime import datetime
import os
#Variables
items = []   # List of Items in the items
selected_dealers = []  # Randomly selected dealers
all_dealers = []   # All of the dealers


def val_item_code(item_code):
    # Function for Validate if the item_code is numeric and it not already used.
    if not item_code.isdigit():
        return False, "Item code must be numeric"
    # Check if the item code is already in use
    for item in items:
        if item['item_code'] == item_code:
            return False, "Item code already exists"
    return True, ""


def val_price(price_str):
    # Validate if the price string is a valid float.
    try:
        price = float(price_str)
        if price < 0:
            return False
        return True
    except ValueError:
        return False


def val_quantity(qty_str):
    # Validate if the quantity string is a valid integer.
    try:
        qty = int(qty_str)
        if qty < 0:
            return False
        return True
    except ValueError:
        return False


def val_date(date_str):
    # Validate if the date string is in the right format YYYY/MM/DD.
    try:
        datetime.strptime(date_str, '%Y/%m/%d')
        return True
    except ValueError:
        return False


def load_items():
    # Load items from the text file.
    global items
    items = []
    try:
        # Check if 'items.txt' file exists
        if os.path.exists('items.txt'):
            with open('items.txt', 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(',')  # Split the lines using commas
                        if len(parts) >= 7:
                            item = {
                                'item_code': parts[0].strip(),
                                'item_name': parts[1].strip(),
                                'item_brand': parts[2].strip(),
                                'price': float(parts[3].strip().split('Rs ')[1] if 'Rs ' in parts[3] else parts[3].strip()),
                                'quantity': int(parts[4].strip()),
                                'category': parts[5].strip(),
                                'purchased_date': parts[6].strip()
                            }
                            items.append(item)
    except Exception as e:
        print(f"Error loading items: {e}")

#Function for a display header table for items
def display_header():
    # Print header for show items
    print("-" * 97)
    print(
        f"{'Code':<6}"
        f" {'Name':<20} {'Brand':<15} {'Price (Rs)':<15}"
        f" {'Qty':<5} {'Category':<15} {'Purchased Date':<15}")
    print("-" * 97)


# Function for a display items according to display_header function table.
def display_item(item):
    # Print item details
    print(f"{item['item_code']:<6}"
          f" {item['item_name'][:18]:<20} {item['item_brand'][:13]:<15} "
          f"{item['price']:<15.2f} {item['quantity']:<5} "
          f"{item['category'][:13]:<15} {item['purchased_date']:<15}")



def save_items():
    # Save items to the text file from items list.
    try:
        with open('items.txt', 'w') as file:
            for item in items:
                file.write(f"{item['item_code']},"
                           f" {item['item_name']},"
                           f" {item['item_brand']},"
                           f" Rs {item['price']:.2f},"
                           f" {item['quantity']},"
                           f" {item['category']},"
                           f" {item['purchased_date']}\n")
        print("Item details saved successfully!")
    except Exception as e:
        print(f"Error saving items: {e}")


def add_item(): #add_item == AID
    #Function for adding new items to the inverntory
    print("\n==== ADD ITEM DETAILS ====\n")

    while True:
        item_code = input("Enter Item Code: ").strip()
        valid, error_message = val_item_code(item_code)
        #Validating item code using the function made earlier as val_item_code
        if valid:
            break
        print(f"Invalid item code: {error_message}")

    item_name = input("Enter Item Name: ").strip()
    while not item_name:
        print("Item name cannot be empty!")
        item_name = input("Enter Item Name: ").strip()

    item_brand = input("Enter Item Brand: ").strip()
    while not item_brand:
        print("Item brand cannot be empty!")
        item_brand = input("Enter Item Brand: ").strip()

    while True:
        # Remove spaces when entering input in price using replace function.
        price_str = input("Enter Price (Rs): ").strip().replace(" ", "")
        if val_price(price_str):
            price = float(price_str)
            break
        print("Invalid price! Please enter a positive number.")

    while True:
        quantity_str = input("Enter Quantity: ").strip()
        if val_quantity(quantity_str):
            quantity = int(quantity_str)
            break
        print("Invalid quantity! Please enter a positive integer.")

    category = input("Enter Category: ").strip()
    while not category:
        print("Category cannot be empty!")
        category = input("Enter Category: ").strip()

    while True:
        purchased_date = input("Enter Purchased Date (YYYY/MM/DD): ").strip()
        if val_date(purchased_date):
            break
        print("Invalid date format! Please use YYYY/MM/DD.")

    #Creating dictionary for new items
    new_item = {
        'item_code': item_code,
        'item_name': item_name,
        'item_brand': item_brand,
        'price': price,
        'quantity': quantity,
        'category': category,
        'purchased_date': purchased_date
    }
    # append new_item dictionary into items list
    items.append(new_item)
    print("\nItem added successfully!")

    # Save items automatically
    save_items()

    input("\nPress Enter to continue...")


def delete_item():
    #Function for Delete an item from the inventory using item code.
    print("\n==== DELETE ITEM DETAILS ====\n")

    item_code = input("Enter Item Code to delete: ").strip()
    for i, item in enumerate(items):
        if item['item_code'] == item_code:
            print(f"\nItem Found: {item['item_code']}\n")
            display_header()
            display_item(item)  # Call display_item function for display requested item
            print("-" * 97)
            confirm = input("\nAre you sure you want to delete this item? (y/n): ").strip()

            if confirm.lower() == 'y':
                del items[i]
                print("Item deleted successfully!")
                save_items()  # Save items list into items file after deletion
            else:
                print("Deletion item cancelled.")

            input("\nPress Enter to continue...")
            return

    print(f"No item found with code: {item_code}")
    input("\nPress Enter to continue...")


def update_item():
    # Update an item's details using item code.
    print("\n==== UPDATE ITEM DETAILS ====\n")
    item_code = input("Enter Item Code to update: ").strip()
    for i, item in enumerate(items):
        if item['item_code'] == item_code:
            print(f"\nItem Found: {item['item_code']}\n")
            display_header()
            display_item(item)  # Call display_item function for display requested item
            print("-" * 97)
            print("Enter new details (press Enter to keep current value):\n")

            new_name = input(f"Item Name [{item['item_name']}]: ").strip()
            if new_name:
                item['item_name'] = new_name

            new_brand = input(f"Item Brand [{item['item_brand']}]: ").strip()
            if new_brand:
                item['item_brand'] = new_brand

            while True:
                new_price = input(f"Price (Rs) [{item['price']}]: ").strip().replace(" ", "")
                if not new_price:
                    break
                if val_price(new_price):
                    item['price'] = float(new_price)
                    break
                print("Invalid price! Please enter a positive number.")

            while True:
                new_quantity = input(f"Quantity [{item['quantity']}]: ")
                if not new_quantity:
                    break
                if val_quantity(new_quantity):
                    item['quantity'] = int(new_quantity)
                    break
                print("Invalid quantity! Please enter a positive integer.")

            new_category = input(f"Category [{item['category']}]: ").strip()
            if new_category:
                item['category'] = new_category

            while True:
                new_date = input(f"Purchased Date [{item['purchased_date']}] (YYYY/MM/DD): ").strip()
                if not new_date:
                    break
                if val_date(new_date):
                    item['purchased_date'] = new_date
                    break
                print("Invalid date format! Please use YYYY/MM/DD.")

            print("\nItem updated successfully!")
            save_items()  # Auto save after updating an item

            input("\nPress Enter to continue...")
            return

    print(f"No item found with code: {item_code}")
    input("\nPress Enter to continue...")


def view_items():
    # View all the items sorted by category in ascending order.
    print("\n===== VIEW ITEMS TABLE =====\n")

    if not items:
        print("No items in inventory.")
        input("\nPress Enter to continue...")
        return

    # Sort items by category in ascending order using bubble sort
    sorted_items = items.copy()
    n = len(sorted_items)
    # Bubble sort by 'category'
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_items[j]['category'].lower() > sorted_items[j + 1]['category'].lower():
                sorted_items[j], sorted_items[j + 1] = sorted_items[j + 1], sorted_items[j]

    # Calculate total value of items
    total_value = sum(item['price'] * item['quantity'] for item in items)
    display_header()
    for item in sorted_items:
        display_item(item)
    print('-'*97)
    print(f"\nTotal Value of Inventory: Rs {total_value:.2f}")

    input("\nPress Enter to continue...")


def load_dealers():
    # Load the dealers from the dealers.txt text file and Create the dealers.txt file if it doesn't exist.
    global all_dealers
    all_dealers = []

    # Check if dealers.txt exists, create it if not exists yet.
    if not os.path.exists('dealers.txt'):
        try:
            with open('dealers.txt', 'w') as file:
                # Create empty file if dealers.txt not created yet
                pass
            print("dealers.txt file was created successfully.")
        except Exception as e:
            print(f"Error creating dealers.txt file: {e}")

    try:   # Reading dealers data from dealers.txt
        with open('dealers.txt', 'r') as file:
            lines = file.readlines()
            if not lines:
                print("Warning: The dealers.txt file is empty. No dealers to load.")
                return

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                if ';' in line:
                    main_info, items_str = line.split(';', 1)
                else:
                    main_info = line
                    items_str = ""

                main_parts = main_info.split(',')
                if len(main_parts) < 3:
                    continue  # Skip invalid lines

                dealer_name = main_parts[0].strip()
                contact = main_parts[1].strip()
                location = main_parts[2].strip()

                dealer_items = []
                if items_str:
                    item_parts = items_str.split(';')
                    for item in item_parts:
                        item_data = item.split(',')
                        if len(item_data) == 4:
                            dealer_item = {
                                'name': item_data[0].strip(),
                                'brand': item_data[1].strip(),
                                'price': float(item_data[2].strip()),
                                'quantity': int(item_data[3].strip())
                            }
                            dealer_items.append(dealer_item)

                        dealer = {
                            'name': dealer_name,
                            'contact': contact,
                            'location': location,
                            'items': dealer_items
                        }
                        all_dealers.append(dealer)

            if not all_dealers:
                print("Warning: No valid dealer records found in the file")

    except Exception as e:
        print(f"Error loading dealers: {e}")

def select_dealers():
    # Select four dealers randomly from the dealers file using random module.
    global selected_dealers

    print("\n=== SELECT DEALERS RANDOMLY ===\n")

    load_dealers()  # Load dealers from the dealers file

    if not all_dealers:
        print("No dealers available. Please add dealers to the dealers file first.")
        input("\nPress Enter to continue...")
        return

    if len(all_dealers) < 4:
        print(f"Not enough dealers available. Only {len(all_dealers)} dealers found.")
        print("At least 4 dealers are required for random selection.")
        input("\nPress Enter to continue...")
        return

    # Randomly select 4 dealers without duplicates
    # selected_dealers = random.sample(all_dealers,4)
    unique_dealers = {dealer['name']: dealer for dealer in all_dealers}.values()
    # Select 4 random dealers from the unique list
    selected_dealers = random.sample(list(unique_dealers), 4)
    print("4 Dealers are Selected Randomly!")
    input("\nPress Enter to continue...")


def view_selected_dealers():
    # View randomly selected dealers sorted by location using bubble sort.
    print("\n=== VIEW RANDOMLY SELECTED DEALERS ===\n")

    if not selected_dealers:
        print("No dealers have been selected yet. Please use SDD option first.")
        input("\nPress Enter to continue...")
        return

    # Sort dealers by location using bubble sort
    dealers = selected_dealers.copy()
    n = len(dealers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if dealers[j]['location'].lower() > dealers[j + 1]['location'].lower():
                dealers[j], dealers[j + 1] = dealers[j + 1], dealers[j]

    # Display sorted dealers
    for dealer in dealers:
        print(f"Name: {dealer['name']}")
        print(f"Contact: {dealer['contact']}")
        print(f"Location: {dealer['location']}")
        print("Items:")   # Display dealers selling items
        for item in dealer['items']:
            print(f"  - {item['name']} "
                  f"({item['brand']}) - Rs {item['price']:.2f} x {item['quantity']}")

        print("-" * 50)

    input("\nPress Enter to continue...")


def display_dealer_items():
    # Display items of a specific dealer.
    print("\n=== DISPLAY DEALER ITEMS ===\n")

    if not selected_dealers:
        print("No dealers have been selected yet. Please use SDD option first.")
        input("\nPress Enter to continue...")
        return

    # List available dealers
    print("Available Dealers:")
    for i, dealer in enumerate(selected_dealers, 1):
        print(f"{i}. {dealer['name']} ({dealer['location']})")

    # Get dealer selection
    try:
        choice = input("\nEnter dealer name: ").strip()
        dealer_found = False

        for dealer in selected_dealers:
            if dealer['name'].lower() == choice.lower():
                dealer_found = True
                # Display header Detials on dealers
                print(f"\nItems from {dealer['name']} ({dealer['location']}):")
                print(f"{'Name':<20} {'Brand':<15} {'Price (Rs)':<15} {'Quantity':<10}")
                print("=" * 60)
                # Display items Dealers selling
                for item in dealer['items']:
                    print(f"{item['name']:<20} {item['brand']:<15} {item['price']:<15.2f} {item['quantity']:<10}")
                break

        if not dealer_found:
            print(f"No dealer found with name: {choice}")

    except Exception as e:
        print(f"Error: {e}")

    input("\nPress Enter to continue...")


def display_menu():
    # Display the main menu for user to interact with the functions in the program.
    print("\n=== ONE NET CAFE INVENTORY SYSTEM ===\n")
    print("AID - Add Item Details")
    print("DID - Delete Item Details")
    print("UID - Update Item Details")
    print("VID - View Items Table")
    print("SID - Save Item Details")
    print("SDD - Select Dealers Randomly")
    print("VRL - View Randomly Selected Dealers")
    print("LDI - List Dealer Items")
    print("ESC - Exit Program")
    print("\n======================================")

    choice = input("Enter your choice: ").upper().strip()
    return choice


def main():
    # Assigning inputs for Main program functions.
    # Load initial data in items file
    load_items()

    while True:
        choice = display_menu()

        if choice == "AID":
            add_item()
        elif choice == "DID":
            delete_item()
        elif choice == "UID":
            update_item()
        elif choice == "VID":
            view_items()
        elif choice == "SID":
            save_items()
            input("\nPress Enter to continue...").strip()
        elif choice == "SDD":
            select_dealers()
        elif choice == "VRL":
            view_selected_dealers()
        elif choice == "LDI":
            display_dealer_items()
        elif choice == "ESC":
            print("\nThank you for using One Net Cafe Inventory System!")
            break
        else:
            print("\nInvalid choice! Please try again.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()

