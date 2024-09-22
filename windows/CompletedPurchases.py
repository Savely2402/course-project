from PySide6.QtWidgets import QDialog, QHeaderView, QAbstractItemView, QMessageBox
from PySide6.QtSql import QSqlTableModel, QSqlDatabase
from PySide6.QtCore import Qt, QItemSelection
from UI.completedPurchasesList.completedPurchasesListUI import Ui_Dialog
from database import DataBase
from sqlite3 import Error


class CompletedPurchases(QDialog):
    def __init__(self, id):
        super().__init__()

        self.completed_purchases_ui = Ui_Dialog()
        self.completed_purchases_ui.setupUi(self)

        self.completed_purchases_ui.ReturnButton.clicked.connect(
            self.on_return_button_clicked)

        self.completed_purchases_ui.SearchPurchasesInput.textChanged.connect(
            self.on_search_completed_purchases_input_change)

        self.db = DataBase()

        if not QSqlDatabase.contains('qt_sql_default_connection'):
            self.sql_db = QSqlDatabase.addDatabase('QSQLITE')
        else:
            self.sql_db = QSqlDatabase.database('qt_sql_default_connection')

        self.sql_db.setDatabaseName('expense_tracker.db')

        if not self.sql_db.open():
            print('Database connect failed.')
            return

        self.model = QSqlTableModel()
        self.model.setTable('Purchase')
        self.model.select()

        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Employee_Id")
        self.model.setHeaderData(2, Qt.Horizontal, "Название")
        self.model.setHeaderData(3, Qt.Horizontal, "Описание")
        self.model.setHeaderData(4, Qt.Horizontal, "Цена")
        self.model.setHeaderData(5, Qt.Horizontal, "Дата")
        self.model.setHeaderData(6, Qt.Horizontal, "Количество")
        self.model.setHeaderData(7, Qt.Horizontal, "Общая стоимость")

        self.completed_purchases_ui.PurchasesTable.setModel(self.model)

        self.completed_purchases_ui.PurchasesTable.hideColumn(1)

        self.completed_purchases_ui.PurchasesTable.horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)

        self.completed_purchases_ui.PurchasesTable.setEditTriggers(
            QAbstractItemView.NoEditTriggers)

    def on_return_button_clicked(self):
        self.close()

    def on_search_completed_purchases_input_change(self, text):
        self.model.setFilter(
            f"purchase_name LIKE '%{text}%' OR description LIKE '%{text}%'")
        self.model.select()
