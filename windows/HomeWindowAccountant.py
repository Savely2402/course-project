from PySide6.QtWidgets import QDialog
from UI.accountantHomeWindow.accountantHomeWindowUI import Ui_Dialog
from database import DataBase
from windows.PersonsAccount import PersonsAccount
from windows.EmployeesList import EmployeesList
from windows.CompletedPurchases import CompletedPurchases
from windows.DepartmentsListAccountant import DepartmentsListAccountant


class HomeWindowAccountant(QDialog):
    def __init__(self, id):
        super().__init__()

        self.accountant_home_ui = Ui_Dialog()
        self.accountant_home_ui.setupUi(self)

        self.id = id

        self.accountant_home_ui.PersonAccountButton.clicked.connect(
            self.on_person_account_button_clicked)
        self.accountant_home_ui.DepartmentButton.clicked.connect(
            self.on_departments_list_button_clicked)
        self.accountant_home_ui.EmployeesListButton.clicked.connect(
            self.on_employees_list_button_clicked)
        self.accountant_home_ui.LogoutButton.clicked.connect(
            self.on_logout_button_clicked)
        self.accountant_home_ui.CompletedDocumentsButton.clicked.connect(
            self.on_completed_documents_button_clicked)

    def on_person_account_button_clicked(self):
        self.open_person_account_window()

    def on_departments_list_button_clicked(self):
        self.open_departments_list_window()

    def on_employees_list_button_clicked(self):
        self.open_employees_list_window()

    def on_completed_documents_button_clicked(self):
        self.open_completed_documents_window()

    def on_logout_button_clicked(self):
        self.close()

    def open_person_account_window(self):
        persons_account = PersonsAccount(id=self.id)
        persons_account.exec()

    def open_departments_list_window(self):
        departments_list = DepartmentsListAccountant(id=self.id)
        departments_list.exec()

    def open_employees_list_window(self):
        employees_list = EmployeesList(self.id)
        employees_list.exec()

    def open_completed_documents_window(self):
        completed_documents = CompletedPurchases(id=self.id)
        completed_documents.exec()
