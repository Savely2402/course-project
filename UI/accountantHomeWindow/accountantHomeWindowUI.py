# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accountantHomeWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
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
        Dialog.resize(591, 415)
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
        self.WindowTitle.setEnabled(True)
        self.WindowTitle.setStyleSheet(u"")
        self.WindowTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.WindowTitle)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PersonAccountButton = QPushButton(self.frame)
        self.PersonAccountButton.setObjectName(u"PersonAccountButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PersonAccountButton.sizePolicy().hasHeightForWidth())
        self.PersonAccountButton.setSizePolicy(sizePolicy)
        self.PersonAccountButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.verticalLayout.addWidget(self.PersonAccountButton)

        self.EmployeesListButton = QPushButton(self.frame)
        self.EmployeesListButton.setObjectName(u"EmployeesListButton")
        sizePolicy.setHeightForWidth(self.EmployeesListButton.sizePolicy().hasHeightForWidth())
        self.EmployeesListButton.setSizePolicy(sizePolicy)
        self.EmployeesListButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.verticalLayout.addWidget(self.EmployeesListButton)

        self.CompletedDocumentsButton = QPushButton(self.frame)
        self.CompletedDocumentsButton.setObjectName(u"CompletedDocumentsButton")
        sizePolicy.setHeightForWidth(self.CompletedDocumentsButton.sizePolicy().hasHeightForWidth())
        self.CompletedDocumentsButton.setSizePolicy(sizePolicy)
        self.CompletedDocumentsButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.verticalLayout.addWidget(self.CompletedDocumentsButton)

        self.DepartmentButton = QPushButton(self.frame)
        self.DepartmentButton.setObjectName(u"DepartmentButton")
        sizePolicy.setHeightForWidth(self.DepartmentButton.sizePolicy().hasHeightForWidth())
        self.DepartmentButton.setSizePolicy(sizePolicy)
        self.DepartmentButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.verticalLayout.addWidget(self.DepartmentButton)

        self.LogoutButton = QPushButton(self.frame)
        self.LogoutButton.setObjectName(u"LogoutButton")
        sizePolicy.setHeightForWidth(self.LogoutButton.sizePolicy().hasHeightForWidth())
        self.LogoutButton.setSizePolicy(sizePolicy)
        self.LogoutButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.verticalLayout.addWidget(self.LogoutButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.WindowTitle.setText(QCoreApplication.translate("Dialog", u"\u0411\u0443\u0445\u0433\u0430\u043b\u0442\u0435\u0440\u0438\u044f", None))
        self.PersonAccountButton.setText(QCoreApplication.translate("Dialog", u"\u041b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442", None))
        self.EmployeesListButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
        self.CompletedDocumentsButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u043d\u044b\u0445 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.DepartmentButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0434\u0435\u043b", None))
        self.LogoutButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

