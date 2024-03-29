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
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTextBrowser, QVBoxLayout,
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
        self.QGroupBox_1 = QGroupBox(self.centralwidget)
        self.QGroupBox_1.setObjectName(u"QGroupBox_1")
        self.QGroupBox_1.setMinimumSize(QSize(620, 326))
        font = QFont()
        font.setBold(True)
        self.QGroupBox_1.setFont(font)
        self.QGroupBox_1.setStyleSheet(u"QGroupBox#QGroupBox_1 {\n"
"    background-color:  #222831;\n"
"    border: 3px solid gray;\n"
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
"	border: 2px solid gray;\n"
"}")

        self.gridLayout_2.addWidget(self.QTextBrowser_Logs, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.QGroupBox_1, 1, 1, 1, 1)

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
"    border: 3px solid gray;\n"
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
"    border: 3px solid gray;\n"
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
        self.gridLayout_10 = QGridLayout(self.QGroupBox_3)
        self.gridLayout_10.setSpacing(16)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(16, 16, 16, 16)
        self.QFrame_Advanced_Moves = QFrame(self.QGroupBox_3)
        self.QFrame_Advanced_Moves.setObjectName(u"QFrame_Advanced_Moves")
        self.QFrame_Advanced_Moves.setStyleSheet(u"QFrame#QFrame_Advanced_Moves {\n"
"    border-radius: 64px;\n"
"	border: 2px solid gray;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_Advanced_Moves.setFrameShape(QFrame.StyledPanel)
        self.QFrame_Advanced_Moves.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.QFrame_Advanced_Moves)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.QPushButton_Down = QPushButton(self.QFrame_Advanced_Moves)
        self.QPushButton_Down.setObjectName(u"QPushButton_Down")
        self.QPushButton_Down.setEnabled(False)
        self.QPushButton_Down.setMinimumSize(QSize(65, 55))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Down.setIcon(icon1)
        self.QPushButton_Down.setIconSize(QSize(40, 40))

        self.gridLayout_12.addWidget(self.QPushButton_Down, 3, 3, 1, 1)

        self.QLabel_CW = QLabel(self.QFrame_Advanced_Moves)
        self.QLabel_CW.setObjectName(u"QLabel_CW")
        self.QLabel_CW.setStyleSheet(u"QLabel#QLabel_CW{\n"
"	color:#EEEEEE;\n"
"}")
        self.QLabel_CW.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.QLabel_CW, 2, 5, 1, 1)

        self.QPushButton_Dummy2 = QPushButton(self.QFrame_Advanced_Moves)
        self.QPushButton_Dummy2.setObjectName(u"QPushButton_Dummy2")
        self.QPushButton_Dummy2.setEnabled(False)
        self.QPushButton_Dummy2.setMinimumSize(QSize(65, 45))
        self.QPushButton_Dummy2.setFlat(True)

        self.gridLayout_12.addWidget(self.QPushButton_Dummy2, 2, 3, 1, 1)

        self.QPushButton_Rotate_Right = QPushButton(self.QFrame_Advanced_Moves)
        self.QPushButton_Rotate_Right.setObjectName(u"QPushButton_Rotate_Right")
        self.QPushButton_Rotate_Right.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.QPushButton_Rotate_Right.sizePolicy().hasHeightForWidth())
        self.QPushButton_Rotate_Right.setSizePolicy(sizePolicy2)
        self.QPushButton_Rotate_Right.setMinimumSize(QSize(65, 55))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/rotate_right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Rotate_Right.setIcon(icon2)
        self.QPushButton_Rotate_Right.setIconSize(QSize(40, 40))

        self.gridLayout_12.addWidget(self.QPushButton_Rotate_Right, 2, 4, 1, 1)

        self.QPushButton_Up = QPushButton(self.QFrame_Advanced_Moves)
        self.QPushButton_Up.setObjectName(u"QPushButton_Up")
        self.QPushButton_Up.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.QPushButton_Up.sizePolicy().hasHeightForWidth())
        self.QPushButton_Up.setSizePolicy(sizePolicy2)
        self.QPushButton_Up.setMinimumSize(QSize(65, 55))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Up.setIcon(icon3)
        self.QPushButton_Up.setIconSize(QSize(40, 40))

        self.gridLayout_12.addWidget(self.QPushButton_Up, 1, 3, 1, 1)

        self.QPushButton_Rotate_Left = QPushButton(self.QFrame_Advanced_Moves)
        self.QPushButton_Rotate_Left.setObjectName(u"QPushButton_Rotate_Left")
        self.QPushButton_Rotate_Left.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.QPushButton_Rotate_Left.sizePolicy().hasHeightForWidth())
        self.QPushButton_Rotate_Left.setSizePolicy(sizePolicy2)
        self.QPushButton_Rotate_Left.setMinimumSize(QSize(65, 55))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/rotate_left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Rotate_Left.setIcon(icon4)
        self.QPushButton_Rotate_Left.setIconSize(QSize(40, 40))

        self.gridLayout_12.addWidget(self.QPushButton_Rotate_Left, 2, 1, 1, 1)

        self.QLabel_Up = QLabel(self.QFrame_Advanced_Moves)
        self.QLabel_Up.setObjectName(u"QLabel_Up")
        self.QLabel_Up.setStyleSheet(u"QLabel#QLabel_Up{\n"
"	color:#EEEEEE;\n"
"}")
        self.QLabel_Up.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.QLabel_Up, 0, 3, 1, 1)

        self.QLabel_Down = QLabel(self.QFrame_Advanced_Moves)
        self.QLabel_Down.setObjectName(u"QLabel_Down")
        self.QLabel_Down.setStyleSheet(u"QLabel#QLabel_Down{\n"
"	color:#EEEEEE;\n"
"}")
        self.QLabel_Down.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.QLabel_Down, 4, 3, 1, 1)

        self.QLabel_CCW = QLabel(self.QFrame_Advanced_Moves)
        self.QLabel_CCW.setObjectName(u"QLabel_CCW")
        self.QLabel_CCW.setStyleSheet(u"QLabel#QLabel_CCW{\n"
"	color:#EEEEEE;\n"
"}")
        self.QLabel_CCW.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.QLabel_CCW, 2, 0, 1, 1)


        self.gridLayout_10.addWidget(self.QFrame_Advanced_Moves, 1, 0, 1, 1)

        self.QFrame_Basic_Moves = QFrame(self.QGroupBox_3)
        self.QFrame_Basic_Moves.setObjectName(u"QFrame_Basic_Moves")
        self.QFrame_Basic_Moves.setStyleSheet(u"QFrame#QFrame_Basic_Moves {\n"
"    border-radius: 64px;\n"
"	    border: 2px solid gray;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_Basic_Moves.setFrameShape(QFrame.StyledPanel)
        self.QFrame_Basic_Moves.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.QFrame_Basic_Moves)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.QLabel_Left = QLabel(self.QFrame_Basic_Moves)
        self.QLabel_Left.setObjectName(u"QLabel_Left")
        self.QLabel_Left.setStyleSheet(u"QLabel#QLabel_Left{\n"
"	color:#EEEEEE;\n"
"}")

        self.gridLayout_11.addWidget(self.QLabel_Left, 2, 0, 1, 1)

        self.QPushButton_Forward = QPushButton(self.QFrame_Basic_Moves)
        self.QPushButton_Forward.setObjectName(u"QPushButton_Forward")
        self.QPushButton_Forward.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.QPushButton_Forward.sizePolicy().hasHeightForWidth())
        self.QPushButton_Forward.setSizePolicy(sizePolicy2)
        self.QPushButton_Forward.setMinimumSize(QSize(65, 55))
        icon5 = QIcon()
        icon5.addFile(u":/images/images/forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Forward.setIcon(icon5)
        self.QPushButton_Forward.setIconSize(QSize(40, 40))

        self.gridLayout_11.addWidget(self.QPushButton_Forward, 1, 3, 1, 1)

        self.QPushButton_Left = QPushButton(self.QFrame_Basic_Moves)
        self.QPushButton_Left.setObjectName(u"QPushButton_Left")
        self.QPushButton_Left.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.QPushButton_Left.sizePolicy().hasHeightForWidth())
        self.QPushButton_Left.setSizePolicy(sizePolicy2)
        self.QPushButton_Left.setMinimumSize(QSize(65, 55))
        icon6 = QIcon()
        icon6.addFile(u":/images/images/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Left.setIcon(icon6)
        self.QPushButton_Left.setIconSize(QSize(40, 40))

        self.gridLayout_11.addWidget(self.QPushButton_Left, 2, 1, 1, 1)

        self.QPushButton_Right = QPushButton(self.QFrame_Basic_Moves)
        self.QPushButton_Right.setObjectName(u"QPushButton_Right")
        self.QPushButton_Right.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.QPushButton_Right.sizePolicy().hasHeightForWidth())
        self.QPushButton_Right.setSizePolicy(sizePolicy2)
        self.QPushButton_Right.setMinimumSize(QSize(65, 55))
        icon7 = QIcon()
        icon7.addFile(u":/images/images/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Right.setIcon(icon7)
        self.QPushButton_Right.setIconSize(QSize(40, 40))

        self.gridLayout_11.addWidget(self.QPushButton_Right, 2, 4, 1, 1)

        self.QPushButton_Backward = QPushButton(self.QFrame_Basic_Moves)
        self.QPushButton_Backward.setObjectName(u"QPushButton_Backward")
        self.QPushButton_Backward.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.QPushButton_Backward.sizePolicy().hasHeightForWidth())
        self.QPushButton_Backward.setSizePolicy(sizePolicy2)
        self.QPushButton_Backward.setMinimumSize(QSize(65, 55))
        icon8 = QIcon()
        icon8.addFile(u":/images/images/backward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QPushButton_Backward.setIcon(icon8)
        self.QPushButton_Backward.setIconSize(QSize(40, 40))

        self.gridLayout_11.addWidget(self.QPushButton_Backward, 3, 3, 1, 1)

        self.QLabel_Forward = QLabel(self.QFrame_Basic_Moves)
        self.QLabel_Forward.setObjectName(u"QLabel_Forward")
        self.QLabel_Forward.setStyleSheet(u"QLabel#QLabel_Forward{\n"
"	color:#EEEEEE;\n"
"}")
        self.QLabel_Forward.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.QLabel_Forward, 0, 3, 1, 1)

        self.QLabel_Right = QLabel(self.QFrame_Basic_Moves)
        self.QLabel_Right.setObjectName(u"QLabel_Right")
        self.QLabel_Right.setStyleSheet(u"QLabel#QLabel_Right{\n"
"	color:#EEEEEE;\n"
"}")

        self.gridLayout_11.addWidget(self.QLabel_Right, 2, 5, 1, 1)

        self.QPushButton_Dummy1 = QPushButton(self.QFrame_Basic_Moves)
        self.QPushButton_Dummy1.setObjectName(u"QPushButton_Dummy1")
        self.QPushButton_Dummy1.setEnabled(False)
        self.QPushButton_Dummy1.setMinimumSize(QSize(65, 45))
        self.QPushButton_Dummy1.setFlat(True)

        self.gridLayout_11.addWidget(self.QPushButton_Dummy1, 2, 3, 1, 1)

        self.QLabel_Backward = QLabel(self.QFrame_Basic_Moves)
        self.QLabel_Backward.setObjectName(u"QLabel_Backward")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.QLabel_Backward.sizePolicy().hasHeightForWidth())
        self.QLabel_Backward.setSizePolicy(sizePolicy3)
        self.QLabel_Backward.setMinimumSize(QSize(65, 0))
        self.QLabel_Backward.setStyleSheet(u"QLabel#QLabel_Backward{\n"
"	color:#EEEEEE;\n"
"}")
        self.QLabel_Backward.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.QLabel_Backward, 4, 3, 1, 1)


        self.gridLayout_10.addWidget(self.QFrame_Basic_Moves, 1, 2, 1, 1)

        self.QPushButton_Land = QPushButton(self.QGroupBox_3)
        self.QPushButton_Land.setObjectName(u"QPushButton_Land")
        self.QPushButton_Land.setEnabled(False)
        self.QPushButton_Land.setStyleSheet(u"QPushButton#QPushButton_Land{\n"
"	color:#EEEEEE;\n"
"}\n"
"\n"
"QPushButton::disabled#QPushButton_Land {\n"
"    color:  grey;\n"
"}")

        self.gridLayout_10.addWidget(self.QPushButton_Land, 2, 2, 1, 1)

        self.QPushButton_Take_Off = QPushButton(self.QGroupBox_3)
        self.QPushButton_Take_Off.setObjectName(u"QPushButton_Take_Off")
        self.QPushButton_Take_Off.setEnabled(False)
        self.QPushButton_Take_Off.setStyleSheet(u"QPushButton#QPushButton_Take_Off{\n"
"	color:#EEEEEE;\n"
"}\n"
"\n"
"QPushButton::disabled#QPushButton_Take_Off  {\n"
"    color:  grey;\n"
"}")

        self.gridLayout_10.addWidget(self.QPushButton_Take_Off, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.QGroupBox_3, 1, 0, 1, 1)

        self.QGroupBox_2 = QGroupBox(self.centralwidget)
        self.QGroupBox_2.setObjectName(u"QGroupBox_2")
        self.QGroupBox_2.setMinimumSize(QSize(620, 326))
        self.QGroupBox_2.setFont(font)
        self.QGroupBox_2.setStyleSheet(u"QGroupBox#QGroupBox_2 {\n"
"    background-color:  #222831;\n"
"    border: 3px solid gray;\n"
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
        self.gridLayout_25 = QGridLayout(self.QGroupBox_2)
        self.gridLayout_25.setSpacing(12)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(12, 12, 12, 12)
        self.QGroupBox_Absolute_Height = QGroupBox(self.QGroupBox_2)
        self.QGroupBox_Absolute_Height.setObjectName(u"QGroupBox_Absolute_Height")
        self.QGroupBox_Absolute_Height.setStyleSheet(u"QGroupBox#QGroupBox_Absolute_Height{\n"
"    background-color:  #222831;\n"
"    border: 2px solid gray;\n"
"	 border-color: #00ADB5;\n"
"    border-radius: 8px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_Absolute_Height {\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.gridLayout_24 = QGridLayout(self.QGroupBox_Absolute_Height)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(12, 12, 12, 12)
        self.QFrame_Absolute_Height = QFrame(self.QGroupBox_Absolute_Height)
        self.QFrame_Absolute_Height.setObjectName(u"QFrame_Absolute_Height")
        self.QFrame_Absolute_Height.setStyleSheet(u"QFrame#QFrame_Absolute_Height{\n"
"    border-radius: 8px;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_Absolute_Height.setFrameShape(QFrame.Panel)
        self.QFrame_Absolute_Height.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.QFrame_Absolute_Height)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.QLineEdit_Absolute_Height = QLineEdit(self.QFrame_Absolute_Height)
        self.QLineEdit_Absolute_Height.setObjectName(u"QLineEdit_Absolute_Height")
        self.QLineEdit_Absolute_Height.setEnabled(True)
        self.QLineEdit_Absolute_Height.setStyleSheet(u"QLineEdit#QLineEdit_Absolute_Height{\n"
"    border: 1px solid grey;\n"
"    border-radius: 4px;\n"
"	 color:#EEEEEE;\n"
"}")
        self.QLineEdit_Absolute_Height.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.QLineEdit_Absolute_Height.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.QLineEdit_Absolute_Height)

        self.QLabel_cm_b = QLabel(self.QFrame_Absolute_Height)
        self.QLabel_cm_b.setObjectName(u"QLabel_cm_b")
        font1 = QFont()
        font1.setPointSize(11)
        self.QLabel_cm_b.setFont(font1)
        self.QLabel_cm_b.setStyleSheet(u"QLabel#QLabel_cm_b{\n"
"	 color:#EEEEEE;\n"
"}")

        self.horizontalLayout_10.addWidget(self.QLabel_cm_b)


        self.gridLayout_24.addWidget(self.QFrame_Absolute_Height, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.QGroupBox_Absolute_Height, 0, 0, 1, 1)

        self.QGroupBox_Flight_Time = QGroupBox(self.QGroupBox_2)
        self.QGroupBox_Flight_Time.setObjectName(u"QGroupBox_Flight_Time")
        self.QGroupBox_Flight_Time.setStyleSheet(u"QGroupBox#QGroupBox_Flight_Time{\n"
"    background-color:  #222831;\n"
"    border: 2px solid gray;\n"
"	 border-color: #00ADB5;\n"
"    border-radius: 8px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_Flight_Time{\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.gridLayout_23 = QGridLayout(self.QGroupBox_Flight_Time)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(12, 12, 12, 12)
        self.QFrame_Flight_Time = QFrame(self.QGroupBox_Flight_Time)
        self.QFrame_Flight_Time.setObjectName(u"QFrame_Flight_Time")
        self.QFrame_Flight_Time.setStyleSheet(u"QFrame#QFrame_Flight_Time{\n"
"    border-radius: 8px;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_Flight_Time.setFrameShape(QFrame.Panel)
        self.QFrame_Flight_Time.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.QFrame_Flight_Time)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.QLineEdit_Flight_Time = QLineEdit(self.QFrame_Flight_Time)
        self.QLineEdit_Flight_Time.setObjectName(u"QLineEdit_Flight_Time")
        self.QLineEdit_Flight_Time.setEnabled(True)
        self.QLineEdit_Flight_Time.setStyleSheet(u"QLineEdit#QLineEdit_Flight_Time{\n"
"    border: 1px solid grey;\n"
"    border-radius: 4px;\n"
"	 color:#EEEEEE;\n"
"}")
        self.QLineEdit_Flight_Time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.QLineEdit_Flight_Time.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.QLineEdit_Flight_Time)

        self.QLabel_s = QLabel(self.QFrame_Flight_Time)
        self.QLabel_s.setObjectName(u"QLabel_s")
        self.QLabel_s.setFont(font1)
        self.QLabel_s.setStyleSheet(u"QLabel#QLabel_s{\n"
"	 color:#EEEEEE;\n"
"}")

        self.horizontalLayout_9.addWidget(self.QLabel_s)


        self.gridLayout_23.addWidget(self.QFrame_Flight_Time, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.QGroupBox_Flight_Time, 0, 1, 1, 1)

        self.QGroupBox_Temperature = QGroupBox(self.QGroupBox_2)
        self.QGroupBox_Temperature.setObjectName(u"QGroupBox_Temperature")
        self.QGroupBox_Temperature.setStyleSheet(u"QGroupBox#QGroupBox_Temperature{\n"
"    background-color:  #222831;\n"
"    border: 2px solid gray;\n"
"	 border-color: #00ADB5;\n"
"    border-radius: 8px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_Temperature {\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.gridLayout_22 = QGridLayout(self.QGroupBox_Temperature)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(12, 12, 12, 12)
        self.QFrame_Temperature = QFrame(self.QGroupBox_Temperature)
        self.QFrame_Temperature.setObjectName(u"QFrame_Temperature")
        self.QFrame_Temperature.setStyleSheet(u"QFrame#QFrame_Temperature{\n"
"    border-radius: 8px;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_Temperature.setFrameShape(QFrame.Panel)
        self.QFrame_Temperature.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.QFrame_Temperature)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.QLineEdit_Temperature = QLineEdit(self.QFrame_Temperature)
        self.QLineEdit_Temperature.setObjectName(u"QLineEdit_Temperature")
        self.QLineEdit_Temperature.setEnabled(True)
        self.QLineEdit_Temperature.setStyleSheet(u"QLineEdit#QLineEdit_Temperature{\n"
"    border: 1px solid grey;\n"
"    border-radius: 4px;\n"
"	 color:#EEEEEE;\n"
"}")
        self.QLineEdit_Temperature.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.QLineEdit_Temperature.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.QLineEdit_Temperature)

        self.QLabel_celcius = QLabel(self.QFrame_Temperature)
        self.QLabel_celcius.setObjectName(u"QLabel_celcius")
        self.QLabel_celcius.setFont(font1)
        self.QLabel_celcius.setStyleSheet(u"QLabel#QLabel_celcius{\n"
"	 color:#EEEEEE;\n"
"}")

        self.horizontalLayout_8.addWidget(self.QLabel_celcius)


        self.gridLayout_22.addWidget(self.QFrame_Temperature, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.QGroupBox_Temperature, 0, 2, 1, 1)

        self.QGroupBox_TOF = QGroupBox(self.QGroupBox_2)
        self.QGroupBox_TOF.setObjectName(u"QGroupBox_TOF")
        self.QGroupBox_TOF.setStyleSheet(u"QGroupBox#QGroupBox_TOF{\n"
"    background-color:  #222831;\n"
"    border: 2px solid gray;\n"
"	 border-color: #00ADB5;\n"
"    border-radius: 8px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_TOF {\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.gridLayout_21 = QGridLayout(self.QGroupBox_TOF)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(12, 12, 12, 12)
        self.QFrame_TOF = QFrame(self.QGroupBox_TOF)
        self.QFrame_TOF.setObjectName(u"QFrame_TOF")
        self.QFrame_TOF.setStyleSheet(u"QFrame#QFrame_TOF{\n"
"    border-radius: 8px;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_TOF.setFrameShape(QFrame.Panel)
        self.QFrame_TOF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.QFrame_TOF)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.QLineEdit_Distance = QLineEdit(self.QFrame_TOF)
        self.QLineEdit_Distance.setObjectName(u"QLineEdit_Distance")
        self.QLineEdit_Distance.setEnabled(True)
        self.QLineEdit_Distance.setStyleSheet(u"QLineEdit#QLineEdit_Distance{\n"
"    border: 1px solid grey;\n"
"    border-radius: 4px;\n"
"	 color:#EEEEEE;\n"
"}")
        self.QLineEdit_Distance.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.QLineEdit_Distance.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.QLineEdit_Distance)

        self.QLabel_cm = QLabel(self.QFrame_TOF)
        self.QLabel_cm.setObjectName(u"QLabel_cm")
        self.QLabel_cm.setStyleSheet(u"QLabel#QLabel_cm{\n"
"	 color:#EEEEEE;\n"
"}")

        self.horizontalLayout_7.addWidget(self.QLabel_cm)


        self.gridLayout_21.addWidget(self.QFrame_TOF, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.QGroupBox_TOF, 1, 0, 1, 1)

        self.QGroupBox_Camera_Source = QGroupBox(self.QGroupBox_2)
        self.QGroupBox_Camera_Source.setObjectName(u"QGroupBox_Camera_Source")
        self.QGroupBox_Camera_Source.setStyleSheet(u"QGroupBox#QGroupBox_Camera_Source{\n"
"	background-color:  #222831;  /* Ustaw kolor t\u0142a */\n"
"	border: 2px solid gray;\n"
"	border-color: #00ADB5;\n"
"	border-radius: 8px;\n"
"	margin-top: 1ex;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_Camera_Source  {\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	 left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.gridLayout_19 = QGridLayout(self.QGroupBox_Camera_Source)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(12, 12, 12, 12)
        self.QFrame_Camera_Source = QFrame(self.QGroupBox_Camera_Source)
        self.QFrame_Camera_Source.setObjectName(u"QFrame_Camera_Source")
        self.QFrame_Camera_Source.setStyleSheet(u"QFrame#QFrame_Camera_Source{\n"
"    border-radius: 8px;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_Camera_Source.setFrameShape(QFrame.Panel)
        self.QFrame_Camera_Source.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.QFrame_Camera_Source)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.QPushButton_Computer = QPushButton(self.QFrame_Camera_Source)
        self.QPushButton_Computer.setObjectName(u"QPushButton_Computer")
        self.QPushButton_Computer.setEnabled(False)
        self.QPushButton_Computer.setMinimumSize(QSize(0, 35))
        self.QPushButton_Computer.setFont(font1)
        self.QPushButton_Computer.setStyleSheet(u"QPushButton#QPushButton_Computer{\n"
"	color:#EEEEEE;\n"
"}\n"
"\n"
"QPushButton::disabled#QPushButton_Computer   {\n"
"    color:  grey;\n"
"}")

        self.horizontalLayout_6.addWidget(self.QPushButton_Computer)

        self.QPushButton_Tello = QPushButton(self.QFrame_Camera_Source)
        self.QPushButton_Tello.setObjectName(u"QPushButton_Tello")
        self.QPushButton_Tello.setEnabled(False)
        self.QPushButton_Tello.setMinimumSize(QSize(0, 35))
        self.QPushButton_Tello.setFont(font1)
        self.QPushButton_Tello.setStyleSheet(u"QPushButton#QPushButton_Tello{\n"
"	color:#EEEEEE;\n"
"}\n"
"\n"
"QPushButton::disabled#QPushButton_Tello  {\n"
"    color:  grey;\n"
"}")

        self.horizontalLayout_6.addWidget(self.QPushButton_Tello)


        self.gridLayout_20.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.QFrame_Camera_Source, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.QGroupBox_Camera_Source, 1, 1, 1, 1)

        self.QGroupBox_Hand_Mode = QGroupBox(self.QGroupBox_2)
        self.QGroupBox_Hand_Mode.setObjectName(u"QGroupBox_Hand_Mode")
        self.QGroupBox_Hand_Mode.setStyleSheet(u"QGroupBox#QGroupBox_Hand_Mode {\n"
"    background-color:  #222831;\n"
"    border: 2px solid gray;\n"
"	 border-color: #00ADB5;\n"
"    border-radius: 8px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QGroupBox::title#QGroupBox_Hand_Mode   {\n"
"    color:  white;\n"
"    subcontrol-origin: margin;\n"
"	left: 15px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.gridLayout_13 = QGridLayout(self.QGroupBox_Hand_Mode)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(12, 12, 12, 12)
        self.QFrame_Hand_Mode = QFrame(self.QGroupBox_Hand_Mode)
        self.QFrame_Hand_Mode.setObjectName(u"QFrame_Hand_Mode")
        self.QFrame_Hand_Mode.setStyleSheet(u"QFrame#QFrame_Hand_Mode {\n"
"    border-radius: 8px;\n"
"	background-color: #393E46;\n"
"}")
        self.QFrame_Hand_Mode.setFrameShape(QFrame.Panel)
        self.QFrame_Hand_Mode.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.QFrame_Hand_Mode)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.QPushButton_Left_Hand = QPushButton(self.QFrame_Hand_Mode)
        self.QPushButton_Left_Hand.setObjectName(u"QPushButton_Left_Hand")
        self.QPushButton_Left_Hand.setEnabled(True)
        self.QPushButton_Left_Hand.setMinimumSize(QSize(0, 35))
        self.QPushButton_Left_Hand.setFont(font1)
        self.QPushButton_Left_Hand.setStyleSheet(u"QPushButton#QPushButton_Left_Hand{\n"
"	color:#EEEEEE;\n"
"}\n"
"\n"
"QPushButton::disabled#QPushButton_Left_Hand   {\n"
"    color:  grey;\n"
"}")

        self.horizontalLayout_5.addWidget(self.QPushButton_Left_Hand)

        self.QPushButton_Right_Hand = QPushButton(self.QFrame_Hand_Mode)
        self.QPushButton_Right_Hand.setObjectName(u"QPushButton_Right_Hand")
        self.QPushButton_Right_Hand.setEnabled(False)
        self.QPushButton_Right_Hand.setMinimumSize(QSize(0, 35))
        self.QPushButton_Right_Hand.setFont(font1)
        self.QPushButton_Right_Hand.setStyleSheet(u"QPushButton#QPushButton_Right_Hand{\n"
"	color:#EEEEEE;\n"
"}\n"
"\n"
"QPushButton::disabled#QPushButton_Right_Hand   {\n"
"    color:  grey;\n"
"}")

        self.horizontalLayout_5.addWidget(self.QPushButton_Right_Hand)


        self.gridLayout_14.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.QFrame_Hand_Mode, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.QGroupBox_Hand_Mode, 1, 2, 1, 1)

        self.QGroupBox_Drone_Battery = QGroupBox(self.QGroupBox_2)
        self.QGroupBox_Drone_Battery.setObjectName(u"QGroupBox_Drone_Battery")
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.QProgressBar_Battery.sizePolicy().hasHeightForWidth())
        self.QProgressBar_Battery.setSizePolicy(sizePolicy4)
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


        self.gridLayout_25.addWidget(self.QGroupBox_Drone_Battery, 2, 0, 1, 1)

        self.QGroupBox_Drone_Connection = QGroupBox(self.QGroupBox_2)
        self.QGroupBox_Drone_Connection.setObjectName(u"QGroupBox_Drone_Connection")
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


        self.gridLayout_25.addWidget(self.QGroupBox_Drone_Connection, 2, 1, 1, 1)

        self.QGroupBox_Data_Collector = QGroupBox(self.QGroupBox_2)
        self.QGroupBox_Data_Collector.setObjectName(u"QGroupBox_Data_Collector")
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
        self.QPushButton_Save_Gesture.setFont(font1)
        self.QPushButton_Save_Gesture.setStyleSheet(u"QPushButton#QPushButton_Save_Gesture {\n"
"	color:#EEEEEE;\n"
"}\n"
"\n"
"QPushButton::disabled#QPushButton_Save_Gesture   {\n"
"    color:  grey;\n"
"}")

        self.horizontalLayout.addWidget(self.QPushButton_Save_Gesture)

        self.QSpinBox_Gesture_Label = QSpinBox(self.QFrame_Data_Collector)
        self.QSpinBox_Gesture_Label.setObjectName(u"QSpinBox_Gesture_Label")
        self.QSpinBox_Gesture_Label.setStyleSheet(u"QSpinBox#QSpinBox_Gesture_Label {\n"
"	color:#EEEEEE;\n"
"}\n"
"\n"
"QSpinBox::disabled#QSpinBox_Gesture_Label   {\n"
"    color:  grey;\n"
"}")
        self.QSpinBox_Gesture_Label.setMaximum(9)

        self.horizontalLayout.addWidget(self.QSpinBox_Gesture_Label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.QPushButton_Clear_All_Gestures = QPushButton(self.QFrame_Data_Collector)
        self.QPushButton_Clear_All_Gestures.setObjectName(u"QPushButton_Clear_All_Gestures")
        self.QPushButton_Clear_All_Gestures.setFont(font1)
        self.QPushButton_Clear_All_Gestures.setStyleSheet(u"QPushButton#QPushButton_Clear_All_Gestures{\n"
"	color:#EEEEEE;\n"
"}\n"
"\n"
"QPushButton::disabled#QPushButton_Clear_All_Gestures  {\n"
"    color:  grey;\n"
"}")

        self.verticalLayout.addWidget(self.QPushButton_Clear_All_Gestures)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.QFrame_Data_Collector, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.QGroupBox_Data_Collector, 2, 2, 1, 1)


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
        self.QGroupBox_Camera_Feed.setTitle(QCoreApplication.translate("MainWindow", u"Camera Feed", None))
        self.QLabel_Camera_Feed.setText("")
        self.QGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.QPushButton_Down.setText("")
