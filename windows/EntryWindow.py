
from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox
# Импортируйте ваш сгенерированный файл
from UI.entryWindow.entryWindowUI import Ui_MainWindow
from UI.adminHomeWindow.adminHomeWindowUI import Ui_Dialog
from database import DataBase
from windows.HomeWindowAdministrator import HomeWindowAdministrator


class EntryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.entry_window = Ui_MainWindow()
        self.entry_window.setupUi(self)
        self.db = DataBase()
        self.db.create_table()

        self.entry_window.LoginButton.clicked.connect(
            self.on_enter_button_Clicked_clicked)

    def on_enter_button_Clicked_clicked(self):
        login = self.entry_window.LoginInput.text()
        password = self.entry_window.PasswordInput.text()

        if login == '1' and password == '1':
            self.openHomeWindowAdministrator()
        else:
            if login == '' or password == '':
                errorMessage = 'Все поля должны быть заполнены!'
            self.show_error_message(errorMessage)

    def show_error_message(self, message):
        error_msg_box = QMessageBox()
        error_msg_box.setIcon(QMessageBox.Icon.Warning)
        error_msg_box.setText("Ошибка")
        error_msg_box.setInformativeText(message)
        error_msg_box.setWindowTitle("Ошибка")
        error_msg_box.setStandardButtons(QMessageBox.Ok)
        error_msg_box.exec_()

    def openHomeWindowAdministrator(self):
        self.close()

        homeWindowAdministrator = HomeWindowAdministrator(id=1)
        homeWindowAdministrator.exec()
