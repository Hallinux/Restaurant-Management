 
from tabulate import tabulate
from databasRecords import  execute_query , add_record, remove_record, update_record


def customers_management(cursor, connection):
    while True:
        print("\nCustomers Management")
        print("╔════════════════════════════════╗")
        print("║ 1. Add Customer                ║")
        print("║ 2. Remove Customer             ║")
        print("║ 3. Update Customer             ║")
        print("║ 4. View Customers              ║")
        print("║ 0. Back                        ║")
        print("╚════════════════════════════════╝")


        choice = input("Enter your choice: ")
        if choice == "1":
            customer_data = {
                "first_name": input("Enter customer first name: "),
                "last_name": input("Enter customer last name: "),
                "phone_number": input("Enter customer phone number: "),
                "address": input("Enter customer address: ")
            }
            add_record(cursor, connection, "Customers", customer_data)
        elif choice == "2":
            customer_id = input("Enter the ID of the customer to remove: ")
            remove_record(cursor, connection, "Customers", "customers_id", customer_id)
        elif choice == "3":
            customer_id = input("Enter the ID of the customer to update: ")
            print("1. Update First Name")
            print("2. Update Last Name")
            print("3. Update Phone Number")
            print("4. Update Address")
            update_choice = input("Enter your choice: ")
            if update_choice == "1":
                column = "first_name"
            elif update_choice == "2":
                column = "last_name"
            elif update_choice == "3":
                column = "phone_number"
            elif update_choice == "4":
                column = "address"
            else:
                print("Invalid choice. Please try again.")
                continue
            new_value = input("Enter the new value: ")
            update_record(cursor, connection, "Customers", customer_id, column, new_value)
        elif choice == "4":
            customers = execute_query(cursor, "SELECT * FROM Customers")
            print(tabulate(customers, headers="keys", tablefmt="pretty"))
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

 
            
