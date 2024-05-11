from tabulate import tabulate
from databasRecords import get_records,Tot_cost_customer,get_orders_details,Employee_TokeOrderBy_date
from databasRecords import total_income ,find_customers,top_customer,most_sold_item_in_period
from builtins import input

def reports(cursor,connection):
 
    while True:
        print("\nReports")
        print("╔═══════════════════════════════════════════════╗")
        print("║ 1. View Tables                                ║")   #Done
        print("║ 2. View Total ordered by a customer           ║")   #done
        print("║ 3. Employee Toke order by date                ║")   #done
        print("║ 4. Get Orders Details                         ║")   #done
        print("║ 5. Top Customer                               ║")   #done
        print("║ 6. Top item                                   ║")   #done
        print("║ 7. Total income by date                       ║")   #done
        print("║ 8. Search Customer                            ║")   #done
        print("║ 0. Back                                       ║")          
        print("╚═══════════════════════════════════════════════╝")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Tables")
            print("╔════════════════════╗")
            print("║ 1. Employees       ║")
            print("║ 2. Customers       ║")
            print("║ 3. Menu            ║")
            print("║ 4. Orders          ║")
            print("║ 0. Back            ║")
            print("╚════════════════════╝")
            choice_table = input("Enter your choice: ")
            if choice_table == "1":
                employees = get_records(cursor, "Employees")
                print(tabulate(employees, headers="keys", tablefmt="pretty"))
            elif choice_table == "2":
                customers = get_records(cursor, "Customers")
                print(tabulate(customers, headers="keys", tablefmt="pretty"))
            elif choice_table == "3":
                menu = get_records(cursor, "Menu")
                print(tabulate(menu, headers="keys", tablefmt="pretty"))
            elif choice_table == "4":
                orders = get_records(cursor, "Orders")
                print(tabulate(orders, headers="keys", tablefmt="pretty"))
            elif choice_table == "0":
                break
            else:
                print("Invalid choice. Please try again.")

        elif choice == "2":
            customer_id = input("Enter customer ID: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            total_cost = Tot_cost_customer(cursor, customer_id, start_date, end_date)
            print(f"Total price: {total_cost}")

        elif choice == "3":
            employee_id = input("Enter employee ID: ")
            order_date = input("Enter order date (YYYY-MM-DD): ")
            employee = Employee_TokeOrderBy_date(cursor, employee_id, order_date)
            print(f"Employee {employee} took orders on {order_date}")

        elif choice == "4":
            order_details = get_orders_details(cursor )
            print(tabulate(order_details, headers="keys", tablefmt="pretty"))

        elif choice == "5":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            print("")
            print("Top Customer by total cost:")
            top_customer( cursor, start_date, end_date)
        elif choice == "6":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date =  input("Enter end date (YYYY-MM-DD): ")
            print("")
            print("Top item by total ordered:")
            item = most_sold_item_in_period( cursor, start_date, end_date)
            print(f"The most sold item is: {item}")
        elif choice == "7":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            print("")
            print("Total income by date:")
            total = total_income(cursor, start_date, end_date)
            print(f"The total income is: {total}")
        elif choice == "8":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            find_customers(cursor, first_name, last_name)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
 