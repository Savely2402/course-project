from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QTimer
from UI.adminHomeWindow.adminHomeWindowUI import Ui_Dialog
from database import DataBase
from windows.EmployeesListAdmin import EmployeesListAdmin
from windows.DepartmentsListAdmin import DepartmentsListAdmin
from windows.PersonsAccount import PersonsAccount


class HomeWindowAdministrator(QDialog):
    def __init__(self, id):
        super().__init__()

        self.admin_home_ui = Ui_Dialog()
        self.admin_home_ui.setupUi(self)

        self.id = id

        self.admin_home_ui.PersonAccountButton.clicked.connect(
            self.on_person_account_button_clicked)
        self.admin_home_ui.DepartmentButton.clicked.connect(
            self.on_departments_list_button_clicked)
        self.admin_home_ui.EmployeesListButton.clicked.connect(
            self.on_employees_list_button_clicked)
        self.admin_home_ui.LogoutButton.clicked.connect(
            self.on_logout_button_clicked)

    def on_person_account_button_clicked(self):
        self.open_person_account_window()

    def on_departments_list_button_clicked(self):
        self.open_departments_list_window()

    def on_employees_list_button_clicked(self):
        self.open_employees_list_window()

    def on_logout_button_clicked(self):
        self.close()

    def open_person_account_window(self):
        persons_account = PersonsAccount(id=self.id)
        persons_account.exec()

    def open_departments_list_window(self):
        departments_list_admin = DepartmentsListAdmin(id=1)
        departments_list_admin.exec()

    def open_employees_list_window(self):
        employees_list_admin = EmployeesListAdmin(id=1)
        employees_list_admin.exec()
