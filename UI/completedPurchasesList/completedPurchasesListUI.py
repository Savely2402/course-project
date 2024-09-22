# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'completedPurchasesList.ui'
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
        Dialog.resize(912, 343)
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

        self.SearchPurchasesBlock = QHBoxLayout()
        self.SearchPurchasesBlock.setObjectName(u"SearchPurchasesBlock")
        self.SearchPurchasesLabel = QLabel(self.frame)
        self.SearchPurchasesLabel.setObjectName(u"SearchPurchasesLabel")
        sizePolicy.setHeightForWidth(self.SearchPurchasesLabel.sizePolicy().hasHeightForWidth())
        self.SearchPurchasesLabel.setSizePolicy(sizePolicy)

        self.SearchPurchasesBlock.addWidget(self.SearchPurchasesLabel)

        self.SearchPurchasesInput = QLineEdit(self.frame)
        self.SearchPurchasesInput.setObjectName(u"SearchPurchasesInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SearchPurchasesInput.sizePolicy().hasHeightForWidth())
        self.SearchPurchasesInput.setSizePolicy(sizePolicy1)
        self.SearchPurchasesInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.SearchPurchasesBlock.addWidget(self.SearchPurchasesInput)


        self.verticalLayout.addLayout(self.SearchPurchasesBlock)

        self.PurchasesTable = QTableView(self.frame)
        self.PurchasesTable.setObjectName(u"PurchasesTable")

        self.verticalLayout.addWidget(self.PurchasesTable)

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
        self.WindowTitle.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u043d\u044b\u0445 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.SearchPurchasesLabel.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0438\u0441\u043a: ", None))
        self.ReturnButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

