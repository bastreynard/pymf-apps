# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

from waitingspinnerwidget import QtWaitingSpinner

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(1530, 1052)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        self.resultGroupBox = QGroupBox(Main)
        self.resultGroupBox.setObjectName(u"resultGroupBox")
        self.resultGroupBox.setGeometry(QRect(720, 10, 801, 641))
        self.resultGroupBox.setStyleSheet(u"QGroupBox#resultGroupBox {border:0;}")
        self.verticalLayoutWidget_2 = QWidget(self.resultGroupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 20, 291, 421))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 10, 10)
        self.moviePosterLabel = QLabel(self.verticalLayoutWidget_2)
        self.moviePosterLabel.setObjectName(u"moviePosterLabel")

        self.verticalLayout_2.addWidget(self.moviePosterLabel)

        self.verticalLayoutWidget = QWidget(self.resultGroupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(290, 20, 501, 621))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 10, 10)
        self.summaryLabel = QLabel(self.verticalLayoutWidget)
        self.summaryLabel.setObjectName(u"summaryLabel")
        self.summaryLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.summaryLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.summaryLabel)

        self.ratingGroupBox = QGroupBox(self.resultGroupBox)
        self.ratingGroupBox.setObjectName(u"ratingGroupBox")
        self.ratingGroupBox.setEnabled(True)
        self.ratingGroupBox.setGeometry(QRect(0, 440, 291, 41))
        self.ratingGroupBox.setStyleSheet(u"QGroupBox#ratingGroupBox {border:0;}")
        self.ratingGroupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.ratingGroupBox.setFlat(False)
        self.ratingGroupBox.setCheckable(False)
        self.layoutWidget = QWidget(self.ratingGroupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 291, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ratingImdbLogo = QLabel(self.layoutWidget)
        self.ratingImdbLogo.setObjectName(u"ratingImdbLogo")
        self.ratingImdbLogo.setTabletTracking(False)
        self.ratingImdbLogo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ratingImdbLogo.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.ratingImdbLogo)

        self.ratingLabel = QLabel(self.layoutWidget)
        self.ratingLabel.setObjectName(u"ratingLabel")
        self.ratingLabel.setTabletTracking(False)
        self.ratingLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ratingLabel.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.ratingLabel)

        self.imdbLinkLabel = QLabel(self.layoutWidget)
        self.imdbLinkLabel.setObjectName(u"imdbLinkLabel")
        self.imdbLinkLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.imdbLinkLabel.setWordWrap(True)
        self.imdbLinkLabel.setOpenExternalLinks(True)

        self.horizontalLayout_3.addWidget(self.imdbLinkLabel)

        self.spinnerImdb = QtWaitingSpinner(self.resultGroupBox)
        self.spinnerImdb.setObjectName(u"spinnerImdb")
        self.spinnerImdb.setGeometry(QRect(440, -100, 351, 741))
        self.tabWidget = QTabWidget(Main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 691, 641))
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.imdbSearchGroupBox = QGroupBox(self.tabWidgetPage1)
        self.imdbSearchGroupBox.setObjectName(u"imdbSearchGroupBox")
        self.imdbSearchGroupBox.setGeometry(QRect(0, 0, 681, 601))
        self.searchEdit = QLineEdit(self.imdbSearchGroupBox)
        self.searchEdit.setObjectName(u"searchEdit")
        self.searchEdit.setGeometry(QRect(10, 20, 261, 31))
        self.searchImdbButton = QPushButton(self.imdbSearchGroupBox)
        self.searchImdbButton.setObjectName(u"searchImdbButton")
        self.searchImdbButton.setGeometry(QRect(280, 20, 81, 31))
        self.searchImdbButton.setAutoDefault(True)
        self.imdbResultListView = QListView(self.imdbSearchGroupBox)
        self.imdbResultListView.setObjectName(u"imdbResultListView")
        self.imdbResultListView.setGeometry(QRect(10, 90, 661, 501))
        self.imdbResultListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.seriesCheckBox = QCheckBox(self.imdbSearchGroupBox)
        self.seriesCheckBox.setObjectName(u"seriesCheckBox")
        self.seriesCheckBox.setGeometry(QRect(10, 60, 131, 20))
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), u"IMDb")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.torrentSearchGroupBox = QGroupBox(self.tabWidgetPage2)
        self.torrentSearchGroupBox.setObjectName(u"torrentSearchGroupBox")
        self.torrentSearchGroupBox.setGeometry(QRect(0, 0, 681, 601))
        self.torrentSearchButton = QPushButton(self.torrentSearchGroupBox)
        self.torrentSearchButton.setObjectName(u"torrentSearchButton")
        self.torrentSearchButton.setGeometry(QRect(20, 20, 341, 31))
        self.torrentSearchButton.setAutoDefault(True)
        self.jackettCheckBox = QCheckBox(self.torrentSearchGroupBox)
        self.jackettCheckBox.setObjectName(u"jackettCheckBox")
        self.jackettCheckBox.setGeometry(QRect(80, 60, 101, 22))
        self.jackettCheckBox.setChecked(True)
        self.ytsCheckBox = QCheckBox(self.torrentSearchGroupBox)
        self.ytsCheckBox.setObjectName(u"ytsCheckBox")
        self.ytsCheckBox.setGeometry(QRect(20, 60, 61, 22))
        self.ytsCheckBox.setChecked(True)
        self.torrentResultListView = QListView(self.torrentSearchGroupBox)
        self.torrentResultListView.setObjectName(u"torrentResultListView")
        self.torrentResultListView.setGeometry(QRect(10, 90, 661, 231))
        self.torrentResultListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.torrentSendButton = QPushButton(self.torrentSearchGroupBox)
        self.torrentSendButton.setObjectName(u"torrentSendButton")
        self.torrentSendButton.setEnabled(True)
        self.torrentSendButton.setGeometry(QRect(230, 550, 131, 41))
        self.torrentInfoLabel = QLabel(self.torrentSearchGroupBox)
        self.torrentInfoLabel.setObjectName(u"torrentInfoLabel")
        self.torrentInfoLabel.setGeometry(QRect(10, 340, 341, 201))
        self.torrentInfoLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.torrentInfoLabel.setWordWrap(True)
        self.spinnerTorrent = QtWaitingSpinner(self.torrentSearchGroupBox)
        self.spinnerTorrent.setObjectName(u"spinnerTorrent")
        self.spinnerTorrent.setGeometry(QRect(10, 90, 661, 231))
        self.torrentUrlLabel = QLabel(self.torrentSearchGroupBox)
        self.torrentUrlLabel.setObjectName(u"torrentUrlLabel")
        self.torrentUrlLabel.setGeometry(QRect(20, 500, 341, 41))
        self.torrentUrlLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.torrentUrlLabel.setWordWrap(True)
        self.torrentUrlLabel.setOpenExternalLinks(True)
        self.settingsButton = QPushButton(self.torrentSearchGroupBox)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setEnabled(True)
        self.settingsButton.setGeometry(QRect(80, 550, 131, 41))
        self.tabWidget.addTab(self.tabWidgetPage2, "")

        self.retranslateUi(Main)

        self.tabWidget.setCurrentIndex(0)
        self.searchImdbButton.setDefault(False)
        self.torrentSearchButton.setDefault(True)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Movie Finder", None))
        self.resultGroupBox.setTitle("")
        self.moviePosterLabel.setText("")
        self.summaryLabel.setText("")
        self.ratingGroupBox.setTitle("")
        self.ratingImdbLogo.setText("")
        self.ratingLabel.setText("")
        self.imdbLinkLabel.setText("")
        self.imdbSearchGroupBox.setTitle(QCoreApplication.translate("Main", u"Search Movie on IMDb", None))
        self.searchEdit.setText("")
        self.searchImdbButton.setText(QCoreApplication.translate("Main", u"Search", None))
        self.seriesCheckBox.setText(QCoreApplication.translate("Main", u"Include TV Shows", None))
        self.torrentSearchGroupBox.setTitle(QCoreApplication.translate("Main", u"First select a movie from IMDb", None))
        self.torrentSearchButton.setText(QCoreApplication.translate("Main", u"Search", None))
        self.jackettCheckBox.setText(QCoreApplication.translate("Main", u"Jackett API", None))
        self.ytsCheckBox.setText(QCoreApplication.translate("Main", u"YTS", None))
        self.torrentSendButton.setText(QCoreApplication.translate("Main", u"Download", None))
        self.torrentInfoLabel.setText("")
        self.torrentUrlLabel.setText("")
        self.settingsButton.setText(QCoreApplication.translate("Main", u"Host Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("Main", u"Torrent", None))
    # retranslateUi

