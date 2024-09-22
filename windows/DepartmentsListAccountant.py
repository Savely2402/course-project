from PySide6.QtWidgets import QDialog, QHeaderView, QAbstractItemView, QMessageBox
from PySide6.QtSql import QSqlTableModel, QSqlDatabase
from PySide6.QtCore import Qt, QItemSelection
from UI.departmentsListAccountant.departmentsListAccountantUI import Ui_Dialog
from database import DataBase
from windows.ChangeDepartmentBudget import ChangeDepartmentBudget
from utils import show_error_message
from sqlite3 import Error


class DepartmentsListAccountant(QDialog):

    def __init__(self, id):
        super().__init__()

        self.departments_list_accountant_ui = Ui_Dialog()
        self.departments_list_accountant_ui.setupUi(self)

        self.departments_list_accountant_ui.ChangeDepartmentBudgetButton.clicked.connect(
            self.on_change_department_budget_button_clicked)

        self.departments_list_accountant_ui.ReturnButton.clicked.connect(
            self.on_return_button_clicked)

        self.departments_list_accountant_ui.SearchDepartmentInput.textChanged.connect(
            self.on_search_department_input_change)

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
        self.model.setTable('Department')
        self.model.select()

        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Название отдела")
        self.model.setHeaderData(2, Qt.Horizontal, "Общий бюджет")
        self.model.setHeaderData(3, Qt.Horizontal, "Бюджет на месяц")

        self.departments_list_accountant_ui.DepartmentsTable.setModel(
            self.model)

        self.departments_list_accountant_ui.DepartmentsTable.horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)

        self.departments_list_accountant_ui.DepartmentsTable.setEditTriggers(
            QAbstractItemView.NoEditTriggers)

        self.departments_list_accountant_ui.ChangeDepartmentBudgetButton.setEnabled(
            False)

        self.departments_list_accountant_ui.DepartmentsTable.selectionModel(
        ).selectionChanged.connect(self.on_selection_changed)

    def on_change_department_budget_button_clicked(self):
        department_id = self.get_selected_department_id()
        self.open_change_department_budget_window(id=department_id)

    def on_return_button_clicked(self):
        self.close()

    def on_selection_changed(self, selected: QItemSelection):
        selected_indexes = selected.indexes()
        column = selected_indexes[0].column()

        if column == 0:
            self.departments_list_accountant_ui.ChangeDepartmentBudgetButton.setEnabled(
                True)
        else:
            self.departments_list_accountant_ui.ChangeDepartmentBudgetButton.setEnabled(
                False)

    def get_selected_department_id(self):
        selected_indexes = self.departments_list_accountant_ui.DepartmentsTable.selectedIndexes()
        if selected_indexes:
            return self.model.data(selected_indexes[0])
        return None

    def on_search_department_input_change(self, text):
        self.model.setFilter(f"department_name LIKE '%{text}%'")
        self.model.select()

    def open_change_department_budget_window(self, id):
        add_department = ChangeDepartmentBudget(id)
        add_department.exec()

    def update_table(self):
        self.model.select()
