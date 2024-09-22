import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
# Импортируйте ваш сгенерированный файл
from UI.entryWindow.entryWindowUI import Ui_MainWindow
from UI.adminHomeWindow.adminHomeWindowUI import Ui_Dialog
from database import DataBase
from windows.EntryWindow import EntryWindow


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = EntryWindow()
    window.show()

    sys.exit(app.exec())
