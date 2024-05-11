import mysql.connector
import tabulate


def execute_query(cursor, query, data=None):
    try:
        cursor.execute(query, data)
        return cursor.fetchall()
    except mysql.connector.Error as e:
        raise e

def add_record(cursor, connection, table, data):
    try:
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, tuple(data.values()))
        connection.commit()
        print(f"Record added to {table} successfully")
    except mysql.connector.Error as e:
        raise e

def remove_record(cursor, connection, table, column, value):
    try:
        query = f"DELETE FROM {table} WHERE {column} = %s"
        cursor.execute(query, (value,))
        connection.commit()
        print(f"Record removed from {table} successfully")
    except mysql.connector.Error as e:
        raise e

def update_record(cursor, connection, table, record_id, column, new_value):
    try:
        query = f"UPDATE {table} SET {column} = %s WHERE {table}_id = %s"
        cursor.execute(query, (new_value, record_id,))
        connection.commit()
        print("Record updated successfully")
    except mysql.connector.Error as e:
        raise e
    
def get_records(cursor, table):
    try:
        query = f"SELECT * FROM {table}"
        cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as e:
        raise e
    
def Tot_cost_customer(cursor ,costumer_id, start_date, end_date):
    try:
        query = "SELECT Total_customers_cost(%s, %s, %s)"
        cursor.execute(query, (costumer_id, start_date, end_date))
        result = cursor.fetchone()
        key = f"Total_customers_cost('{costumer_id}', '{start_date}', '{end_date}')"
        price = result[key]
        return price
    except mysql.connector.Error as e:
        raise e
    
def Employee_TokeOrderBy_date(cursor, emoployee_id, order_date):
    try:
        query = "SELECT employee_TokeOrderBy_date(%s, %s)"
        cursor.execute(query, (emoployee_id, order_date))
        result = cursor.fetchone()
        key = f"employee_TokeOrderBy_date('{emoployee_id}', '{order_date}')"
        count = result[key]
        return count
    except mysql.connector.Error as e:
        raise e
    
def get_orders_details(cursor ):
    try:
        query = """
        SELECT 
        Orders.orders_id,
        Customers.first_name AS customer_first_name,
        Customers.last_name AS customer_last_name,
        Employees.first_name AS staff_first_name,
        Employees.employees_id AS employees_id,
        Menu.item_Name AS item_name,
        Menu.item_Price AS item_price,
        Orders.order_status,
        Orders.order_date
        FROM 
            Orders
        JOIN 
            Customers ON Orders.customer_id = Customers.customers_id
        JOIN 
            Employees ON Orders.staff_id = Employees.employees_id
        JOIN 
            Menu ON Orders.item_id = Menu.menu_id;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        if not result:
            print("No orders found ")
        return result
    except mysql.connector.Error as e:
        raise e
     
def top_customer(cursor, start_date, end_date):
    try:
        query = """
        SELECT 
            Customers.first_name AS customer_first_name,
            Customers.last_name AS customer_last_name,
            SUM(Menu.item_Price) AS total_cost
        FROM 
            Orders
        JOIN 
            Menu ON Orders.item_id = Menu.menu_ID
        JOIN 
            Customers ON Orders.customer_id = Customers.customers_id
        WHERE 
            Orders.order_date BETWEEN %s AND %s
        GROUP BY 
            Orders.customer_id
        ORDER BY 
            total_cost DESC
        LIMIT 1;
        """
        cursor.execute(query, (start_date, end_date))
        result = cursor.fetchone()
        if result:
            print(f"Customer Name: {result['customer_first_name']} {result['customer_last_name']}")
            print(f"Total Cost: {result['total_cost']}")
        else:
            print("No orders found within the specified date range.")
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")

def most_sold_item_in_period(cursor, start_date, end_date):
    try:
        query = "SELECT most_sold_item_in_period(%s, %s)"
        cursor.execute(query, (start_date, end_date))
        result = cursor.fetchone()
        key = f"most_sold_item_in_period('{start_date}', '{end_date}')"
        count = result[key]
        return count
    except mysql.connector.Error as e:
        raise e

def total_income(cursor, start_date, end_date):
    try:
        query = "SELECT calculate_total_income_by_period(%s, %s)"
        cursor.execute(query, (start_date, end_date))
        result = cursor.fetchone()
        key = f"calculate_total_income_by_period('{start_date}', '{end_date}')"
        income = result[key]
        return income
    except mysql.connector.Error as e:
        raise e

def find_customers(cursor, first_name, last_name):
    try:
        cursor.callproc("find_customers", [first_name, last_name])
        results = cursor.stored_results()
        if results:
            for result in results:
                rows = result.fetchall()
                if rows:
                    headers = rows[0].keys()
                    data = [row.values() for row in rows]
                    print(tabulate.tabulate(data, headers, tablefmt="grid"))
                else:
                    print("No customer with this first and lastname found in the database.")
        else:
            print("No customer with this first and lastname found in the database.")
    except mysql.connector.Error as e:
        raise e

        


    
