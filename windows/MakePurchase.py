from sqlite3 import Error
from PySide6.QtWidgets import QDialog, QMessageBox
from UI.makePurchase.makePurchaseUI import Ui_Dialog
from database import DataBase
from datetime import datetime
from utils import show_error_message, show_info_message, show_warning_message


class MakePurchase(QDialog):
    def __init__(self, id):
        super().__init__()

        self.make_purchase_ui = Ui_Dialog()
        self.make_purchase_ui.setupUi(self)

        self.db = DataBase()

        self._employee = self.db.db_find_employee_by_id(id)
        department_id = self._employee[8]

        department = self.db.db_find_department_by_id(department_id)
        self._total_department_budget = department[2]

        self.make_purchase_ui.TotalDepartmentBudgetLabel.setText(
            str(self._total_department_budget))

        self.make_purchase_ui.CurrentPriceInput.textChanged.connect(
            self.on_price_input_changed)
        self.make_purchase_ui.QuantityInput.textChanged.connect(
            self.on_quantity_input_changed)

        self.make_purchase_ui.BuyButton.clicked.connect(
            self.on_buy_button_clicked)

        self.make_purchase_ui.ReturnButton.clicked.connect(
            self.on_logout_button_clicked)

    def on_quantity_input_changed(self, quantity):
        price = self.make_purchase_ui.CurrentPriceInput.text()
        total_price = '0' if quantity == '' or price == '' else int(
            price) * int(quantity)

        self.make_purchase_ui.TotalPriceLabel_2.setText(
            str(total_price))

    def on_price_input_changed(self, price):
        quantity = self.make_purchase_ui.QuantityInput.text()
        total_price = '0' if quantity == '' or price == '' else int(
            price) * int(quantity)

        self.make_purchase_ui.TotalPriceLabel_2.setText(
            str(total_price))

    def on_buy_button_clicked(self):
        desc_text = self.make_purchase_ui.DescriptionText.toPlainText()
        name_text = self.make_purchase_ui.PurchaseNameInput.text()
        quantity_text = self.make_purchase_ui.QuantityInput.text()
        price_text = self.make_purchase_ui.CurrentPriceInput.text()
        employee_id = self._employee[0]
        total_price = int(self.make_purchase_ui.TotalPriceLabel_2.text())
        current_date = datetime.now().strftime('%Y-%m-%d')

        if name_text != '' and quantity_text != '' and price_text != '' and total_price <= self._total_department_budget:
            try:
                self.db.db_add_purchase(employee_id, name_text, desc_text, int(
                    price_text), current_date, int(quantity_text), total_price)
                self.make_purchase_ui.TotalDepartmentBudgetLabel.setText(
                    str(self._total_department_budget - total_price))

                show_info_message('Покупка прошла успешно')
            except Error as e:
                show_error_message('Ошибка при покупке!')
                return
        elif total_price > self._total_department_budget:
            show_warning_message('Сумма товара превышает общий бюджет!')
            return
        else:
            show_warning_message(
                'Поля: Наименования, стоимость и количество должны быть заполнены!')
            return

    def on_logout_button_clicked(self):
        self.close()
