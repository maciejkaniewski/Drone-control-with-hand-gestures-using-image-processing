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
    QProgressBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)
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
        self.QGroupBox_2 = QGroupBox(self.centralwidget)
        self.QGroupBox_2.setObjectName(u"QGroupBox_2")
        self.QGroupBox_2.setMinimumSize(QSize(620, 326))
        font = QFont()
        font.setBold(True)
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
        self.QFrame_Drone_Connection = QFrame(self.QGroupBox_Drone_Connection)
        self.QFrame_Drone_Connection.setObjectName(u"QFrame_Drone_Connection")
        self.QFrame_Drone_Connection.setStyleSheet(u"QFrame#QFrame_Drone_Connection {\n"
"    border-radius: 8px;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_Drone_Connection.setFrameShape(QFrame.Panel)
        self.QFrame_Drone_Connection.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.QFrame_Drone_Connection)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.QPushButton_Connect = QPushButton(self.QFrame_Drone_Connection)
        self.QPushButton_Connect.setObjectName(u"QPushButton_Connect")
        self.QPushButton_Connect.setMinimumSize(QSize(0, 35))
        self.QPushButton_Connect.setFont(font1)
        self.QPushButton_Connect.setStyleSheet(u"QPushButton#QPushButton_Connect{\n"
"	color:#EEEEEE;\n"
"}")

        self.horizontalLayout_2.addWidget(self.QPushButton_Connect)

        self.QLabel_WiFI = QLabel(self.QFrame_Drone_Connection)
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


        self.gridLayout_7.addWidget(self.QFrame_Drone_Connection, 0, 0, 1, 1)

        self.QGroupBox_Drone_Battery = QGroupBox(self.QGroupBox_2)
        self.QGroupBox_Drone_Battery.setObjectName(u"QGroupBox_Drone_Battery")
        self.QGroupBox_Drone_Battery.setGeometry(QRect(10, 200, 191, 111))
        self.QGroupBox_Drone_Battery.setStyleSheet(u"QGroupBox#QGroupBox_Drone_Battery {\n"
"    background-color:  #222831;\n"
"    border: 2px solid gray;\n"
"	 border-color: #00ADB5;\n"
"    border-radius: 8px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_Drone_Battery   {\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.gridLayout_8 = QGridLayout(self.QGroupBox_Drone_Battery)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(12, 12, 12, 12)
        self.QFrame_Drone_Battery = QFrame(self.QGroupBox_Drone_Battery)
        self.QFrame_Drone_Battery.setObjectName(u"QFrame_Drone_Battery")
        self.QFrame_Drone_Battery.setStyleSheet(u"QFrame#QFrame_Drone_Battery {\n"
"    border-radius: 8px;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_Drone_Battery.setFrameShape(QFrame.Panel)
        self.QFrame_Drone_Battery.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.QFrame_Drone_Battery)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.QProgressBar_Battery = QProgressBar(self.QFrame_Drone_Battery)
        self.QProgressBar_Battery.setObjectName(u"QProgressBar_Battery")
        self.QProgressBar_Battery.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.QProgressBar_Battery.sizePolicy().hasHeightForWidth())
        self.QProgressBar_Battery.setSizePolicy(sizePolicy1)
        self.QProgressBar_Battery.setStyleSheet(u"QProgressBar#QProgressBar_Battery {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"	 color:#EEEEEE;\n"
"}\n"
"\n"
"QProgressBar::chunk#QProgressBar_Battery  {\n"
"    background-color: #00ADB5;\n"
"    width: 20px;\n"
"}\n"
"")
        self.QProgressBar_Battery.setValue(0)
        self.QProgressBar_Battery.setAlignment(Qt.AlignCenter)
        self.QProgressBar_Battery.setTextVisible(True)
        self.QProgressBar_Battery.setOrientation(Qt.Horizontal)
        self.QProgressBar_Battery.setInvertedAppearance(False)

        self.gridLayout_9.addWidget(self.QProgressBar_Battery, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.QFrame_Drone_Battery, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.QGroupBox_2, 0, 1, 1, 1)

        self.QGroupBox_1 = QGroupBox(self.centralwidget)
        self.QGroupBox_1.setObjectName(u"QGroupBox_1")
        self.QGroupBox_1.setMinimumSize(QSize(620, 326))
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

        self.QGroupBox_Camera_Feed = QGroupBox(self.centralwidget)
        self.QGroupBox_Camera_Feed.setObjectName(u"QGroupBox_Camera_Feed")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.QGroupBox_Camera_Feed.sizePolicy().hasHeightForWidth())
        self.QGroupBox_Camera_Feed.setSizePolicy(sizePolicy2)
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
        self.QPushButton_Take_Off = QPushButton(self.QGroupBox_3)
        self.QPushButton_Take_Off.setObjectName(u"QPushButton_Take_Off")
        self.QPushButton_Take_Off.setEnabled(False)
        self.QPushButton_Take_Off.setGeometry(QRect(260, 260, 89, 25))
        self.QPushButton_Take_Off.setStyleSheet(u"QPushButton#QPushButton_Take_Off{\n"
"	color:#EEEEEE;\n"
"}")
        self.QPushButton_Land = QPushButton(self.QGroupBox_3)
        self.QPushButton_Land.setObjectName(u"QPushButton_Land")
        self.QPushButton_Land.setEnabled(False)
        self.QPushButton_Land.setGeometry(QRect(260, 290, 89, 25))
        self.QPushButton_Land.setStyleSheet(u"QPushButton#QPushButton_Land{\n"
"	color:#EEEEEE;\n"
"}")
        self.QFrame_Basic_Moves = QFrame(self.QGroupBox_3)
        self.QFrame_Basic_Moves.setObjectName(u"QFrame_Basic_Moves")
        self.QFrame_Basic_Moves.setGeometry(QRect(358, 81, 225, 168))
        self.QFrame_Basic_Moves.setStyleSheet(u"QFrame#QFrame_Basic_Moves {\n"
"    border-radius: 64px;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_Basic_Moves.setFrameShape(QFrame.StyledPanel)
        self.QFrame_Basic_Moves.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.QFrame_Basic_Moves)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.QPushButton_Backward = QPushButton(self.QFrame_Basic_Moves)
        self.QPushButton_Backward.setObjectName(u"QPushButton_Backward")
        self.QPushButton_Backward.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.QPushButton_Backward.sizePolicy().hasHeightForWidth())
        self.QPushButton_Backward.setSizePolicy(sizePolicy3)
        self.QPushButton_Backward.setMinimumSize(QSize(65, 45))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/backward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Backward.setIcon(icon1)
        self.QPushButton_Backward.setIconSize(QSize(40, 40))

        self.gridLayout_11.addWidget(self.QPushButton_Backward, 2, 2, 1, 1)

        self.QPushButton_Forward = QPushButton(self.QFrame_Basic_Moves)
        self.QPushButton_Forward.setObjectName(u"QPushButton_Forward")
        self.QPushButton_Forward.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.QPushButton_Forward.sizePolicy().hasHeightForWidth())
        self.QPushButton_Forward.setSizePolicy(sizePolicy3)
        self.QPushButton_Forward.setMinimumSize(QSize(65, 45))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Forward.setIcon(icon2)
        self.QPushButton_Forward.setIconSize(QSize(40, 40))

        self.gridLayout_11.addWidget(self.QPushButton_Forward, 0, 2, 1, 1)

        self.QPushButton_Dummy1 = QPushButton(self.QFrame_Basic_Moves)
        self.QPushButton_Dummy1.setObjectName(u"QPushButton_Dummy1")
        self.QPushButton_Dummy1.setEnabled(False)
        self.QPushButton_Dummy1.setMinimumSize(QSize(65, 45))
        self.QPushButton_Dummy1.setFlat(True)

        self.gridLayout_11.addWidget(self.QPushButton_Dummy1, 1, 2, 1, 1)

        self.QPushButton_Right = QPushButton(self.QFrame_Basic_Moves)
        self.QPushButton_Right.setObjectName(u"QPushButton_Right")
        self.QPushButton_Right.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.QPushButton_Right.sizePolicy().hasHeightForWidth())
        self.QPushButton_Right.setSizePolicy(sizePolicy3)
        self.QPushButton_Right.setMinimumSize(QSize(65, 45))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Right.setIcon(icon3)
        self.QPushButton_Right.setIconSize(QSize(40, 40))

        self.gridLayout_11.addWidget(self.QPushButton_Right, 1, 3, 1, 1)

        self.QPushButton_Left = QPushButton(self.QFrame_Basic_Moves)
        self.QPushButton_Left.setObjectName(u"QPushButton_Left")
        self.QPushButton_Left.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.QPushButton_Left.sizePolicy().hasHeightForWidth())
        self.QPushButton_Left.setSizePolicy(sizePolicy3)
        self.QPushButton_Left.setMinimumSize(QSize(65, 45))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Left.setIcon(icon4)
        self.QPushButton_Left.setIconSize(QSize(40, 40))

        self.gridLayout_11.addWidget(self.QPushButton_Left, 1, 0, 1, 1)

        self.QFrame_Advanced_Moves = QFrame(self.QGroupBox_3)
        self.QFrame_Advanced_Moves.setObjectName(u"QFrame_Advanced_Moves")
        self.QFrame_Advanced_Moves.setGeometry(QRect(41, 81, 225, 168))
        self.QFrame_Advanced_Moves.setStyleSheet(u"QFrame#QFrame_Advanced_Moves {\n"
"    border-radius: 64px;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_Advanced_Moves.setFrameShape(QFrame.StyledPanel)
        self.QFrame_Advanced_Moves.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.QFrame_Advanced_Moves)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.QPushButton_Down = QPushButton(self.QFrame_Advanced_Moves)
        self.QPushButton_Down.setObjectName(u"QPushButton_Down")
        self.QPushButton_Down.setEnabled(False)
        self.QPushButton_Down.setMinimumSize(QSize(65, 45))
        icon5 = QIcon()
        icon5.addFile(u":/images/images/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Down.setIcon(icon5)
        self.QPushButton_Down.setIconSize(QSize(40, 40))

        self.gridLayout_12.addWidget(self.QPushButton_Down, 2, 2, 1, 1)

        self.QPushButton_Up = QPushButton(self.QFrame_Advanced_Moves)
        self.QPushButton_Up.setObjectName(u"QPushButton_Up")
        self.QPushButton_Up.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.QPushButton_Up.sizePolicy().hasHeightForWidth())
        self.QPushButton_Up.setSizePolicy(sizePolicy3)
        self.QPushButton_Up.setMinimumSize(QSize(65, 45))
        icon6 = QIcon()
        icon6.addFile(u":/images/images/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Up.setIcon(icon6)
        self.QPushButton_Up.setIconSize(QSize(40, 40))

        self.gridLayout_12.addWidget(self.QPushButton_Up, 0, 2, 1, 1)

        self.QPushButton_Dummy2 = QPushButton(self.QFrame_Advanced_Moves)
        self.QPushButton_Dummy2.setObjectName(u"QPushButton_Dummy2")
        self.QPushButton_Dummy2.setEnabled(False)
        self.QPushButton_Dummy2.setMinimumSize(QSize(65, 45))
        self.QPushButton_Dummy2.setFlat(True)

        self.gridLayout_12.addWidget(self.QPushButton_Dummy2, 1, 2, 1, 1)

        self.QPushButton_Rotate_Left = QPushButton(self.QFrame_Advanced_Moves)
        self.QPushButton_Rotate_Left.setObjectName(u"QPushButton_Rotate_Left")
        self.QPushButton_Rotate_Left.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.QPushButton_Rotate_Left.sizePolicy().hasHeightForWidth())
        self.QPushButton_Rotate_Left.setSizePolicy(sizePolicy3)
        self.QPushButton_Rotate_Left.setMinimumSize(QSize(65, 45))
        icon7 = QIcon()
        icon7.addFile(u":/images/images/rotate_left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Rotate_Left.setIcon(icon7)
        self.QPushButton_Rotate_Left.setIconSize(QSize(40, 40))

        self.gridLayout_12.addWidget(self.QPushButton_Rotate_Left, 1, 0, 1, 1)

        self.QPushButton_Rotate_Right = QPushButton(self.QFrame_Advanced_Moves)
        self.QPushButton_Rotate_Right.setObjectName(u"QPushButton_Rotate_Right")
        self.QPushButton_Rotate_Right.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.QPushButton_Rotate_Right.sizePolicy().hasHeightForWidth())
        self.QPushButton_Rotate_Right.setSizePolicy(sizePolicy3)
        self.QPushButton_Rotate_Right.setMinimumSize(QSize(65, 45))
        icon8 = QIcon()
        icon8.addFile(u":/images/images/rotate_right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Rotate_Right.setIcon(icon8)
        self.QPushButton_Rotate_Right.setIconSize(QSize(40, 40))

        self.gridLayout_12.addWidget(self.QPushButton_Rotate_Right, 1, 3, 1, 1)


        self.gridLayout.addWidget(self.QGroupBox_3, 1, 0, 1, 1)

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
        self.QGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Utilities and settings", None))
        self.QGroupBox_Data_Collector.setTitle(QCoreApplication.translate("MainWindow", u"Data Collector", None))
        self.QPushButton_Save_Gesture.setText(QCoreApplication.translate("MainWindow", u"Save gesture", None))
        self.QPushButton_Clear_All_Gestures.setText(QCoreApplication.translate("MainWindow", u"Clear all gestures", None))
        self.QGroupBox_Drone_Connection.setTitle(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.QPushButton_Connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.QLabel_WiFI.setText("")
        self.QGroupBox_Drone_Battery.setTitle(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.QGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.QGroupBox_Camera_Feed.setTitle(QCoreApplication.translate("MainWindow", u"Camera Feed", None))
        self.QLabel_Camera_Feed.setText("")
        self.QGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.QPushButton_Take_Off.setText(QCoreApplication.translate("MainWindow", u"Take Off", None))
        self.QPushButton_Land.setText(QCoreApplication.translate("MainWindow", u"Land", None))
        self.QPushButton_Backward.setText("")
        self.QPushButton_Forward.setText("")
        self.QPushButton_Dummy1.setText("")
        self.QPushButton_Right.setText("")
        self.QPushButton_Left.setText("")
        self.QPushButton_Down.setText("")
        self.QPushButton_Up.setText("")
        self.QPushButton_Dummy2.setText("")
        self.QPushButton_Rotate_Left.setText("")
        self.QPushButton_Rotate_Right.setText("")
    # retranslateUi

