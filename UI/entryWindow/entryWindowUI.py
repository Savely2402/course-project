# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entryWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(611, 441)
        MainWindow.setMaximumSize(QSize(626, 441))
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
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.WindowTitle = QLabel(self.frame)
        self.WindowTitle.setObjectName(u"WindowTitle")
        self.WindowTitle.setStyleSheet(u"")
        self.WindowTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.WindowTitle)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LoginFormBlock = QVBoxLayout()
        self.LoginFormBlock.setSpacing(0)
        self.LoginFormBlock.setObjectName(u"LoginFormBlock")
        self.LoginLabel = QLabel(self.frame)
        self.LoginLabel.setObjectName(u"LoginLabel")

        self.LoginFormBlock.addWidget(self.LoginLabel)

        self.LoginInput = QLineEdit(self.frame)
        self.LoginInput.setObjectName(u"LoginInput")
        self.LoginInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.LoginFormBlock.addWidget(self.LoginInput)

        self.PasswordLabel = QLabel(self.frame)
        self.PasswordLabel.setObjectName(u"PasswordLabel")

        self.LoginFormBlock.addWidget(self.PasswordLabel)

        self.PasswordInput = QLineEdit(self.frame)
        self.PasswordInput.setObjectName(u"PasswordInput")
        self.PasswordInput.setStyleSheet(u"border-bottom: 1px solid rgb(191, 233, 123);")

        self.LoginFormBlock.addWidget(self.PasswordInput)


        self.verticalLayout.addLayout(self.LoginFormBlock)

        self.LoginButton = QPushButton(self.frame)
        self.LoginButton.setObjectName(u"LoginButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginButton.sizePolicy().hasHeightForWidth())
        self.LoginButton.setSizePolicy(sizePolicy)
        self.LoginButton.setStyleSheet(u"QPushButton {\n"
"border-radius: 10;\n"
"background-color: '#bfe97b';\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a7ca6b;\n"
"}")

        self.verticalLayout.addWidget(self.LoginButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expense tracker", None))
        self.WindowTitle.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043d\u043e \u0432\u0445\u043e\u0434\u0430 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.LoginLabel.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.PasswordLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

