# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'departmentsListAdmin.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

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

        self.SearchDepartmentBlock = QHBoxLayout()
        self.SearchDepartmentBlock.setObjectName(u"SearchDepartmentBlock")
        self.SearchDepartmentLabel = QLabel(self.frame)
        self.SearchDepartmentLabel.setObjectName(u"SearchDepartmentLabel")
        sizePolicy.setHeightForWidth(self.SearchDepartmentLabel.sizePolicy().hasHeightForWidth())
        self.SearchDepartmentLabel.setSizePolicy(sizePolicy)

        self.SearchDepartmentBlock.addWidget(self.SearchDepartmentLabel)

        self.SearchDepartmentInput = QLineEdit(self.frame)
        self.SearchDepartmentInput.setObjectName(u"SearchDepartmentInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SearchDepartmentInput.sizePolicy().hasHeightForWidth())
        self.SearchDepartmentInput.setSizePolicy(sizePolicy1)
        self.SearchDepartmentInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.SearchDepartmentBlock.addWidget(self.SearchDepartmentInput)


        self.verticalLayout.addLayout(self.SearchDepartmentBlock)

        self.ActionsButtonsBlock = QHBoxLayout()
        self.ActionsButtonsBlock.setObjectName(u"ActionsButtonsBlock")
        self.AddDepartmentButton = QPushButton(self.frame)
        self.AddDepartmentButton.setObjectName(u"AddDepartmentButton")
        self.AddDepartmentButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.ActionsButtonsBlock.addWidget(self.AddDepartmentButton)

        self.DeleteDepartmentButton = QPushButton(self.frame)
        self.DeleteDepartmentButton.setObjectName(u"DeleteDepartmentButton")
        self.DeleteDepartmentButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.ActionsButtonsBlock.addWidget(self.DeleteDepartmentButton)


        self.verticalLayout.addLayout(self.ActionsButtonsBlock)

        self.DepartmentsTable = QTableView(self.frame)
        self.DepartmentsTable.setObjectName(u"DepartmentsTable")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.DepartmentsTable.sizePolicy().hasHeightForWidth())
        self.DepartmentsTable.setSizePolicy(sizePolicy2)
        self.DepartmentsTable.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.DepartmentsTable.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

        self.verticalLayout.addWidget(self.DepartmentsTable)

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
        self.WindowTitle.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0434\u0435\u043b\u044b", None))
        self.SearchDepartmentLabel.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0438\u0441\u043a: ", None))
        self.AddDepartmentButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0434\u0435\u043b", None))
        self.DeleteDepartmentButton.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043e\u0442\u0434\u0435\u043b", None))
        self.ReturnButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

