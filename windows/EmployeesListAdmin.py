from PySide6.QtWidgets import QDialog
from UI.employeesListAdmin.employeesListAdminUI import Ui_Dialog
from database import DataBase


class EmployeesListAdmin(QDialog):
    def __init__(self, id):
        super().__init__()

        self.employees_list_admin_ui = Ui_Dialog()
        self.employees_list_admin_ui.setupUi(self)

        self.employees_list_admin_ui.AddEmployeeButton.clicked.connect(
            self.on_person_account_button_clicked)
        self.employees_list_admin_ui.DeleteEmployeeButton.clicked.connect(
            self.on_departments_button_clicked)

    def on_person_account_button_clicked(self):
        pass

    def on_departments_button_clicked(self):
        pass

    def on_employees_list_button_clicked(self):
        pass

    def on_logout_button_clicked(self):
        pass

    def open_person_account_window(self):
        pass

    def open_departments_window(self):
        pass

    def open_employees_list_window(self):
        pass

    def open_entry_window(self):
        pass
