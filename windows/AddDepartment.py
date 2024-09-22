
from sqlite3 import Error
from PySide6.QtWidgets import QDialog
from UI.addDepartment.addDepartmentUI import Ui_Dialog
from database import DataBase
from utils import show_warning_message, show_info_message, show_error_message


class AddDepartment(QDialog):
    def __init__(self, id):
        super().__init__()

        self.db = DataBase()

        self.add_department_ui = Ui_Dialog()
        self.add_department_ui.setupUi(self)

        self.add_department_ui.AddDepartmentButton.clicked.connect(
            self.on_add_department_button_clicked)
        self.add_department_ui.ReturnButton.clicked.connect(
            self.on_return_button_clicked)

    def on_add_department_button_clicked(self):
        department_name_text = self.add_department_ui.DepartmentNameInput.text()

        if not department_name_text:
            warning_message = 'Введите название отдела!'
            show_warning_message(warning_message)
            return

        try:
            self.db.db_add_department(department_name_text)
            info_message = 'Отдел успешно добавлен'
            show_info_message(info_message)
        except Error as e:
            error_message = 'Ошибка при добавлении отдела!'
            show_error_message(error_message)

    def on_return_button_clicked(self):
        self.close()
