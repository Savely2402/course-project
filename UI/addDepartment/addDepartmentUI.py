# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addDepartment.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(544, 302)
        Dialog.setStyleSheet(u"background-color: 	rgb(191, 233, 123);\n"
"font-family: Myanmar Text;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: white;\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.WindowTitle = QLabel(self.frame)
        self.WindowTitle.setObjectName(u"WindowTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WindowTitle.sizePolicy().hasHeightForWidth())
        self.WindowTitle.setSizePolicy(sizePolicy)
        self.WindowTitle.setStyleSheet(u"")
        self.WindowTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.WindowTitle, 0, Qt.AlignmentFlag.AlignHCenter)

        self.DepartmentNameForm = QFormLayout()
        self.DepartmentNameForm.setObjectName(u"DepartmentNameForm")
        self.DepartmentNameForm.setContentsMargins(-1, 0, -1, 0)
        self.DepartmentNameLabel = QLabel(self.frame)
        self.DepartmentNameLabel.setObjectName(u"DepartmentNameLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DepartmentNameLabel.sizePolicy().hasHeightForWidth())
        self.DepartmentNameLabel.setSizePolicy(sizePolicy1)

        self.DepartmentNameForm.setWidget(0, QFormLayout.LabelRole, self.DepartmentNameLabel)

        self.DepartmentNameInput = QLineEdit(self.frame)
        self.DepartmentNameInput.setObjectName(u"DepartmentNameInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.DepartmentNameInput.sizePolicy().hasHeightForWidth())
        self.DepartmentNameInput.setSizePolicy(sizePolicy2)
        self.DepartmentNameInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.DepartmentNameForm.setWidget(0, QFormLayout.FieldRole, self.DepartmentNameInput)


        self.verticalLayout.addLayout(self.DepartmentNameForm)

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

        self.verticalLayout.addWidget(self.AddDepartmentButton)

        self.ReturnButton = QPushButton(self.frame)
        self.ReturnButton.setObjectName(u"ReturnButton")
        sizePolicy1.setHeightForWidth(self.ReturnButton.sizePolicy().hasHeightForWidth())
        self.ReturnButton.setSizePolicy(sizePolicy1)
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


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.ReturnButton.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.WindowTitle.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0434\u0435\u043b", None))
        self.DepartmentNameLabel.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.AddDepartmentButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.ReturnButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

