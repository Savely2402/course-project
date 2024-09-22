from PySide6.QtWidgets import QDialog
from UI.adminHomeWindow.adminHomeWindowUI import Ui_Dialog
from database import DataBase
from windows.EmployeesListAdmin import EmployeesListAdmin


class HomeWindowAdministrator(QDialog):
    def __init__(self, id):
        super().__init__()

        self.admin_home_ui = Ui_Dialog()
        self.admin_home_ui.setupUi(self)

        self.admin_home_ui.PersonAccountButton.clicked.connect(
            self.on_person_account_button_clicked)
        self.admin_home_ui.DepartmentButton.clicked.connect(
            self.on_departments_button_clicked)
        self.admin_home_ui.EmployeesListButton.clicked.connect(
            self.on_employees_list_button_clicked)
        self.admin_home_ui.LogoutButton.clicked.connect(
            self.on_logout_button_clicked)

    def on_person_account_button_clicked(self):
        pass

    def on_departments_button_clicked(self):
        pass

    def on_employees_list_button_clicked(self):
        self.open_employees_list_window()

    def on_logout_button_clicked(self):
        pass

    def open_person_account_window(self):
        pass

    def open_departments_window(self):
        pass

    def open_employees_list_window(self):
        self.close()

        employeesListAdmin = EmployeesListAdmin(id=1)
        employeesListAdmin.exec()

    def open_entry_window(self):
        pass
