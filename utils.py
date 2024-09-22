from PySide6.QtWidgets import QMessageBox


def show_warning_message(message):
    error_msg_box = QMessageBox()
    error_msg_box.setIcon(QMessageBox.Icon.Warning)
    error_msg_box.setText("Ошибка")
    error_msg_box.setInformativeText(message)
    error_msg_box.setWindowTitle("Ошибка")
    error_msg_box.setStandardButtons(QMessageBox.Ok)
    error_msg_box.exec_()


def show_info_message(message):
    error_msg_box = QMessageBox()
    error_msg_box.setIcon(QMessageBox.Icon.Information)
    error_msg_box.setText("Info")
    error_msg_box.setInformativeText(message)
    error_msg_box.setWindowTitle("Info")
    error_msg_box.setStandardButtons(QMessageBox.Ok)
    error_msg_box.exec_()


def show_error_message(message):
    error_msg_box = QMessageBox()
    error_msg_box.setIcon(QMessageBox.Icon.Critical)
    error_msg_box.setText("Ошибка")
    error_msg_box.setInformativeText(message)
    error_msg_box.setWindowTitle("Ошибка")
    error_msg_box.setStandardButtons(QMessageBox.Ok)
    error_msg_box.exec_()
