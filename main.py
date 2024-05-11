from databaseConnection import connect_to_database
from feedback import customers_feedback
from reports import reports
from menuManagement import menu_management
from ordersManagement import orders_management
from employeesManagement import employees_management
from customersManagement import customers_management
import mysql.connector

 
def display_main_menu():
    print("\nWelcome to Restaurant Management")
    print("╔══════════════════════════════╗")
    print("║ 1. Employees Management      ║")
    print("║ 2. Customers Management      ║")
    print("║ 3. Menu Management           ║")
    print("║ 4. Orders Management         ║")
    print("║ 5. Customers Feedback        ║")
    print("║ 6. Reports                   ║")
    print("║ 0. Exit                      ║")
    print("╚══════════════════════════════╝")



def main():
    try:
        
        connection = connect_to_database()
      
        cursor = connection.cursor(dictionary=True)

        while True:
            display_main_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                employees_management(cursor, connection)
            elif choice == "2":
                customers_management(cursor, connection)
            elif choice == "3":
                menu_management(cursor, connection)
            elif choice == "4":
                orders_management(cursor, connection)
            elif choice == "5":
                customers_feedback(cursor, connection)
            elif choice == "6":
                reports(cursor, connection)
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()
            print("Program exited")

if __name__ == "__main__":
    main()


