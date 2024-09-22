
from sqlite3 import Error
from PySide6.QtWidgets import QDialog, QMessageBox
from UI.personsAccount.personsAccountUI import Ui_Dialog
from database import DataBase
from utils import show_error_message, show_info_message, show_warning_message


class PersonsAccount(QDialog):
    def __init__(self, id):
        super().__init__()

        self.persons_account_ui = Ui_Dialog()
        self.persons_account_ui.setupUi(self)

        self.persons_account_ui.ChangePasswordButton.clicked.connect(
            self.on_change_password_button_clicked)
        self.persons_account_ui.ReturnButton.clicked.connect(
            self.on_return_button_clicked)
        self.persons_account_ui.ChangePhoneButton.clicked.connect(
            self.on_change_phone_button_clicked)

        self.db = DataBase()
        self.id = id
        employee = self.db.db_find_employee_by_id(id)

        if employee:
            name = employee[1]
            last_name = employee[2]
            middle_name = employee[3] if employee[3] else ''
            login = employee[4]
            phone = employee[6]
            role = employee[7]
            department_id = employee[8]
            department = self.db.db_find_department_by_id(department_id)

            self.persons_account_ui.NameValue.setText(
                f"{last_name} {name} {middle_name}")
            self.persons_account_ui.LoginValue.setText(login)
            self.persons_account_ui.PhoneValue.setText(phone)
            self.persons_account_ui.RoleValue.setText(role)
            self.persons_account_ui.DepartmenValue.setText(department[1])

    def on_change_password_button_clicked(self):
        employee = self.db.db_find_employee_by_id(self.id)
        current_password = employee[5]
        old_password_input = self.persons_account_ui.OldPasswordInput.text()
        new_password_input = self.persons_account_ui.NewPasswordInput.text()
        new_confirmed_password_input = self.persons_account_ui.ConfirmNewPasswordInput.text()

        if old_password_input == current_password and new_confirmed_password_input == new_password_input and current_password != new_password_input:
            reply = QMessageBox.question(self,
                                         'Подтверждение смены пароля',
                                         'Вы уверены, что хотите сменить пароль?',
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)

            if reply == QMessageBox.Yes:
                try:
                    self.db.db_change_password(self.id, new_password_input)
                    show_info_message('Пароль успешно изменен')
                except Error as e:
                    show_error_message('Не удалось изменить пароль!')
                    return

        elif old_password_input != current_password:
            show_warning_message('Старый пароль не совпадает с текущим!')
            return
        elif new_confirmed_password_input != new_password_input:
            show_warning_message('Новые пароли не совпадают!')
            return
        elif current_password == new_password_input:
            show_warning_message('Новый пароль совпадает со старым!')
            return

    def on_change_phone_button_clicked(self):
        employee = self.db.db_find_employee_by_id(self.id)
        current_phone = employee[6]
        phone_input = self.persons_account_ui.ChangePhoneInput.text()

        if current_phone == phone_input:
            show_warning_message('Новый телефон не должен совпадать с текущим')
            return

        reply = QMessageBox.question(self,
                                     'Подтверждение смены пароля',
                                     'Вы уверены, что хотите сменить номер телефона?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                self.db.db_change_phone(self.id, phone_input)
                self.persons_account_ui.PhoneValue.setText(phone_input)
                show_info_message('Телефон успешно изменен')
            except Error as e:
                show_error_message('Не удалось изменить телефон!')
                return

    def on_return_button_clicked(self):
        self.close()