#if QT_CONFIG(shortcut)
        self.QPushButton_Down.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.QLabel_CW.setText(QCoreApplication.translate("MainWindow", u"CW", None))
        self.QPushButton_Dummy2.setText("")
        self.QPushButton_Rotate_Right.setText("")
#if QT_CONFIG(shortcut)
        self.QPushButton_Rotate_Right.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.QPushButton_Up.setText("")
#if QT_CONFIG(shortcut)
        self.QPushButton_Up.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.QPushButton_Rotate_Left.setText("")
#if QT_CONFIG(shortcut)
        self.QPushButton_Rotate_Left.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.QLabel_Up.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.QLabel_Down.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.QLabel_CCW.setText(QCoreApplication.translate("MainWindow", u"CCW", None))
        self.QLabel_Left.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.QPushButton_Forward.setText("")
#if QT_CONFIG(shortcut)
        self.QPushButton_Forward.setShortcut(QCoreApplication.translate("MainWindow", u"Up", None))
#endif // QT_CONFIG(shortcut)
        self.QPushButton_Left.setText("")
#if QT_CONFIG(shortcut)
        self.QPushButton_Left.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.QPushButton_Right.setText("")
#if QT_CONFIG(shortcut)
        self.QPushButton_Right.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.QPushButton_Backward.setText("")
