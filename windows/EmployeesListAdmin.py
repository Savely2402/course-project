from PySide6.QtWidgets import QDialog, QHeaderView, QAbstractItemView, QMessageBox
from PySide6.QtSql import QSqlTableModel, QSqlDatabase
from PySide6.QtCore import Qt, QItemSelection
from UI.employeesListAdmin.employeesListAdminUI import Ui_Dialog
from database import DataBase
from windows.AddEmployee import AddEmployee
from utils import show_error_message
from sqlite3 import Error


class EmployeesListAdmin(QDialog):
    def __init__(self, id):
        super().__init__()

        self.employees_list_admin_ui = Ui_Dialog()
        self.employees_list_admin_ui.setupUi(self)

        self.employees_list_admin_ui.AddEmployeeButton.clicked.connect(
            self.on_add_employee_button_clicked)
        self.employees_list_admin_ui.DeleteEmployeeButton.clicked.connect(
            self.on_delete_employee_button_clicked)
        self.employees_list_admin_ui.ReturnButton.clicked.connect(
            self.on_return_button_clicked)

        self.employees_list_admin_ui.DeleteEmployeeButton.setEnabled(False)

        self.employees_list_admin_ui.SearchEmployeeInput.textChanged.connect(
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

        self.employees_list_admin_ui.tableView.setModel(self.model)

        self.employees_list_admin_ui.tableView.hideColumn(4)
        self.employees_list_admin_ui.tableView.hideColumn(5)

        self.employees_list_admin_ui.tableView.horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)

        self.employees_list_admin_ui.tableView.setEditTriggers(
            QAbstractItemView.NoEditTriggers)

        self.employees_list_admin_ui.tableView.selectionModel(
        ).selectionChanged.connect(self.on_selection_changed)

    def on_add_employee_button_clicked(self):
        self.close()

        self.open_add_employee_window()

    def on_delete_employee_button_clicked(self):
        reply = QMessageBox.question(self,
                                     'Подтверждение удаления',
                                     'Вы уверены, что хотите удалить этого сотрудника?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:

            employee_id = self.get_selected_employee_id()
            if employee_id is not None:
                try:
                    self.db.db_delete_employee_by_id(id=employee_id)
                    self.update_table()
                    QMessageBox.information(
                        self, 'Успех', 'Сотрудник успешно удален!')
                except Error as e:
                    QMessageBox.critical(
                        self, 'Ошибка!', 'Ошибка при удалении!')

    def on_return_button_clicked(self):
        self.close()

    def on_selection_changed(self, selected: QItemSelection):
        selected_indexes = selected.indexes()
        column = selected_indexes[0].column()

        if column == 0:
            self.employees_list_admin_ui.DeleteEmployeeButton.setEnabled(
                True)
        else:
            self.employees_list_admin_ui.DeleteEmployeeButton.setEnabled(
                False)

    def get_selected_employee_id(self):
        selected_indexes = self.employees_list_admin_ui.tableView.selectedIndexes()
        if selected_indexes:
            return self.model.data(selected_indexes[0])
        return None

    def on_search_employee_input_change(self, text):
        self.model.setFilter(
            f"name LIKE '%{text}%' OR last_name LIKE '%{text}%' OR middle_name LIKE '%{text}%'")
        self.model.select()

    def open_add_employee_window(self):
        add_employee = AddEmployee(id=1)
        add_employee.exec()

    def update_table(self):
        self.model.select()
