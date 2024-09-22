from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIntValidator
from UI.changeDepartmentBudget.changeDepartmentBudgetUI import Ui_Dialog
from database import DataBase
from sqlite3 import Error
from utils import show_warning_message, show_error_message, show_info_message


class ChangeDepartmentBudget(QDialog):
    def __init__(self, department_id):
        super().__init__()

        self.change_department_budget_ui = Ui_Dialog()
        self.change_department_budget_ui.setupUi(self)

        self.db = DataBase()
        self.department_id = department_id

        department = self.db.db_find_department_by_id(department_id)

        department_name = department[1] if department else None
        self.change_department_budget_ui.DepartmentValue.setText(
            department_name)

        self.change_department_budget_ui.SumInput.setValidator(QIntValidator())

        self.change_department_budget_ui.GiveAwayButton.clicked.connect(
            self.on_give_away_button_clicked)
        self.change_department_budget_ui.ReturnButton.clicked.connect(
            self.on_logout_button_clicked)

    def on_give_away_button_clicked(self):
        sum_input = self.change_department_budget_ui.SumInput.text()
        current_budget = self.change_department_budget_ui.TotalDepartmentBudgetValue.text()

        if not sum_input:
            show_warning_message('Введите сумму!')
            return
        else:
            try:
                self.db.db_increase_department_budget(
                    self.department_id, int(sum_input))
                self.change_department_budget_ui.TotalDepartmentBudgetValue.setText(
                    str(int(current_budget) + int(sum_input)))
                show_info_message('Деньги выделены!')

            except Error as e:
                show_error_message('Не удалось выделть деньги!')
                return

    def on_logout_button_clicked(self):
        self.close()
