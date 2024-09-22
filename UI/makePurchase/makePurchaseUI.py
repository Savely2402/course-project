# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'makePurchase.ui'
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
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(593, 527)
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WindowTitle.sizePolicy().hasHeightForWidth())
        self.WindowTitle.setSizePolicy(sizePolicy)
        self.WindowTitle.setStyleSheet(u"")
        self.WindowTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.WindowTitle)

        self.PurchaseDetails1Block = QVBoxLayout()
        self.PurchaseDetails1Block.setSpacing(17)
        self.PurchaseDetails1Block.setObjectName(u"PurchaseDetails1Block")
        self.PurchaseDetails1HBlock = QHBoxLayout()
        self.PurchaseDetails1HBlock.setSpacing(6)
        self.PurchaseDetails1HBlock.setObjectName(u"PurchaseDetails1HBlock")
        self.PurchaseDetails1LabelsBlock = QVBoxLayout()
        self.PurchaseDetails1LabelsBlock.setSpacing(8)
        self.PurchaseDetails1LabelsBlock.setObjectName(u"PurchaseDetails1LabelsBlock")
        self.TotalDepartmentBudgetbel = QLabel(self.frame)
        self.TotalDepartmentBudgetbel.setObjectName(u"TotalDepartmentBudgetbel")

        self.PurchaseDetails1LabelsBlock.addWidget(self.TotalDepartmentBudgetbel)

        self.PurchaseNameLabel = QLabel(self.frame)
        self.PurchaseNameLabel.setObjectName(u"PurchaseNameLabel")

        self.PurchaseDetails1LabelsBlock.addWidget(self.PurchaseNameLabel)


        self.PurchaseDetails1HBlock.addLayout(self.PurchaseDetails1LabelsBlock)

        self.PurchaseDetails1InputsBlock = QVBoxLayout()
        self.PurchaseDetails1InputsBlock.setObjectName(u"PurchaseDetails1InputsBlock")
        self.TotalDepartmentBudgetInput = QLineEdit(self.frame)
        self.TotalDepartmentBudgetInput.setObjectName(u"TotalDepartmentBudgetInput")
        self.TotalDepartmentBudgetInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.PurchaseDetails1InputsBlock.addWidget(self.TotalDepartmentBudgetInput)

        self.PurchaseNameInput = QLineEdit(self.frame)
        self.PurchaseNameInput.setObjectName(u"PurchaseNameInput")
        self.PurchaseNameInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.PurchaseDetails1InputsBlock.addWidget(self.PurchaseNameInput)


        self.PurchaseDetails1HBlock.addLayout(self.PurchaseDetails1InputsBlock)


        self.PurchaseDetails1Block.addLayout(self.PurchaseDetails1HBlock)


        self.verticalLayout_3.addLayout(self.PurchaseDetails1Block)

        self.PurchaseDescription = QVBoxLayout()
        self.PurchaseDescription.setObjectName(u"PurchaseDescription")
        self.DescriptionLabel = QLabel(self.frame)
        self.DescriptionLabel.setObjectName(u"DescriptionLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DescriptionLabel.sizePolicy().hasHeightForWidth())
        self.DescriptionLabel.setSizePolicy(sizePolicy1)
        self.DescriptionLabel.setStyleSheet(u"")
        self.DescriptionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.PurchaseDescription.addWidget(self.DescriptionLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.DescriptionText = QTextEdit(self.frame)
        self.DescriptionText.setObjectName(u"DescriptionText")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.DescriptionText.sizePolicy().hasHeightForWidth())
        self.DescriptionText.setSizePolicy(sizePolicy2)
        self.DescriptionText.setStyleSheet(u"border: 2px solid rgb(191, 233, 123);\n"
"border-radius: 15px;")

        self.PurchaseDescription.addWidget(self.DescriptionText)


        self.verticalLayout_3.addLayout(self.PurchaseDescription)

        self.PurchaseDetails2Block = QHBoxLayout()
        self.PurchaseDetails2Block.setSpacing(6)
        self.PurchaseDetails2Block.setObjectName(u"PurchaseDetails2Block")
        self.PurchaseDetails2LabelsBlock = QVBoxLayout()
        self.PurchaseDetails2LabelsBlock.setSpacing(8)
        self.PurchaseDetails2LabelsBlock.setObjectName(u"PurchaseDetails2LabelsBlock")
        self.CurrentPriceLabel = QLabel(self.frame)
        self.CurrentPriceLabel.setObjectName(u"CurrentPriceLabel")

        self.PurchaseDetails2LabelsBlock.addWidget(self.CurrentPriceLabel)

        self.QuantityLabel = QLabel(self.frame)
        self.QuantityLabel.setObjectName(u"QuantityLabel")

        self.PurchaseDetails2LabelsBlock.addWidget(self.QuantityLabel)

        self.TotalPriceLabel = QLabel(self.frame)
        self.TotalPriceLabel.setObjectName(u"TotalPriceLabel")
        self.TotalPriceLabel.setStyleSheet(u"font-weight: 700;")

        self.PurchaseDetails2LabelsBlock.addWidget(self.TotalPriceLabel)


        self.PurchaseDetails2Block.addLayout(self.PurchaseDetails2LabelsBlock)

        self.PurchaseDetails2InputsBlock = QVBoxLayout()
        self.PurchaseDetails2InputsBlock.setObjectName(u"PurchaseDetails2InputsBlock")
        self.CurrentPriceInput = QLineEdit(self.frame)
        self.CurrentPriceInput.setObjectName(u"CurrentPriceInput")
        self.CurrentPriceInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.PurchaseDetails2InputsBlock.addWidget(self.CurrentPriceInput)

        self.QuantityInput = QLineEdit(self.frame)
        self.QuantityInput.setObjectName(u"QuantityInput")
        self.QuantityInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.PurchaseDetails2InputsBlock.addWidget(self.QuantityInput)

        self.TotalPriceInput = QLineEdit(self.frame)
        self.TotalPriceInput.setObjectName(u"TotalPriceInput")
        self.TotalPriceInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.PurchaseDetails2InputsBlock.addWidget(self.TotalPriceInput)


        self.PurchaseDetails2Block.addLayout(self.PurchaseDetails2InputsBlock)


        self.verticalLayout_3.addLayout(self.PurchaseDetails2Block)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.BuyButton = QPushButton(self.frame)
        self.BuyButton.setObjectName(u"BuyButton")
        self.BuyButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.verticalLayout_3.addWidget(self.BuyButton)

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

        self.verticalLayout_3.addWidget(self.ReturnButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.ReturnButton.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.WindowTitle.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0435 \u043f\u043e\u043a\u0443\u043f\u043a\u0438", None))
        self.TotalDepartmentBudgetbel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0449\u0438\u0439 \u0431\u044e\u0434\u0436\u0435\u0442 \u043e\u0442\u0434\u0435\u043b\u0430:", None))
        self.PurchaseNameLabel.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u044f \u043f\u043e\u043a\u0443\u043f\u043a\u0438:", None))
        self.DescriptionLabel.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.CurrentPriceLabel.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c:", None))
        self.QuantityLabel.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e: ", None))
        self.TotalPriceLabel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0449\u0430\u044f \u0446\u0435\u043d\u0430:", None))
        self.BuyButton.setText(QCoreApplication.translate("Dialog", u"\u041a\u0443\u043f\u0438\u0442\u044c", None))
        self.ReturnButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

