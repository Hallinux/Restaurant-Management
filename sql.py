import mysql.connector
from databaseConnection import connect_to_database

try:
    # Establish a connection to the database
    connection = connect_to_database()
    
    if connection.is_connected():
        print("Connected to MySQL database")
        
        # Create cursor object to execute SQL queries
        cursor = connection.cursor()
        
        # Drop existing tables if they exist
        cursor.execute("DROP TABLE IF EXISTS Employees")
        cursor.execute("DROP TABLE IF EXISTS Menu")
        cursor.execute("DROP TABLE IF EXISTS Orders")
        cursor.execute("DROP TABLE IF EXISTS Customers")
        
        # Create Menu table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Menu (
                menu_ID INT PRIMARY KEY AUTO_INCREMENT,
                item_Name VARCHAR(50),
                item_Description TEXT,
                item_Price DECIMAL(10,2),
                ordered INT DEFAULT 0
            )
        """)
     
        # Create Employees table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Employees (
                employees_id INT PRIMARY KEY AUTO_INCREMENT,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                phone_number VARCHAR(15),
                address VARCHAR(100),
                hire_date DATE
            )
        """)
        
        # Create Customers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Customers (
                customers_id INT PRIMARY KEY AUTO_INCREMENT,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                phone_number VARCHAR(15),
                address VARCHAR(100),
                Feedback TEXT,
                tot_ordered INT DEFAULT 0
            )
        """)
        
        # Create Orders table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Orders (
                orders_id INT PRIMARY KEY AUTO_INCREMENT,
                customer_id INT,
                staff_id INT,
                item_id INT,
                order_status BOOLEAN,
                order_date DATETIME default now(),
                FOREIGN KEY (customer_id) REFERENCES Customers(customers_id)
            )
        """)

        print("Tables created successfully")


        
###############################################################################
# Find Customer (serach by first and last name)
###############################################################################

    cursor.execute("""
                   DROP procedure IF EXISTS find_customers;""")
    cursor.execute("""create procedure find_customers(in f_name varchar(50), in l_name varchar(50))
                    begin
                   select * from Customers
                   where first_name = f_name and last_name = l_name;
                   end;
                   """)

    print("Data inserted successfully")




     
###########################################################3#
#               Triggers!
############################################################
   
    cursor.execute("""
    DROP TRIGGER IF EXISTS increase_ordered_column;
    """)
    cursor.execute("""
        CREATE TRIGGER increase_ordered_column
        AFTER INSERT ON Orders
        FOR EACH ROW
        BEGIN
            UPDATE Menu
            SET Menu.ordered = Menu.ordered + 1
            WHERE menu_ID = NEW.item_id;
        END;
    """)
    connection.commit()

    
    cursor.execute("""
    DROP TRIGGER IF EXISTS increase_tot_ordered_of_a_cus;
    """)
    cursor.execute("""
        CREATE TRIGGER increase_tot_ordered_of_a_cus
        AFTER INSERT ON Orders
        FOR EACH ROW
        BEGIN
            UPDATE Customers
            SET Customers.tot_ordered  = Customers.tot_ordered + 1
            WHERE Customers.customers_id = new.customer_id;
        END;
    """)
    connection.commit()
                   




        # Insert data into Menu table
    cursor.execute("""
        INSERT INTO Menu (item_Name, item_Description, item_Price)
        VALUES ('Burger', 'Delicious beef burger', 9.99 ),
                ('Pizza', 'Cheesy pizza with various toppings', 12.99 ),
                ('Salad', 'Fresh and healthy salad', 6.99 ),
                ('Pasta', 'Classic Italian pasta', 10.99 ),
                ('Steak', 'Juicy steak cooked to perfection', 15.99 ),
                ('Sushi', 'Traditional Japanese sushi rolls', 8.99 ),
                ('Chicken Wings', 'Spicy and crispy chicken wings', 7.99 ),
                ('Fish and Chips', 'British-style fish and chips', 11.99 ),
                ('Tacos', 'Authentic Mexican tacos', 9.99 ),
                ('Ice Cream', 'Creamy and delicious ice cream', 4.99 )
    """)
    connection.commit()

    # Insert data into Employees table
    cursor.execute("""
        INSERT INTO Employees (first_name, last_name, phone_number, address, hire_date)
        VALUES ('John', 'Doe', '1234567890', '123 Main St', '2022-01-01'),
            ('Jane', 'Smith', '9876543210', '456 Elm St', '2022-02-01'),
            ('Michael', 'Johnson', '5555555555', '789 Oak St', '2022-03-01'),
            ('Emily', 'Brown', '1111111111', '321 Pine St', '2022-04-01'),
            ('David', 'Taylor', '9999999999', '654 Maple St', '2022-05-01'),
            ('Sarah', 'Anderson', '8888888888', '987 Cedar St', '2022-06-01'),
            ('Daniel', 'Wilson', '7777777777', '654 Birch St', '2022-07-01'),
            ('Olivia', 'Miller', '2222222222', '321 Walnut St', '2022-08-01'),
            ('James', 'Davis', '3333333333', '789 Pine St', '2022-09-01'),
            ('Sophia', 'Martinez', '4444444444', '987 Oak St', '2022-10-01')
    """)
    
    connection.commit()

    # Insert data into Customers table
    cursor.execute("""
        INSERT INTO Customers (first_name, last_name, phone_number, address, Feedback)
        VALUES ('Emma', 'Johnson', '5555555555', '123 Main St', 'Great service!'),
            ('Liam', 'Smith', '9876543210', '456 Elm St', 'Delicious food!'),
            ('Ava', 'Brown', '1111111111', '789 Oak St', 'Friendly staff!'),
            ('Noah', 'Taylor', '9999999999', '321 Pine St', 'Amazing experience!'),
            ('Isabella', 'Anderson', '8888888888', '654 Maple St', 'Highly recommended!'),
            ('Mia', 'Wilson', '7777777777', '987 Cedar St', 'Excellent quality!'),
            ('Lucas', 'Miller', '2222222222', '654 Birch St', 'Fast delivery!'),
            ('Sophia', 'Davis', '3333333333', '321 Walnut St', 'Fresh ingredients!'),
            ('Jackson', 'Martinez', '4444444444', '789 Pine St', 'Good value for money!'),
            ('Aiden', 'Johnson', '5555555555', '987 Oak St', 'Satisfied customer!')
    """)
    connection.commit()

    # Insert data into Orders table
    cursor.execute("""
        INSERT INTO Orders (customer_id, staff_id, item_id, order_status)
        VALUES (1, 1, 1, True),
            (2, 2, 2, True),
            (2, 2, 2, True),
            (2, 2, 2, True),
            (3, 3, 3, True),
            (4, 4, 4, True),
            (5, 5, 5, True),
            (7, 7, 7, True),
            (6, 6, 6, True),
            (8, 8, 8, True),
            (9, 9, 9, True),
            (10, 10, 10, True),
            (10, 10, 11, True)
    """)
    connection.commit()
    cursor.execute("""
    DROP TRIGGER IF EXISTS increase_ordered_column;
    """)
    cursor.execute("""
        CREATE TRIGGER increase_ordered_column
        AFTER INSERT ON Orders
        FOR EACH ROW
        BEGIN
            UPDATE Menu
            SET Menu.ordered = Menu.ordered + 1
            WHERE menu_ID = NEW.item_id;
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



