import mysql.connector
from databaseConnection import connect_to_database

try:
    connection = connect_to_database()
    if connection.is_connected():
        print("Connected to MySQL database")
        
        # Create cursor object to execute SQL queries
        cursor = connection.cursor()


 
#####################################################################3
# Find the total cost of all orders for a specific customer
#####################################################################3


    cursor.execute(""" drop FUNCTION IF EXISTS Total_customers_cost;""")
    cursor.execute("""
        CREATE FUNCTION Total_customers_cost(customer_id_input INT, start_date DATE, end_date DATE)
        RETURNS DECIMAL(10, 2)
        DETERMINISTIC
        BEGIN
            DECLARE total_cost DECIMAL(10, 2);
            SELECT SUM(Menu.item_Price) INTO total_cost
            FROM Orders
            INNER JOIN Menu ON Orders.item_id = Menu.menu_ID
            WHERE Orders.customer_id = customer_id_input;
            RETURN total_cost;
        END  ; 
                   """)
    connection.commit()




########################################################### #
#a function that count the number of an employees toke order in a specific date
############################################################
    cursor.execute("""
    DROP FUNCTION IF EXISTS employee_TokeOrderBy_date;
    """)
    cursor.execute("""
        CREATE FUNCTION employee_TokeOrderBy_date(Employees_id_input INT, TheDate date)
        RETURNS INT
        DETERMINISTIC
        BEGIN
            DECLARE counter int;
            select COUNT(*) into counter
            from Orders
            where staff_id = Employees_id_input
            and  date(order_date) = TheDate;
            RETURN counter;
        END;
    """)
    connection.commit()

##############################################################################
# Find the most sold item in a specific period  
##############################################################################

    cursor.execute("""DROP FUNCTION IF EXISTS most_sold_item_in_period;""")
    cursor.execute("""
 
    CREATE FUNCTION most_sold_item_in_period(start_date DATE, end_date DATE)
    RETURNS VARCHAR(50) 
    DETERMINISTIC
    BEGIN 
        DECLARE most_sold_item_name VARCHAR(50);
        
        SELECT Menu.item_name INTO most_sold_item_name
        FROM (
            SELECT item_id, COUNT(*) AS num_orders
            FROM Orders
            WHERE order_date BETWEEN start_date AND end_date
            GROUP BY item_id
            ORDER BY num_orders DESC
            LIMIT 1
        ) AS most_sold_item
        JOIN Menu ON most_sold_item.item_id = Menu.menu_ID;
        
        RETURN most_sold_item_name;
    END;
    """)
    connection.commit()

###############################################################################
# Find total Income by period
###############################################################################

    cursor.execute("""drop FUNCTION IF EXISTS calculate_total_income_by_period;""")
    cursor.execute("""
                   CREATE FUNCTION calculate_total_income_by_period(start_date DATE, end_date DATE)
    RETURNS DECIMAL(10, 2)
    DETERMINISTIC
    BEGIN
        DECLARE total_income DECIMAL(10, 2);
        
        SELECT SUM(Menu.item_Price) INTO total_income
        FROM Orders
        JOIN Menu ON Orders.item_id = Menu.menu_ID
        WHERE Orders.order_date BETWEEN start_date AND end_date;
        
        RETURN total_income;
    END;
 
                   """)


    connection.commit()

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")



