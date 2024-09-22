from PySide6.QtWidgets import QDialog, QHeaderView, QAbstractItemView, QMessageBox
from PySide6.QtSql import QSqlTableModel, QSqlDatabase
from PySide6.QtCore import Qt, QItemSelection
from UI.employeesList.employeesListUI import Ui_Dialog
from database import DataBase
from sqlite3 import Error


class EmployeesList(QDialog):
    def __init__(self, id):
        super().__init__()

        self.employees_list_ui = Ui_Dialog()
        self.employees_list_ui.setupUi(self)

        self.employees_list_ui.ReturnButton.clicked.connect(
            self.on_return_button_clicked)

        self.employees_list_ui.SearchEmployeeInput.textChanged.connect(
            self.on_search_employee_input_change)

        self.db = DataBase()

        if not QSqlDatabase.contains('qt_sql_default_connection'):
            self.sql_db = QSqlDatabase.addDatabase('QSQLITE')
        else:
            self.sql_db = QSqlDatabase.database('qt_sql_default_connection')

        self.sql_db.setDatabaseName('expense_tracker.db')

        if not self.sql_db.open():
            print('Database connect failed.')
            return

        self.model = QSqlTableModel()
        self.model.setTable('Employees')
        self.model.select()

        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Имя")
        self.model.setHeaderData(2, Qt.Horizontal, "Фамилия")
        self.model.setHeaderData(3, Qt.Horizontal, "Отчество")
        self.model.setHeaderData(4, Qt.Horizontal, "Логин")
        self.model.setHeaderData(5, Qt.Horizontal, "Пароль")
        self.model.setHeaderData(6, Qt.Horizontal, "Телефон")
        self.model.setHeaderData(7, Qt.Horizontal, "Роль")
        self.model.setHeaderData(8, Qt.Horizontal, "ID отдела")

        # tableView - EmployeesTable

        self.employees_list_ui.tableView.setModel(self.model)

        self.employees_list_ui.tableView.hideColumn(4)
        self.employees_list_ui.tableView.hideColumn(5)

        self.employees_list_ui.tableView.horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)

        self.employees_list_ui.tableView.setEditTriggers(
            QAbstractItemView.NoEditTriggers)

    def on_return_button_clicked(self):
        self.close()

    def on_search_employee_input_change(self, text):
        self.model.setFilter(
            f"name LIKE '%{text}%' OR last_name LIKE '%{text}%' OR middle_name LIKE '%{text}%'")
        self.model.select()
