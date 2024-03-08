# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.setWindowModality(Qt.NonModal)
        Settings.resize(382, 243)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        self.layoutWidget = QWidget(Settings)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 341, 211))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.hostTextEdit = QLineEdit(self.layoutWidget)
        self.hostTextEdit.setObjectName(u"hostTextEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.hostTextEdit)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.usernameTextEdit = QLineEdit(self.layoutWidget)
        self.usernameTextEdit.setObjectName(u"usernameTextEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.usernameTextEdit)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.passwordTextEdit = QLineEdit(self.layoutWidget)
        self.passwordTextEdit.setObjectName(u"passwordTextEdit")
        self.passwordTextEdit.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.passwordTextEdit)

        self.downloadDirTextEdit = QLineEdit(self.layoutWidget)
        self.downloadDirTextEdit.setObjectName(u"downloadDirTextEdit")
        self.downloadDirTextEdit.setEchoMode(QLineEdit.Normal)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.downloadDirTextEdit)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.jackettHostTextEdit = QLineEdit(self.layoutWidget)
        self.jackettHostTextEdit.setObjectName(u"jackettHostTextEdit")
        self.jackettHostTextEdit.setEchoMode(QLineEdit.Normal)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.jackettHostTextEdit)

        self.jackettApiKeyTextEdit = QLineEdit(self.layoutWidget)
        self.jackettApiKeyTextEdit.setObjectName(u"jackettApiKeyTextEdit")
        self.jackettApiKeyTextEdit.setEchoMode(QLineEdit.Normal)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.jackettApiKeyTextEdit)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAutoDefault(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.pushButton)


        self.retranslateUi(Settings)

        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.label.setText(QCoreApplication.translate("Settings", u"RPC URL", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("Settings", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("Settings", u"Download Directory", None))
        self.label_5.setText(QCoreApplication.translate("Settings", u"Jackett Host", None))
        self.label_6.setText(QCoreApplication.translate("Settings", u"Jacket API key", None))
        self.pushButton.setText(QCoreApplication.translate("Settings", u"OK", None))
    # retranslateUi

