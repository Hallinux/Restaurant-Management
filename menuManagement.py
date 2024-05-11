import mysql.connector
from tabulate import tabulate
from databasRecords import  execute_query
    
def menu_management (cursor, connection):
    while True:
        print("\nMenu Management")
        print("╔═══════════════════════════╗")
        print("║ 1. Add Menu Item          ║")
        print("║ 2. Remove Menu Item       ║")
        print("║ 3. Update Menu Item       ║")
        print("║ 4. View Menu              ║")
        print("║ 0. Back                   ║")
        print("╚═══════════════════════════╝")


        choice = input("Enter your choice: ")
        if choice == "1":
            item_name = input("Enter item name: ")
            item_description = input("Enter item description: ")
            item_price = float(input("Enter item price: "))
            try:
                cursor.execute("""
                    INSERT INTO Menu (item_Name, item_Description, item_Price)
                    VALUES (%s, %s, %s)
                """, (item_name, item_description, item_price))
                connection.commit()
                print("Menu item added successfully")
            except mysql.connector.Error as e:
                print(f"Error adding menu item: {e}")
        elif choice == "2":
            item_id = input("Enter the ID of the item to remove: ")
            try:
                cursor.execute("DELETE FROM Menu WHERE menu_ID = %s", (item_id,))
                connection.commit()
                print("Menu item removed successfully")
            except mysql.connector.Error as e:
                print(f"Error removing menu item: {e}")
        elif choice == "3":
            item_id = input("Enter the ID of the item to update: ")
            print("1. Update Item Name")
            print("2. Update Item Description")
            print("3. Update Item Price")
            update_choice = input("Enter your choice: ")
            if update_choice == "1":
                column = "item_Name"
            elif update_choice == "2":
                column = "item_Description"
            elif update_choice == "3":
                column = "item_Price"
            else:
                print("Invalid choice. Please try again.")
                continue
            new_value = input("Enter the new value: ")
            try:
                cursor.execute(f"UPDATE Menu SET {column} = %s WHERE menu_ID = %s", (new_value, item_id))
                connection.commit()
                print("Menu item updated successfully")
            except mysql.connector.Error as e:
                print(f"Error updating menu item: {e}")
        elif choice == "4":
            menu = execute_query(cursor, "SELECT * FROM Menu")
            print(tabulate(menu, headers="keys", tablefmt="pretty"))
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")