# This Python file uses the following encoding: utf-8
import sys
import os

import time

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from PySide6.QtWidgets import QApplication, QMainWindow

from ui import Ui_MainWindow
from data_collector import DataCollector, cv2
from wifi import WiFi
from wifi.wifi import DRONE_WIFI_NETWORK_NAME


class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        self.data_collector = DataCollector()  # Construct Data Collector instance
        self.data_collector.configure_MediaPipe_Hands(False, 1, 0.8, 0.6)  # Configure MediaPipe model
        self.wifi = WiFi()
        self.gesture_label = "0"  # Variable for gesture label
        self.wifi_signal_image = None

        self.CameraThread = CameraThread()  # Construct Camera Thread instance
        self.CameraThread.start()  # Start Camera Thread
        self.CameraThread.image_update_signal.connect(self.image_update_slot)
        self.CameraThread.landmarks_update_signal.connect(self.landmarks_update_slot)

        self.WiFiThread = WiFiThread()
        self.WiFiThread.wifi_strength_update_signal.connect(self.wifi_strength_update_slot)

        self.ui.QPushButton_Save_Gesture.clicked.connect(self.save_gesture)
        self.ui.QPushButton_Clear_All_Gestures.clicked.connect(self.clear_all_gestures)
        self.ui.QSpinBox_Gesture_Label.valueChanged.connect(self.set_gesture_label)
        self.ui.QPushButton_Connect.clicked.connect(self.connect_to_the_drone)

    def closeEvent(self, event):
        self.CameraThread.stop_thread()
        self.CameraThread.wait(500)
        self.WiFiThread.stop_thread()
        self.WiFiThread.wait(500)
        if self.CameraThread.isFinished():
            event.accept()

    def image_update_slot(self, image):
        self.ui.QLabel_Camera_Feed.setPixmap(QPixmap.fromImage(image))

    def landmarks_update_slot(self, landmarks_list):
        self.data_collector.multi_hand_landmarks = landmarks_list

    def wifi_strength_update_slot(self, strength):
        if strength == 0:
            self.ui.QLabel_WiFI.setPixmap(QPixmap(u":/images/images/wifi_0.png"))
            self.WiFiThread.stop_thread()
            self.WiFiThread.wait(500)
            self.wifi.is_there_active_connection = False
        elif strength <= 25:
            self.ui.QLabel_WiFI.setPixmap(QPixmap(u":/images/images/wifi_1.png"))
        elif strength <= 50:
            self.ui.QLabel_WiFI.setPixmap(QPixmap(u":/images/images/wifi_2.png"))
        elif strength <= 75:
            self.ui.QLabel_WiFI.setPixmap(QPixmap(u":/images/images/wifi_3.png"))
        else:
            self.ui.QLabel_WiFI.setPixmap(QPixmap(u":/images/images/wifi_4.png"))

    def add_message_to_the_logs(self, message):
        current_time = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.ui.QTextBrowser_Logs.append("[ " + current_time + " ]" + " :  " + message)

    def set_gesture_label(self):
        self.gesture_label = str(self.ui.QSpinBox_Gesture_Label.value())

    def save_gesture(self):

        if len(self.data_collector.multi_hand_landmarks):
            self.data_collector.convert_coordinates()
            self.data_collector.maximum_absolute_scaling()
            self.data_collector.min_max_scaling()
            self.data_collector.standardization()
            self.data_collector.robust_scaling()
            self.data_collector.append_labels(int(self.gesture_label))
            self.data_collector.save_data(
                'data_collector/data/01_data_raw.csv',
                'data_collector/data/02_data_max_abs.csv',
                'data_collector/data/03_data_min_max.csv',
                'data_collector/data/04_data_standardized.csv',
                'data_collector/data/05_data_robust.csv')
            self.add_message_to_the_logs(
                "<font color=\"GreenYellow\">Gesture with label <font color=\"Plum\">"
                + self.gesture_label
                + "<font color=\"GreenYellow\"> has been successfully saved.")
        else:
            self.add_message_to_the_logs("<font color=\"OrangeRed\">No gesture has been detected in the camera image.")

    def clear_all_gestures(self):

        if os.stat('data_collector/data/01_data_raw.csv').st_size == 0:
            self.add_message_to_the_logs("<font color=\"Gold\">Gesture files are already empty, no need to clear.")
        else:
            self.data_collector.clear_data('data_collector/data/01_data_raw.csv')
            self.data_collector.clear_data('data_collector/data/02_data_max_abs.csv')
            self.data_collector.clear_data('data_collector/data/03_data_min_max.csv')
            self.data_collector.clear_data('data_collector/data/04_data_standardized.csv')
            self.data_collector.clear_data('data_collector/data/05_data_robust.csv')
            self.add_message_to_the_logs("<font color=\"GreenYellow\">All gesture files have been cleared.")

    def connect_to_the_drone(self):
        self.wifi.find_available_networks()
        if self.wifi.is_wifi_available(DRONE_WIFI_NETWORK_NAME) and not self.wifi.is_there_active_connection:
            self.wifi.connect_to(DRONE_WIFI_NETWORK_NAME, '')
            self.add_message_to_the_logs("<font color=\"GreenYellow\">Successfully connected to the drone.")
            self.WiFiThread.start()
            self.wifi.is_there_active_connection = True
            self.CameraThread.start()
        elif self.wifi.is_there_active_connection:
            self.add_message_to_the_logs("<font color=\"Gold\">You are already connected to the drone.")
        else:
            self.add_message_to_the_logs(
                "<font color=\"OrangeRed\">Drone WiFi is not available. Make sure the drone is powered on.")


class CameraThread(QThread):
    image_update_signal = Signal(QImage)
    landmarks_update_signal = Signal(list)

    def run(self):
        data_collector = DataCollector()  # Construct Data Collector instance
        data_collector.configure_camera()  # Configure Data Collector's camera
        data_collector.configure_MediaPipe_Hands(False, 1, 0.8, 0.6)  # Configure MediaPipe model
        self.ThreadActive = True

        while self.ThreadActive:
            data_collector.detect()
            self.image_update_signal.emit(data_collector.image)
            self.landmarks_update_signal.emit(data_collector.multi_hand_landmarks)
            data_collector.multi_hand_landmarks = None  # Clear hand landmarks
        data_collector.free_camera()  # Free data_collector's resources

    def stop_thread(self):
        self.ThreadActive = False
        self.quit()


class WiFiThread(QThread):
    wifi_strength_update_signal = Signal(int)

    def run(self):
        wifi = WiFi()
        self.ThreadActive = True
        while self.ThreadActive:
            if wifi.current_connection() == DRONE_WIFI_NETWORK_NAME:
                self.wifi_strength_update_signal.emit(wifi.check_signal_strength())
            else:
                self.wifi_strength_update_signal.emit(0)

    def stop_thread(self):
        self.ThreadActive = False
        self.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
