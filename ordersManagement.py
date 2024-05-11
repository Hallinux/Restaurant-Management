import mysql.connector
import datetime 
from tabulate import tabulate
from databasRecords import  execute_query

 
def orders_management(cursor, connection):
    while True:
        print("\nOrders Management")
        print("╔═════════════════════════════╗")
        print("║ 1. Place Order              ║")
        print("║ 2. Update Order Status      ║")
        print("║ 3. View Orders              ║")
        print("║ 0. Back                     ║")
        print("╚═════════════════════════════╝")

        choice = input("Enter your choice: ")
        if choice == "1":
            customer_id = int(input("Enter customer ID: "))
            staff_id = int(input("Enter staff ID: "))
            item_id = int(input("Enter item ID: "))
            order_status = input("Enter order status (1 for True, 0 for False): ")
            order_date = datetime.datetime.now()

            try:
                cursor.execute("""
                    INSERT INTO Orders (customer_id, staff_id, item_id, order_status, order_date)
                    VALUES (%s, %s, %s, %s, %s)
                """, (customer_id, staff_id, item_id, order_status, order_date))
                connection.commit()
                print("Order placed successfully")
            except mysql.connector.Error as e:
                print(f"Error placing order: {e}")
        elif choice == "2":
            order_id = input("Enter the ID of the order to update: ")
            new_status = input("Enter the new order status (1 for True, 0 for False): ")
            try:
                cursor.execute("UPDATE Orders SET order_status = %s WHERE orders_id = %s", (new_status, order_id))
                connection.commit()
                print("Order status updated successfully")
            except mysql.connector.Error as e:
                print(f"Error updating order status: {e}")
        elif choice == "3":
            orders = execute_query(cursor, "SELECT * FROM Orders")
            print(tabulate(orders, headers="keys", tablefmt="pretty"))
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
 