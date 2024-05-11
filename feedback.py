import mysql.connector
from tabulate import tabulate
from databasRecords import execute_query

def customers_feedback(cursor, connection):
    while True:
        print("\nCustomers Feedback")
        print("╔════════════════════════════════╗")
        print("║ 1. Add Feedback                ║")
        print("║ 2. View Feedback               ║")
        print("║ 0. Back                        ║")
        print("╚════════════════════════════════╝")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            customer_id = input("Enter the ID of the customer: ")
            feedback = input("Enter the feedback: ")
            try:
                cursor.execute("UPDATE Customers SET Feedback = %s WHERE customers_id = %s", (feedback, customer_id))
                connection.commit()
                print("Feedback added successfully")
            except mysql.connector.Error as e:
                print(f"Error adding feedback: {e}")
        elif choice == "2":
            feedback = execute_query(cursor, "SELECT customers_id, Feedback FROM Customers WHERE Feedback IS NOT NULL")
            print(tabulate(feedback, headers="keys", tablefmt="pretty"))
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
