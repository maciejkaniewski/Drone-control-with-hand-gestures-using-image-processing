# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)
from resources import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        icon = QIcon()
        icon.addFile(u":/images/images/drone.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: #393E46;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setVerticalSpacing(9)
        self.gridLayout.setContentsMargins(12, -1, 12, 6)
        self.QGroupBox_Camera_Feed = QGroupBox(self.centralwidget)
        self.QGroupBox_Camera_Feed.setObjectName(u"QGroupBox_Camera_Feed")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.QGroupBox_Camera_Feed.sizePolicy().hasHeightForWidth())
        self.QGroupBox_Camera_Feed.setSizePolicy(sizePolicy1)
        self.QGroupBox_Camera_Feed.setMaximumSize(QSize(620, 16777215))
        self.QGroupBox_Camera_Feed.setStyleSheet(u"QGroupBox#QGroupBox_Camera_Feed {\n"
"    background-color:  #222831;\n"
"    border: 2px solid gray;\n"
"	 border-color: #00ADB5;\n"
"    border-radius: 8px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_Camera_Feed {\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.QGroupBox_Camera_Feed)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(12, 12, 12, 12)
        self.QLabel_Camera_Feed = QLabel(self.QGroupBox_Camera_Feed)
        self.QLabel_Camera_Feed.setObjectName(u"QLabel_Camera_Feed")
        self.QLabel_Camera_Feed.setStyleSheet(u"QLabel#QLabel_Camera_Feed{\n"
"    border-radius: 8px;\n"
"}")

        self.gridLayout_6.addWidget(self.QLabel_Camera_Feed, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.QGroupBox_Camera_Feed, 0, 0, 1, 1)

        self.QGroupBox_2 = QGroupBox(self.centralwidget)
        self.QGroupBox_2.setObjectName(u"QGroupBox_2")
        self.QGroupBox_2.setStyleSheet(u"QGroupBox#QGroupBox_2 {\n"
"    background-color:  #222831;\n"
"    border: 2px solid gray;\n"
"	 border-color: #00ADB5;\n"
"    border-radius: 8px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_2 {\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")

        self.gridLayout.addWidget(self.QGroupBox_2, 0, 1, 1, 1)

        self.QGroupBox_3 = QGroupBox(self.centralwidget)
        self.QGroupBox_3.setObjectName(u"QGroupBox_3")
        self.QGroupBox_3.setStyleSheet(u"QGroupBox#QGroupBox_3 {\n"
"    background-color:  #222831;\n"
"    border: 2px solid gray;\n"
"	 border-color: #00ADB5;\n"
"    border-radius: 8px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_3 {\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")

        self.gridLayout.addWidget(self.QGroupBox_3, 1, 0, 1, 1)

        self.QGroupBox_1 = QGroupBox(self.centralwidget)
        self.QGroupBox_1.setObjectName(u"QGroupBox_1")
        self.QGroupBox_1.setStyleSheet(u"QGroupBox#QGroupBox_1 {\n"
"    background-color:  #222831;\n"
"    border: 2px solid gray;\n"
"	 border-color: #00ADB5;\n"
"    border-radius: 8px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_1 {\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")

        self.gridLayout.addWidget(self.QGroupBox_1, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Drone Control Application", None))
        self.QGroupBox_Camera_Feed.setTitle(QCoreApplication.translate("MainWindow", u"Camera Feed", None))
        self.QLabel_Camera_Feed.setText("")
        self.QGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.QGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.QGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Logs", None))
    # retranslateUi