#if QT_CONFIG(shortcut)
        self.QPushButton_Backward.setShortcut(QCoreApplication.translate("MainWindow", u"Down", None))
#endif // QT_CONFIG(shortcut)
        self.QLabel_Forward.setText(QCoreApplication.translate("MainWindow", u"Forward", None))
        self.QLabel_Right.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.QPushButton_Dummy1.setText("")
        self.QLabel_Backward.setText(QCoreApplication.translate("MainWindow", u"Backward", None))
        self.QPushButton_Land.setText(QCoreApplication.translate("MainWindow", u"Land", None))
        self.QPushButton_Take_Off.setText(QCoreApplication.translate("MainWindow", u"Take Off", None))
        self.QGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Utilities and settings", None))
        self.QGroupBox_Absolute_Height.setTitle(QCoreApplication.translate("MainWindow", u"Absolute Height", None))
        self.QLineEdit_Absolute_Height.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.QLabel_cm_b.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.QGroupBox_Flight_Time.setTitle(QCoreApplication.translate("MainWindow", u"Flight Time", None))
        self.QLineEdit_Flight_Time.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.QLabel_s.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.QGroupBox_Temperature.setTitle(QCoreApplication.translate("MainWindow", u"Drone Temperature", None))
        self.QLineEdit_Temperature.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.QLabel_celcius.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.QGroupBox_TOF.setTitle(QCoreApplication.translate("MainWindow", u"TOF Distance", None))
        self.QLineEdit_Distance.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.QLabel_cm.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.QGroupBox_Camera_Source.setTitle(QCoreApplication.translate("MainWindow", u"Camera source", None))
        self.QPushButton_Computer.setText(QCoreApplication.translate("MainWindow", u"PC", None))
        self.QPushButton_Tello.setText(QCoreApplication.translate("MainWindow", u"Drone", None))
        self.QGroupBox_Hand_Mode.setTitle(QCoreApplication.translate("MainWindow", u"Hand Mode", None))
        self.QPushButton_Left_Hand.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.QPushButton_Right_Hand.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.QGroupBox_Drone_Battery.setTitle(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.QGroupBox_Drone_Connection.setTitle(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.QPushButton_Connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.QLabel_WiFI.setText("")
        self.QGroupBox_Data_Collector.setTitle(QCoreApplication.translate("MainWindow", u"Data Collector", None))
        self.QPushButton_Save_Gesture.setText(QCoreApplication.translate("MainWindow", u"Save gesture", None))
        self.QPushButton_Clear_All_Gestures.setText(QCoreApplication.translate("MainWindow", u"Clear all gestures", None))
    # retranslateUi

