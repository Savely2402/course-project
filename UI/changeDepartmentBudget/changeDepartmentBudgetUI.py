# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangeDepartmentBudget.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(580, 277)
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
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TotalDepartmentBudgetLabel = QLabel(self.frame)
        self.TotalDepartmentBudgetLabel.setObjectName(u"TotalDepartmentBudgetLabel")
        sizePolicy.setHeightForWidth(self.TotalDepartmentBudgetLabel.sizePolicy().hasHeightForWidth())
        self.TotalDepartmentBudgetLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.TotalDepartmentBudgetLabel)

        self.TotalDepartmentBudgetValue = QLabel(self.frame)
        self.TotalDepartmentBudgetValue.setObjectName(u"TotalDepartmentBudgetValue")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TotalDepartmentBudgetValue.sizePolicy().hasHeightForWidth())
        self.TotalDepartmentBudgetValue.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.TotalDepartmentBudgetValue)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.DepartmentLabel = QLabel(self.frame)
        self.DepartmentLabel.setObjectName(u"DepartmentLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.DepartmentLabel.sizePolicy().hasHeightForWidth())
        self.DepartmentLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.DepartmentLabel)

        self.DepartmentValue = QLabel(self.frame)
        self.DepartmentValue.setObjectName(u"DepartmentValue")
        sizePolicy1.setHeightForWidth(self.DepartmentValue.sizePolicy().hasHeightForWidth())
        self.DepartmentValue.setSizePolicy(sizePolicy1)
        self.DepartmentValue.setStyleSheet(u"border: 1px solid rgb(191, 233, 123);\n"
"border-radius: 20;\n"
"padding: 5px;\n"
"min-height: 30px;")

        self.horizontalLayout_2.addWidget(self.DepartmentValue)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.SumLabel = QLabel(self.frame)
        self.SumLabel.setObjectName(u"SumLabel")
        sizePolicy2.setHeightForWidth(self.SumLabel.sizePolicy().hasHeightForWidth())
        self.SumLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.SumLabel)

        self.SumInput = QLineEdit(self.frame)
        self.SumInput.setObjectName(u"SumInput")
        self.SumInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.horizontalLayout_3.addWidget(self.SumInput)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.GiveAwayButton = QPushButton(self.frame)
        self.GiveAwayButton.setObjectName(u"GiveAwayButton")
        self.GiveAwayButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.verticalLayout.addWidget(self.GiveAwayButton)

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
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0411\u044e\u0434\u0436\u0435\u0442", None))
        self.TotalDepartmentBudgetLabel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0449\u0438\u0439 \u0431\u044e\u0434\u0436\u0435\u0442 \u043e\u0442\u0434\u0435\u043b\u0430: ", None))
        self.TotalDepartmentBudgetValue.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.DepartmentLabel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0434\u0435\u043b: ", None))
        self.DepartmentValue.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u043d\u0446\u0435\u043b\u044f\u0440\u0438\u044f", None))
        self.SumLabel.setText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u043c\u043c\u0430:", None))
        self.GiveAwayButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u044c", None))
        self.ReturnButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

