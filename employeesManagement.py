from tabulate import tabulate
from databasRecords import add_record, remove_record, update_record, execute_query
 
    
def employees_management(cursor, connection):
    while True:
        print("\nEmployees Management")
        print("╔══════════════════════════════╗")
        print("║ 1. Add Employee              ║")
        print("║ 2. Remove Employee           ║")
        print("║ 3. Update Employee           ║")
        print("║ 4. View Employees            ║")
        print("║ 0. Back                      ║")
        print("╚══════════════════════════════╝")

        choice = input("Enter your choice: ")
        if choice == "1":
            
            employee_data = {
                "first_name": input("Enter employee first name: "),
                "last_name": input("Enter employee last name: "),
                "phone_number": input("Enter employee phone number: "),
                "address": input("Enter employee address: "),
                "hire_date": input("Enter employee hire date (YYYY-MM-DD): ")
            }
            add_record(cursor, connection, "Employees", employee_data)

        elif choice == "2":
            employee_id = input("Enter the ID of the employee to remove: ")
            remove_record(cursor, connection, "Employees", "employees_id", employee_id)
        elif choice == "3":
            employee_id = input("Enter the ID of the employee to update: ")
            print("1. Update First Name")
            print("2. Update Last Name")
            print("3. Update Phone Number")
            print("4. Update Address")
            print("5. Update Hire Date")
            update_choice = input("Enter your choice: ")
            if update_choice == "1":
                column = "first_name"
            elif update_choice == "2":
                column = "last_name"
            elif update_choice == "3":
                column = "phone_number"
            elif update_choice == "4":
                column = "address"
            elif update_choice == "5":
                column = "hire_date"
            else:
                print("Invalid choice. Please try again.")
                continue
            new_value = input("Enter the new value: ")
            update_record(cursor, connection, "Employees", employee_id, column, new_value)

        elif choice == "4":
            employees = execute_query(cursor, "SELECT * FROM Employees")
            print(tabulate(employees, headers="keys", tablefmt="pretty"))
            
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")