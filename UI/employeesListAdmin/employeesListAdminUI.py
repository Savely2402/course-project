# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employeesListAdmin.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(698, 439)
        Dialog.setStyleSheet(u"background-color: 	rgb(191, 233, 123);\n"
"font-family: Myanmar Text;")
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFocusPolicy(Qt.FocusPolicy.NoFocus)
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

        self.SearchEmployeeBlock = QHBoxLayout()
        self.SearchEmployeeBlock.setObjectName(u"SearchEmployeeBlock")
        self.SearchEmployeeLabel = QLabel(self.frame)
        self.SearchEmployeeLabel.setObjectName(u"SearchEmployeeLabel")
        sizePolicy.setHeightForWidth(self.SearchEmployeeLabel.sizePolicy().hasHeightForWidth())
        self.SearchEmployeeLabel.setSizePolicy(sizePolicy)

        self.SearchEmployeeBlock.addWidget(self.SearchEmployeeLabel)

        self.SearchEmployeeInput = QLineEdit(self.frame)
        self.SearchEmployeeInput.setObjectName(u"SearchEmployeeInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SearchEmployeeInput.sizePolicy().hasHeightForWidth())
        self.SearchEmployeeInput.setSizePolicy(sizePolicy1)
        self.SearchEmployeeInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.SearchEmployeeBlock.addWidget(self.SearchEmployeeInput)


        self.verticalLayout.addLayout(self.SearchEmployeeBlock)

        self.ActionsButtonsBlock = QHBoxLayout()
        self.ActionsButtonsBlock.setObjectName(u"ActionsButtonsBlock")
        self.AddEmployeeButton = QPushButton(self.frame)
        self.AddEmployeeButton.setObjectName(u"AddEmployeeButton")
        self.AddEmployeeButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.ActionsButtonsBlock.addWidget(self.AddEmployeeButton)

        self.DeleteEmployeeButton = QPushButton(self.frame)
        self.DeleteEmployeeButton.setObjectName(u"DeleteEmployeeButton")
        self.DeleteEmployeeButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.ActionsButtonsBlock.addWidget(self.DeleteEmployeeButton)


        self.verticalLayout.addLayout(self.ActionsButtonsBlock)

        self.EmployeesTable = QTableView(self.frame)
        self.EmployeesTable.setObjectName(u"EmployeesTable")
        sizePolicy.setHeightForWidth(self.EmployeesTable.sizePolicy().hasHeightForWidth())
        self.EmployeesTable.setSizePolicy(sizePolicy)
        self.EmployeesTable.setStyleSheet(u"background-color: green;\n"
"")

        self.verticalLayout.addWidget(self.EmployeesTable, 0, Qt.AlignmentFlag.AlignHCenter)

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


        self.verticalLayout_4.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.ReturnButton.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.WindowTitle.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
        self.SearchEmployeeLabel.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0438\u0441\u043a: ", None))
        self.AddEmployeeButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.DeleteEmployeeButton.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.ReturnButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

