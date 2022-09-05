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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)
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
        self.QGroupBox_1 = QGroupBox(self.centralwidget)
        self.QGroupBox_1.setObjectName(u"QGroupBox_1")
        self.QGroupBox_1.setMinimumSize(QSize(620, 326))
        font = QFont()
        font.setBold(True)
        self.QGroupBox_1.setFont(font)
        self.QGroupBox_1.setStyleSheet(u"QGroupBox#QGroupBox_1 {\n"
"    background-color:  #222831;\n"
"    border: 2px solid gray;\n"
"	 border-color: #00ADB5;\n"
"    border-radius: 8px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"	 font-size: 16px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_1 {\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.QGroupBox_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(16, 16, 16, 16)
        self.QTextBrowser_Logs = QTextBrowser(self.QGroupBox_1)
        self.QTextBrowser_Logs.setObjectName(u"QTextBrowser_Logs")
        self.QTextBrowser_Logs.setStyleSheet(u"QTextBrowser#QTextBrowser_Logs {\n"
"	color:#EEEEEE;\n"
"}")

        self.gridLayout_2.addWidget(self.QTextBrowser_Logs, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.QGroupBox_1, 1, 1, 1, 1)

        self.QGroupBox_3 = QGroupBox(self.centralwidget)
        self.QGroupBox_3.setObjectName(u"QGroupBox_3")
        self.QGroupBox_3.setMinimumSize(QSize(620, 326))
        self.QGroupBox_3.setFont(font)
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

        self.QGroupBox_Camera_Feed = QGroupBox(self.centralwidget)
        self.QGroupBox_Camera_Feed.setObjectName(u"QGroupBox_Camera_Feed")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.QGroupBox_Camera_Feed.sizePolicy().hasHeightForWidth())
        self.QGroupBox_Camera_Feed.setSizePolicy(sizePolicy1)
        self.QGroupBox_Camera_Feed.setMinimumSize(QSize(620, 326))
        self.QGroupBox_Camera_Feed.setMaximumSize(QSize(620, 16777215))
        self.QGroupBox_Camera_Feed.setFont(font)
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
        self.QGroupBox_2.setMinimumSize(QSize(620, 326))
        self.QGroupBox_2.setFont(font)
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
        self.QGroupBox_Data_Collector = QGroupBox(self.QGroupBox_2)
        self.QGroupBox_Data_Collector.setObjectName(u"QGroupBox_Data_Collector")
        self.QGroupBox_Data_Collector.setGeometry(QRect(410, 200, 191, 111))
        self.QGroupBox_Data_Collector.setStyleSheet(u"QGroupBox#QGroupBox_Data_Collector {\n"
"    background-color:  #222831;\n"
"    border: 2px solid gray;\n"
"	 border-color: #00ADB5;\n"
"    border-radius: 8px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_Data_Collector  {\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.QGroupBox_Data_Collector)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(12, 12, 12, 12)
        self.QFrame_Data_Collector = QFrame(self.QGroupBox_Data_Collector)
        self.QFrame_Data_Collector.setObjectName(u"QFrame_Data_Collector")
        self.QFrame_Data_Collector.setStyleSheet(u"QFrame#QFrame_Data_Collector {\n"
"    border-radius: 8px;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_Data_Collector.setFrameShape(QFrame.Panel)
        self.QFrame_Data_Collector.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.QFrame_Data_Collector)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.QPushButton_Save_Gesture = QPushButton(self.QFrame_Data_Collector)
        self.QPushButton_Save_Gesture.setObjectName(u"QPushButton_Save_Gesture")
        font1 = QFont()
        font1.setPointSize(11)
        self.QPushButton_Save_Gesture.setFont(font1)
        self.QPushButton_Save_Gesture.setStyleSheet(u"QPushButton#QPushButton_Save_Gesture {\n"
"	color:#EEEEEE;\n"
"}")

        self.horizontalLayout.addWidget(self.QPushButton_Save_Gesture)

        self.QSpinBox_Gesture_Label = QSpinBox(self.QFrame_Data_Collector)
        self.QSpinBox_Gesture_Label.setObjectName(u"QSpinBox_Gesture_Label")
        self.QSpinBox_Gesture_Label.setStyleSheet(u"QSpinBox#QSpinBox_Gesture_Label {\n"
"	color:#EEEEEE;\n"
"}")
        self.QSpinBox_Gesture_Label.setMaximum(9)

        self.horizontalLayout.addWidget(self.QSpinBox_Gesture_Label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.QPushButton_Clear_All_Gestures = QPushButton(self.QFrame_Data_Collector)
        self.QPushButton_Clear_All_Gestures.setObjectName(u"QPushButton_Clear_All_Gestures")
        self.QPushButton_Clear_All_Gestures.setFont(font1)
        self.QPushButton_Clear_All_Gestures.setStyleSheet(u"QPushButton#QPushButton_Clear_All_Gestures{\n"
"	color:#EEEEEE;\n"
"}")

        self.verticalLayout.addWidget(self.QPushButton_Clear_All_Gestures)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.QFrame_Data_Collector, 0, 0, 1, 1)

        self.QGroupBox_Drone_Connection = QGroupBox(self.QGroupBox_2)
        self.QGroupBox_Drone_Connection.setObjectName(u"QGroupBox_Drone_Connection")
        self.QGroupBox_Drone_Connection.setGeometry(QRect(210, 200, 191, 111))
        self.QGroupBox_Drone_Connection.setStyleSheet(u"QGroupBox#QGroupBox_Drone_Connection {\n"
"    background-color:  #222831;\n"
"    border: 2px solid gray;\n"
"	 border-color: #00ADB5;\n"
"    border-radius: 8px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_Drone_Connection   {\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.gridLayout_7 = QGridLayout(self.QGroupBox_Drone_Connection)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(12, 12, 12, 12)
        self.QFrame_Data_Drone_Connection = QFrame(self.QGroupBox_Drone_Connection)
        self.QFrame_Data_Drone_Connection.setObjectName(u"QFrame_Data_Drone_Connection")
        self.QFrame_Data_Drone_Connection.setStyleSheet(u"QFrame#QFrame_Data_Collector {\n"
"    border-radius: 8px;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_Data_Drone_Connection.setFrameShape(QFrame.Panel)
        self.QFrame_Data_Drone_Connection.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.QFrame_Data_Drone_Connection)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.QPushButton_Connect = QPushButton(self.QFrame_Data_Drone_Connection)
        self.QPushButton_Connect.setObjectName(u"QPushButton_Connect")
        self.QPushButton_Connect.setMinimumSize(QSize(0, 35))
        self.QPushButton_Connect.setFont(font1)
        self.QPushButton_Connect.setStyleSheet(u"QPushButton#QPushButton_Connect{\n"
"	color:#EEEEEE;\n"
"}")

        self.horizontalLayout_2.addWidget(self.QPushButton_Connect)

        self.QLabel_WiFI = QLabel(self.QFrame_Data_Drone_Connection)
        self.QLabel_WiFI.setObjectName(u"QLabel_WiFI")
        sizePolicy.setHeightForWidth(self.QLabel_WiFI.sizePolicy().hasHeightForWidth())
        self.QLabel_WiFI.setSizePolicy(sizePolicy)
        self.QLabel_WiFI.setMinimumSize(QSize(35, 35))
        self.QLabel_WiFI.setMaximumSize(QSize(35, 35))
        self.QLabel_WiFI.setPixmap(QPixmap(u":/images/images/wifi_0.png"))
        self.QLabel_WiFI.setScaledContents(True)
        self.QLabel_WiFI.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.QLabel_WiFI)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.QFrame_Data_Drone_Connection, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.QGroupBox_2, 0, 1, 1, 1)

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
        self.QGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.QGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.QGroupBox_Camera_Feed.setTitle(QCoreApplication.translate("MainWindow", u"Camera Feed", None))
        self.QLabel_Camera_Feed.setText("")
        self.QGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Utilities and settings", None))
        self.QGroupBox_Data_Collector.setTitle(QCoreApplication.translate("MainWindow", u"Data Collector", None))
        self.QPushButton_Save_Gesture.setText(QCoreApplication.translate("MainWindow", u"Save gesture", None))
        self.QPushButton_Clear_All_Gestures.setText(QCoreApplication.translate("MainWindow", u"Clear all gestures", None))
        self.QGroupBox_Drone_Connection.setTitle(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.QPushButton_Connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.QLabel_WiFI.setText("")
    # retranslateUi

