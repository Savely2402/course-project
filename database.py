import sqlite3
from sqlite3 import Error


class DataBase:
    def __init__(self) -> None:
        self.connection = None

        try:
            self.connection = sqlite3.connect('expense_tracker.db')
            print('Database connection success!')
        except Error as e:
            print(f'Database connection failed with error: {e}')

    def create_table(self):
        create_employees_table = """
                                CREATE TABLE IF NOT EXISTS Employees (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    last_name TEXT NOT NULL,
                                    middle_name TEXT,
                                    login TEXT UNIQUE NOT NULL,
                                    password TEXT NOT NULL,
                                    phone TEXT NOT NULL,
                                    role TEXT NOT NULL,
                                    department_ID INTEGER NOT NULL,
                                    FOREIGN KEY (department_ID) REFERENCES Department(id)

                                );
                                """

        create_department_table = """
                                CREATE TABLE IF NOT EXISTS Department (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,  
                                    department_name TEXT NOT NULL,         
                                    total_budget REAL,                      
                                    monthly_budget REAL
                                );
                                """

        create_purchase_table = """
                                CREATE TABLE IF NOT EXISTS Purchase (
                                    purchase_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    employee_ID INTEGER,                        
                                    purchase_name TEXT NOT NULL,                  
                                    description TEXT,                             
                                    price REAL NOT NULL,                          
                                    purchase_date DATE,                           
                                    quantity INTEGER,                             
                                    total_cost REAL,                              
                                    FOREIGN KEY (employee_ID) REFERENCES Employee(id)
                                );
                                """

        try:
            cursor = self.connection.cursor()
            cursor.execute(create_employees_table)
            cursor.execute(create_department_table)
            cursor.execute(create_purchase_table)
            self.connection.commit()
            print(
                "Tables employees, departments and purchases were created successfully.")
        except Error as e:
            print(f"Error while creating tables: {e}")

    def checkLoginAndPassword(self, login, password):
        select_query = f"SELECT * FROM employees WHERE login = ?"

        try:

            cursor = self.connection.cursor()
            cursor.execute(select_query, (login, ))
            employee = cursor.fetchone()

            return employee
        except Error as e:
            print(f'Error while getting employee: {e}')
