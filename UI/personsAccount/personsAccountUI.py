# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'personsAccount.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(593, 568)
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
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.WindowTitle = QLabel(self.frame)
        self.WindowTitle.setObjectName(u"WindowTitle")
        self.WindowTitle.setStyleSheet(u"")
        self.WindowTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.WindowTitle)

        self.PersonInfoBlock = QFormLayout()
        self.PersonInfoBlock.setObjectName(u"PersonInfoBlock")
        self.PersonInfoLabelsBlock = QVBoxLayout()
        self.PersonInfoLabelsBlock.setSpacing(11)
        self.PersonInfoLabelsBlock.setObjectName(u"PersonInfoLabelsBlock")
        self.PersonInfoLabelsBlock.setContentsMargins(-1, 0, -1, -1)
        self.NameLabel = QLabel(self.frame)
        self.NameLabel.setObjectName(u"NameLabel")

        self.PersonInfoLabelsBlock.addWidget(self.NameLabel)

        self.LoginLabel = QLabel(self.frame)
        self.LoginLabel.setObjectName(u"LoginLabel")

        self.PersonInfoLabelsBlock.addWidget(self.LoginLabel)

        self.PhoneLabel = QLabel(self.frame)
        self.PhoneLabel.setObjectName(u"PhoneLabel")

        self.PersonInfoLabelsBlock.addWidget(self.PhoneLabel)

        self.RoleLabel = QLabel(self.frame)
        self.RoleLabel.setObjectName(u"RoleLabel")

        self.PersonInfoLabelsBlock.addWidget(self.RoleLabel)

        self.DepartmentLabel = QLabel(self.frame)
        self.DepartmentLabel.setObjectName(u"DepartmentLabel")

        self.PersonInfoLabelsBlock.addWidget(self.DepartmentLabel)


        self.PersonInfoBlock.setLayout(0, QFormLayout.LabelRole, self.PersonInfoLabelsBlock)

        self.PersonInfoValuesBlock = QVBoxLayout()
        self.PersonInfoValuesBlock.setSpacing(11)
        self.PersonInfoValuesBlock.setObjectName(u"PersonInfoValuesBlock")
        self.NameValue = QLabel(self.frame)
        self.NameValue.setObjectName(u"NameValue")

        self.PersonInfoValuesBlock.addWidget(self.NameValue)

        self.LoginValue = QLabel(self.frame)
        self.LoginValue.setObjectName(u"LoginValue")

        self.PersonInfoValuesBlock.addWidget(self.LoginValue)

        self.PhoneValue = QLabel(self.frame)
        self.PhoneValue.setObjectName(u"PhoneValue")

        self.PersonInfoValuesBlock.addWidget(self.PhoneValue)

        self.RoleValue = QLabel(self.frame)
        self.RoleValue.setObjectName(u"RoleValue")

        self.PersonInfoValuesBlock.addWidget(self.RoleValue)

        self.DepartmenValue = QLabel(self.frame)
        self.DepartmenValue.setObjectName(u"DepartmenValue")

        self.PersonInfoValuesBlock.addWidget(self.DepartmenValue)


        self.PersonInfoBlock.setLayout(0, QFormLayout.FieldRole, self.PersonInfoValuesBlock)


        self.verticalLayout_3.addLayout(self.PersonInfoBlock)

        self.ChangePasswordTitle = QLabel(self.frame)
        self.ChangePasswordTitle.setObjectName(u"ChangePasswordTitle")
        self.ChangePasswordTitle.setStyleSheet(u"")
        self.ChangePasswordTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.ChangePasswordTitle)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(17)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ChangePasswordBlock = QHBoxLayout()
        self.ChangePasswordBlock.setSpacing(6)
        self.ChangePasswordBlock.setObjectName(u"ChangePasswordBlock")
        self.ChangePasswordLabelsBlock = QVBoxLayout()
        self.ChangePasswordLabelsBlock.setSpacing(8)
        self.ChangePasswordLabelsBlock.setObjectName(u"ChangePasswordLabelsBlock")
        self.OldPasswordLabel = QLabel(self.frame)
        self.OldPasswordLabel.setObjectName(u"OldPasswordLabel")

        self.ChangePasswordLabelsBlock.addWidget(self.OldPasswordLabel)

        self.NewPasswordLabel = QLabel(self.frame)
        self.NewPasswordLabel.setObjectName(u"NewPasswordLabel")

        self.ChangePasswordLabelsBlock.addWidget(self.NewPasswordLabel)

        self.ConfirmNewPasswordLabel = QLabel(self.frame)
        self.ConfirmNewPasswordLabel.setObjectName(u"ConfirmNewPasswordLabel")

        self.ChangePasswordLabelsBlock.addWidget(self.ConfirmNewPasswordLabel)


        self.ChangePasswordBlock.addLayout(self.ChangePasswordLabelsBlock)

        self.ChangePasswordInputsBlock = QVBoxLayout()
        self.ChangePasswordInputsBlock.setObjectName(u"ChangePasswordInputsBlock")
        self.OldPasswordInput = QLineEdit(self.frame)
        self.OldPasswordInput.setObjectName(u"OldPasswordInput")
        self.OldPasswordInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.ChangePasswordInputsBlock.addWidget(self.OldPasswordInput)

        self.NewPasswordInput = QLineEdit(self.frame)
        self.NewPasswordInput.setObjectName(u"NewPasswordInput")
        self.NewPasswordInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.ChangePasswordInputsBlock.addWidget(self.NewPasswordInput)

        self.ConfirmNewPasswordInput = QLineEdit(self.frame)
        self.ConfirmNewPasswordInput.setObjectName(u"ConfirmNewPasswordInput")
        self.ConfirmNewPasswordInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.ChangePasswordInputsBlock.addWidget(self.ConfirmNewPasswordInput)


        self.ChangePasswordBlock.addLayout(self.ChangePasswordInputsBlock)


        self.verticalLayout.addLayout(self.ChangePasswordBlock)

        self.ChangePasswordButton = QPushButton(self.frame)
        self.ChangePasswordButton.setObjectName(u"ChangePasswordButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChangePasswordButton.sizePolicy().hasHeightForWidth())
        self.ChangePasswordButton.setSizePolicy(sizePolicy)
        self.ChangePasswordButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.verticalLayout.addWidget(self.ChangePasswordButton)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.ChangePhoneTitle = QLabel(self.frame)
        self.ChangePhoneTitle.setObjectName(u"ChangePhoneTitle")
        self.ChangePhoneTitle.setStyleSheet(u"")
        self.ChangePhoneTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.ChangePhoneTitle)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(17)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ChangePhoneBlock = QHBoxLayout()
        self.ChangePhoneBlock.setObjectName(u"ChangePhoneBlock")
        self.ChangePhoneLabel = QLabel(self.frame)
        self.ChangePhoneLabel.setObjectName(u"ChangePhoneLabel")

        self.ChangePhoneBlock.addWidget(self.ChangePhoneLabel)

        self.ChangePhoneInput = QLineEdit(self.frame)
        self.ChangePhoneInput.setObjectName(u"ChangePhoneInput")
        self.ChangePhoneInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.ChangePhoneBlock.addWidget(self.ChangePhoneInput)


        self.verticalLayout_2.addLayout(self.ChangePhoneBlock)

        self.ChangePhoneButton = QPushButton(self.frame)
        self.ChangePhoneButton.setObjectName(u"ChangePhoneButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ChangePhoneButton.sizePolicy().hasHeightForWidth())
        self.ChangePhoneButton.setSizePolicy(sizePolicy1)
        self.ChangePhoneButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.verticalLayout_2.addWidget(self.ChangePhoneButton)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.ReturnButton = QPushButton(self.frame)
        self.ReturnButton.setObjectName(u"ReturnButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ReturnButton.sizePolicy().hasHeightForWidth())
        self.ReturnButton.setSizePolicy(sizePolicy2)
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

        self.verticalLayout_3.addWidget(self.ReturnButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.ReturnButton.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.WindowTitle.setText(QCoreApplication.translate("Dialog", u"\u041b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442", None))
        self.NameLabel.setText(QCoreApplication.translate("Dialog", u"\u0424\u0418\u041e:", None))
        self.LoginLabel.setText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.PhoneLabel.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.RoleLabel.setText(QCoreApplication.translate("Dialog", u"\u0420\u043e\u043b\u044c:", None))
        self.DepartmentLabel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0434\u0435\u043b:", None))
        self.NameValue.setText(QCoreApplication.translate("Dialog", u"\u044b\u0432\u0430\u0432\u0430", None))
        self.LoginValue.setText(QCoreApplication.translate("Dialog", u"\u044b\u0432\u0430", None))
        self.PhoneValue.setText(QCoreApplication.translate("Dialog", u"\u0432\u044b\u0430", None))
        self.RoleValue.setText(QCoreApplication.translate("Dialog", u"\u044b\u0432\u0430", None))
        self.DepartmenValue.setText(QCoreApplication.translate("Dialog", u"\u044b\u0432\u0430", None))
        self.ChangePasswordTitle.setText(QCoreApplication.translate("Dialog", u"\u0421\u043c\u0435\u043d\u0430 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.OldPasswordLabel.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0440\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.NewPasswordLabel.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.ConfirmNewPasswordLabel.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435:", None))
        self.ChangePasswordButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.ChangePhoneTitle.setText(QCoreApplication.translate("Dialog", u"\u0421\u043c\u0435\u043d\u0430 \u043d\u043e\u043c\u0435\u0440\u0430 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.ChangePhoneLabel.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.ChangePhoneButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.ReturnButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

