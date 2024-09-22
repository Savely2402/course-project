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

    def db_create_tables(self):
        create_employees_table = """
                                CREATE TABLE IF NOT EXISTS Employees (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    last_name TEXT NOT NULL,
                                    middle_name TEXT,
                                    login TEXT UNIQUE NOT NULL,
                                    password TEXT NOT NULL,
                                    phone TEXT UNIQUE NOT NULL,
                                    role TEXT NOT NULL,
                                    department_ID INTEGER NOT NULL,
                                    FOREIGN KEY (department_ID) REFERENCES Department(id)

                                );
                                """

        create_department_table = """
                                CREATE TABLE IF NOT EXISTS Department (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,  
                                    department_name TEXT UNIQUE NOT NULL,         
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
            raise

    def db_check_login_and_password(self, login, password):
        select_employees_query = f"SELECT * FROM Employees WHERE login = ?"

        try:

            cursor = self.connection.cursor()
            cursor.execute(select_employees_query, (login, ))
            employee = cursor.fetchone()

            if employee and password == employee[5]:
                return employee
            else:
                return None
        except Error as e:
            print(f'Error while getting employee: {e}')
            raise

    def db_add_department(self, department_name):
        insert_department_query = """
                                INSERT INTO Department (department_name, total_budget, monthly_budget) 
                                VALUES (?, ?, ?)
                                """
        data = (department_name, 0, 0)

        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_department_query, data)
            self.connection.commit()
        except Error as e:
            print(f'Adding department failed with error: {e}')
            raise

    def db_delete_department_by_id(self, id):
        insert_query = """
                                DELETE FROM Department WHERE 
                                id = ?
                                """

        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query, (id, ))
            self.connection.commit()
        except Error as e:
            print(f'Deleting department failed with error: {e}')
            raise

    def db_find_department_by_id(self, id):
        select_query = """
                      SELECT * FROM Department WHERE id = ?
                        """
        data = (id, )
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query, data)
            department = cursor.fetchone()

            return department

        except Error as e:
            print(f'Selecting department by id failed with error: {e}')
            raise

    def db_select_all_departments(self):
        select_query = """
                      SELECT * FROM Department
                        """

        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query)
            departments = cursor.fetchall()

            return departments

        except Error as e:
            print(f'Selecting all departments failed with error: {e}')
            raise

    def db_add_employee(self, name, last_name, middle_name, phone, role, department_id, login, password):

        insert_department_query = """
                                INSERT INTO Employees (name, last_name, middle_name, phone, role, department_ID, login, password) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                                """
        data = (name, last_name, middle_name, phone,
                role, department_id, login, password)

        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_department_query, data)
            self.connection.commit()
        except Error as e:
            print(f'Adding employee failed with error: {e}')
            raise

    def db_delete_employee_by_id(self, id):
        insert_query = """
                                DELETE FROM Employees WHERE 
                                id = ?
                                """

        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query, (id, ))
            self.connection.commit()
        except Error as e:
            print(f'Deleting employee failed with error: {e}')
            raise

    def db_find_employee_by_id(self, id):
        select_query = """
                      SELECT * FROM Employees WHERE id = ?
                        """

        data = (id, )

        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query, data)
            employee = cursor.fetchone()

            return employee

        except Error as e:
            print(f'Selecting employee by id failed with error: {e}')
            raise

    def db_change_password(self, id, password):
        select_query = """
                      UPDATE Employees SET password = ? WHERE id = ?
                        """

        data = (password, id)

        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query, data)
            self.connection.commit()

        except Error as e:
            print(f'Changing password failed with error: {e}')
            raise

    def db_change_phone(self, id, phone):
        select_query = """
                      UPDATE Employees SET phone = ? WHERE id = ?
                        """

        data = (phone, id)

        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query, data)
            self.connection.commit()

        except Error as e:
            print(f'Changing phone failed with error: {e}')
            raise

    def db_increase_department_budget(self, id, increment):
        select_query = """
                      UPDATE Department SET monthly_budget = monthly_budget + ?, total_budget = total_budget + ? WHERE id = ?
                        """

        data = (increment, increment, id)

        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query, data)
            self.connection.commit()

        except Error as e:
            print(f'Changing department budget failed with error: {e}')
            raise

    def db_add_purchase(self, employee_id, name, desc, price, date, quantity, total_cost):

        insert_query = """
                                INSERT INTO Purchase (employee_ID, purchase_name, description, price, purchase_date, quantity, total_cost) 
                                VALUES (?, ?, ?, ?, ?, ?, ?)
                                """
        data = (employee_id, name, desc,  price,
                date, quantity, total_cost)

        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query, data)
            self.connection.commit()
        except Error as e:
            print(f'Adding purchase failed with error: {e}')
            raise
