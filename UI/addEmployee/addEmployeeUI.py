# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addEmployee.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(563, 526)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1111111, 1111111))
        MainWindow.setStyleSheet(u"background-color: 	rgb(191, 233, 123);\n"
"font-family: Myanmar Text;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: white;\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.WindowTitle = QLabel(self.frame)
        self.WindowTitle.setObjectName(u"WindowTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WindowTitle.sizePolicy().hasHeightForWidth())
        self.WindowTitle.setSizePolicy(sizePolicy)
        self.WindowTitle.setStyleSheet(u"")
        self.WindowTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.WindowTitle, 0, Qt.AlignmentFlag.AlignHCenter)

        self.AddEmployeeForm = QGridLayout()
        self.AddEmployeeForm.setObjectName(u"AddEmployeeForm")
        self.AddEmployeeForm.setVerticalSpacing(20)
        self.NameLabel = QLabel(self.frame)
        self.NameLabel.setObjectName(u"NameLabel")

        self.AddEmployeeForm.addWidget(self.NameLabel, 0, 0, 1, 1)

        self.NameInput = QLineEdit(self.frame)
        self.NameInput.setObjectName(u"NameInput")
        self.NameInput.setStyleSheet(u"\n"
"border-bottom: 1px solid rgb(191, 233, 123);")

        self.AddEmployeeForm.addWidget(self.NameInput, 0, 1, 1, 2)

        self.SurnameLabel = QLabel(self.frame)
        self.SurnameLabel.setObjectName(u"SurnameLabel")

        self.AddEmployeeForm.addWidget(self.SurnameLabel, 1, 0, 1, 2)

        self.SurnameInput = QLineEdit(self.frame)
        self.SurnameInput.setObjectName(u"SurnameInput")
        self.SurnameInput.setStyleSheet(u"\n"
"border-bottom: 1px solid rgb(191, 233, 123);")

        self.AddEmployeeForm.addWidget(self.SurnameInput, 1, 2, 1, 1)

        self.PatronLabel = QLabel(self.frame)
        self.PatronLabel.setObjectName(u"PatronLabel")

        self.AddEmployeeForm.addWidget(self.PatronLabel, 2, 0, 1, 1)

        self.PatronInput = QLineEdit(self.frame)
        self.PatronInput.setObjectName(u"PatronInput")
        self.PatronInput.setStyleSheet(u"\n"
"border-bottom: 1px solid rgb(191, 233, 123);")

        self.AddEmployeeForm.addWidget(self.PatronInput, 2, 2, 1, 1)

        self.PhoneLabel = QLabel(self.frame)
        self.PhoneLabel.setObjectName(u"PhoneLabel")

        self.AddEmployeeForm.addWidget(self.PhoneLabel, 3, 0, 1, 2)

        self.PhoneInput = QLineEdit(self.frame)
        self.PhoneInput.setObjectName(u"PhoneInput")
        self.PhoneInput.setStyleSheet(u"\n"
"border-bottom: 1px solid rgb(191, 233, 123);")

        self.AddEmployeeForm.addWidget(self.PhoneInput, 3, 2, 1, 1)

        self.RoleLabel = QLabel(self.frame)
        self.RoleLabel.setObjectName(u"RoleLabel")

        self.AddEmployeeForm.addWidget(self.RoleLabel, 4, 0, 1, 2)

        self.RolesBox = QComboBox(self.frame)
        self.RolesBox.addItem("")
        self.RolesBox.addItem("")
        self.RolesBox.setObjectName(u"RolesBox")
        self.RolesBox.setStyleSheet(u"\n"
"border-bottom: 1px solid rgb(191, 233, 123);")
        self.RolesBox.setFrame(False)

        self.AddEmployeeForm.addWidget(self.RolesBox, 4, 2, 1, 1)

        self.DepartmentLabel = QLabel(self.frame)
        self.DepartmentLabel.setObjectName(u"DepartmentLabel")

        self.AddEmployeeForm.addWidget(self.DepartmentLabel, 5, 0, 1, 2)

        self.DepartmentsBox = QComboBox(self.frame)
        self.DepartmentsBox.addItem("")
        self.DepartmentsBox.addItem("")
        self.DepartmentsBox.addItem("")
        self.DepartmentsBox.setObjectName(u"DepartmentsBox")
        self.DepartmentsBox.setStyleSheet(u"\n"
"border-bottom: 1px solid rgb(191, 233, 123);")
        self.DepartmentsBox.setFrame(False)

        self.AddEmployeeForm.addWidget(self.DepartmentsBox, 5, 2, 1, 1)

        self.LoginLabel = QLabel(self.frame)
        self.LoginLabel.setObjectName(u"LoginLabel")

        self.AddEmployeeForm.addWidget(self.LoginLabel, 6, 0, 1, 2)

        self.LoginInput = QLineEdit(self.frame)
        self.LoginInput.setObjectName(u"LoginInput")
        self.LoginInput.setStyleSheet(u"\n"
"border-bottom: 1px solid rgb(191, 233, 123);")

        self.AddEmployeeForm.addWidget(self.LoginInput, 6, 2, 1, 1)

        self.PasswordLabel = QLabel(self.frame)
        self.PasswordLabel.setObjectName(u"PasswordLabel")

        self.AddEmployeeForm.addWidget(self.PasswordLabel, 7, 0, 1, 2)

        self.PasswordInput = QLineEdit(self.frame)
        self.PasswordInput.setObjectName(u"PasswordInput")
        self.PasswordInput.setStyleSheet(u"\n"
"border-bottom: 1px solid rgb(191, 233, 123);")

        self.AddEmployeeForm.addWidget(self.PasswordInput, 7, 2, 1, 1)


        self.verticalLayout.addLayout(self.AddEmployeeForm)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton)

        self.ReturnButton = QPushButton(self.frame)
        self.ReturnButton.setObjectName(u"ReturnButton")
        sizePolicy.setHeightForWidth(self.ReturnButton.sizePolicy().hasHeightForWidth())
        self.ReturnButton.setSizePolicy(sizePolicy)
        self.ReturnButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px  50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")
        self.ReturnButton.setAutoDefault(True)
        self.ReturnButton.setFlat(False)

        self.verticalLayout.addWidget(self.ReturnButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.ReturnButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expense tracker", None))
        self.WindowTitle.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.NameLabel.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.SurnameLabel.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.PatronLabel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.PhoneLabel.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440:", None))
        self.RoleLabel.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u043b\u044c:", None))
        self.RolesBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a", None))
        self.RolesBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0445\u0433\u0430\u043b\u0442\u0435\u0440", None))

        self.DepartmentLabel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b:", None))
        self.DepartmentsBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u043a\u0435\u0442\u0438\u043d\u0433", None))
        self.DepartmentsBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.DepartmentsBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0434\u0440\u044b", None))

        self.LoginLabel.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.PasswordLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.ReturnButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

