
from sqlite3 import Error
from PySide6.QtWidgets import QDialog
from UI.addEmployee.addEmployeeUI import Ui_Dialog
from database import DataBase
from utils import show_warning_message, show_info_message, show_error_message


class AddEmployee(QDialog):
    def __init__(self, id):
        super().__init__()

        self.db = DataBase()

        self.add_employee_ui = Ui_Dialog()
        self.add_employee_ui.setupUi(self)

        self.add_employee_ui.AddEmployeeButton.clicked.connect(
            self.on_add_employee_button_clicked)
        self.add_employee_ui.ReturnButton.clicked.connect(
            self.on_return_button_clicked)

        self.add_employee_ui.RolesBox.addItems(
            ['Сотрудник', 'Бухгалтер', 'Администратор'])

        departments = self.db.db_select_all_departments()

        for department in departments:
            department_name = department[1]
            department_id = department[0]
            self.add_employee_ui.DepartmentsBox.addItem(
                department_name, department_id)

    def on_add_employee_button_clicked(self):
        employee_name_text = self.add_employee_ui.NameInput.text()
        employee_surname_text = self.add_employee_ui.SurnameInput.text()
        employee_middle_name_text = self.add_employee_ui.MiddleNameInput.text()
        employee_phone_text = self.add_employee_ui.PhoneInput.text()
        employee_role_text = self.add_employee_ui.RolesBox.currentText()
        employee_department_id = self.add_employee_ui.DepartmentsBox.currentData()
        employee_login_text = self.add_employee_ui.LoginInput.text()
        employee_password_text = self.add_employee_ui.PasswordInput.text()

        if not employee_name_text:
            warning_message = 'Введите имя сотрудника!'
            show_warning_message(warning_message)
            return
        if not employee_surname_text:
            warning_message = 'Введите фамилию сотрудника!'
            show_warning_message(warning_message)
            return
        if not employee_phone_text:
            warning_message = 'Введите телефон сотрудника!'
            show_warning_message(warning_message)
            return
        if not employee_login_text:
            warning_message = 'Введите логин сотрудника!'
            show_warning_message(warning_message)
            return
        if not employee_password_text:
            warning_message = 'Введите пароль сотрудника!'
            show_warning_message(warning_message)
            return

        try:
            self.db.db_add_employee(employee_name_text, employee_surname_text, employee_middle_name_text, employee_phone_text,
                                    employee_role_text, employee_department_id, employee_login_text, employee_password_text)
            info_message = 'Сотрудник успешно добавлен'
            show_info_message(info_message)
        except Error as e:
            error_message = 'Ошибка при добавлении сотрудника!'
            show_error_message(error_message)

    def on_return_button_clicked(self):
        self.close()
