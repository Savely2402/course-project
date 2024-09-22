# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'departmentsListAccountant.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

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
        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.SearchDepartmentBlock.addItem(self.horizontalSpacer)

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

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.SearchDepartmentBlock.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.SearchDepartmentBlock)

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

        self.ChangeDepartmentBudgetButton = QPushButton(self.frame)
        self.ChangeDepartmentBudgetButton.setObjectName(u"ChangeDepartmentBudgetButton")
        self.ChangeDepartmentBudgetButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.verticalLayout.addWidget(self.ChangeDepartmentBudgetButton)

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
        self.ChangeDepartmentBudgetButton.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0431\u044e\u0434\u0436\u0435\u0442 \u043e\u0442\u0434\u0435\u043b\u0430", None))
        self.ReturnButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

