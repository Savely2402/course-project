# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'adminHomeWindow.ui'
##
# Created by: Qt User Interface Compiler version 6.7.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(593, 422)
        Dialog.setStyleSheet(u"background-color: 	rgb(191, 233, 123);\n"
                             "font-family: Myanmar Text;")
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: white;\n"
                                 "border-radius: 20px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.WindowTitle = QLabel(self.frame)
        self.WindowTitle.setObjectName(u"WindowTitle")
        self.WindowTitle.setStyleSheet(u"")
        self.WindowTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.WindowTitle)

        self.AdminButtonsBlock = QVBoxLayout()
        self.AdminButtonsBlock.setObjectName(u"AdminButtonsBlock")
        self.PersonAccountButton = QPushButton(self.frame)
        self.PersonAccountButton.setObjectName(u"PersonAccountButton")
        self.PersonAccountButton.setStyleSheet(u"QPushButton {\n"
                                               "border-radius: 10;\n"
                                               "background-color: '#bfe97b';\n"
                                               "padding: 10px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "background-color: #a7ca6b;\n"
                                               "}")

        self.AdminButtonsBlock.addWidget(self.PersonAccountButton)

        self.EmployeesListButton = QPushButton(self.frame)
        self.EmployeesListButton.setObjectName(u"EmployeesListButton")
        self.EmployeesListButton.setStyleSheet(u"QPushButton {\n"
                                               "border-radius: 10;\n"
                                               "background-color: '#bfe97b';\n"
                                               "padding: 10px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "background-color: #a7ca6b;\n"
                                               "}")

        self.AdminButtonsBlock.addWidget(self.EmployeesListButton)

        self.DepartmentButton = QPushButton(self.frame)
        self.DepartmentButton.setObjectName(u"DepartmentButton")
        self.DepartmentButton.setStyleSheet(u"QPushButton {\n"
                                            "border-radius: 10;\n"
                                            "background-color: '#bfe97b';\n"
                                            "padding: 10px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "background-color: #a7ca6b;\n"
                                            "}\n"
                                            "")

        self.AdminButtonsBlock.addWidget(self.DepartmentButton)

        self.LogoutButton = QPushButton(self.frame)
        self.LogoutButton.setObjectName(u"LogoutButton")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.LogoutButton.sizePolicy().hasHeightForWidth())
        self.LogoutButton.setSizePolicy(sizePolicy)
        self.LogoutButton.setStyleSheet(u"QPushButton {\n"
                                        "border-radius: 10;\n"
                                        "background-color: '#bfe97b';\n"
                                        "padding: 10px 50px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: #a7ca6b;\n"
                                        "}\n"
                                        "")

        self.AdminButtonsBlock.addWidget(
            self.LogoutButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2.addLayout(self.AdminButtonsBlock)

        self.verticalLayout_3.addWidget(self.frame)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.WindowTitle.setText(QCoreApplication.translate(
            "Dialog", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.PersonAccountButton.setText(QCoreApplication.translate(
            "Dialog", u"\u041b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442", None))
        self.EmployeesListButton.setText(QCoreApplication.translate(
            "Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
        self.DepartmentButton.setText(QCoreApplication.translate(
            "Dialog", u"\u041e\u0442\u0434\u0435\u043b", None))
        self.LogoutButton.setText(QCoreApplication.translate(
            "Dialog", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi
