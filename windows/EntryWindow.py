
from PySide6.QtWidgets import QMainWindow, QDialog
from UI.entryWindow.entryWindowUI import Ui_MainWindow
from UI.adminHomeWindow.adminHomeWindowUI import Ui_Dialog
from database import DataBase
from windows.HomeWindowAdministrator import HomeWindowAdministrator
from windows.HomeWindowAccountant import HomeWindowAccountant
from windows.HomeWindowEmployee import HomeWindowEmployee
from utils import show_warning_message


class EntryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.entry_window = Ui_MainWindow()
        self.entry_window.setupUi(self)
        self.db = DataBase()
        self.db.db_create_tables()

        self.entry_window.LoginButton.clicked.connect(
            self.on_enter_button_clicked)

    def on_enter_button_clicked(self):
        login = self.entry_window.LoginInput.text()
        password = self.entry_window.PasswordInput.text()

        if login == '' or password == '':
            warningMessage = 'Все поля должны быть заполнены!'
            show_warning_message(warningMessage)
        else:
            employee = self.db.db_check_login_and_password(
                login, password)
            if employee == None:
                warningMessage = 'Неверный логин или пароль'
                show_warning_message(warningMessage)
            else:
                id = employee[0]
                role = employee[7]

                if role == 'Сотрудник':
                    self.open_employee_home_window(id)
                elif role == 'Бухгалтер':
                    self.open_accountant_home_window(id)
                elif role == 'Администратор':
                    self.open_admin_home_window(id)

    def open_admin_home_window(self, id):
        homeWindowAdministrator = HomeWindowAdministrator(id)
        homeWindowAdministrator.exec()

    def open_employee_home_window(self, id):
        homeWindowAdministrator = HomeWindowEmployee(id)
        homeWindowAdministrator.exec()

    def open_accountant_home_window(self, id):
        homeWindowAdministrator = HomeWindowAccountant(id)
        homeWindowAdministrator.exec()
