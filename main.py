## This Python file uses the following encoding: utf-8

# MIT License
#
# Copyright (c) 2018 DAMIÀ FUENTES ESCOTÉ
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys
import os

from PySide6.QtGui import *
from PySide6.QtCore import *

from PySide6.QtWidgets import QApplication, QMainWindow

from ui import Ui_MainWindow
from hand_detector import HandDetector
from wifi import WiFi
from wifi.wifi import DRONE_WIFI_NETWORK_NAME
from djitellopy import Tello
import time

CAMERA_SOURCE = 0  # 0 - PC, 1 - DRONE

FORWARD = "FORWARD"
BACKWARD = "BACKWARD"
RIGHT = "RIGHT"
LEFT = "LEFT"

TAKE_OFF = "TAKE_OFF"
LAND = "LAND"

UP = "UP"
DOWN = "DOWN"
ROTATE_RIGHT = "ROTATE_RIGHT"
ROTATE_LEFT = "ROTATE_LEFT"


class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.has_streamon_called = False

        self.tello_drone = Tello()

        self.hand_detector = HandDetector()  # Construct Data Collector instance
        self.hand_detector.configure_MediaPipe_Hands(False, 1, 0.8, 0.6)  # Configure MediaPipe model
        self.wifi = WiFi()
        self.gesture_label = "0"  # Variable for gesture label
        self.wifi_signal_image = None

        # Camera Thread
        self.CameraThread = CameraThread(self.tello_drone)  # Construct Camera Thread instance
        self.CameraThread.start()  # Start Camera Thread
        self.CameraThread.image_update_signal.connect(self.image_update_slot)
        self.CameraThread.landmarks_update_signal.connect(self.landmarks_update_slot)
        self.CameraThread.message_update_signal.connect(self.add_message_to_the_logs)
        self.CameraThread.gesture_update_signal.connect(self.send_gestures_to_the_drone_control_slot)

        # Wi-Fi Thread
        self.WiFiThread = WiFiThread(self.wifi, self.tello_drone)
        self.WiFiThread.wifi_strength_update_signal.connect(self.wifi_strength_update_slot)
        self.WiFiThread.battery_percentage_update_signal.connect(self.battery_percentage_update_slot)
        self.WiFiThread.tof_distance_update_signal.connect(self.tof_distance_update_slot)
        self.WiFiThread.temperature_update_signal.connect(self.temperature_update_slot)
        self.WiFiThread.absolute_height_update_signal.connect(self.absolute_height_update_slot)
        self.WiFiThread.flight_time_update_signal.connect(self.flight_time_update_slot)
        self.WiFiThread.message_update_signal.connect(self.add_message_to_the_logs)
        self.WiFiThread.ui_update_signal.connect(self.ui_update_slot)

        # Worker
        self.DroneControlThread = DroneControlThread(self.tello_drone)

        # Buttons actions
        self.ui.QPushButton_Save_Gesture.clicked.connect(self.save_gesture)
        self.ui.QPushButton_Clear_All_Gestures.clicked.connect(self.clear_all_gestures)
        self.ui.QSpinBox_Gesture_Label.valueChanged.connect(self.set_gesture_label)
        self.ui.QPushButton_Connect.clicked.connect(self.connect_to_the_drone)

        self.ui.QPushButton_Forward.pressed.connect(self.move_forward_pressed)
        self.ui.QPushButton_Forward.released.connect(self.move_forward_released)

        self.ui.QPushButton_Backward.pressed.connect(self.move_backward_pressed)
        self.ui.QPushButton_Backward.released.connect(self.move_backward_released)

        self.ui.QPushButton_Right.pressed.connect(self.move_right_pressed)
        self.ui.QPushButton_Right.released.connect(self.move_right_released)

        self.ui.QPushButton_Left.pressed.connect(self.move_left_pressed)
        self.ui.QPushButton_Left.released.connect(self.move_left_released)

        self.ui.QPushButton_Take_Off.pressed.connect(self.take_off_pressed)
        self.ui.QPushButton_Take_Off.released.connect(self.take_off_released)

        self.ui.QPushButton_Land.pressed.connect(self.land_pressed)
        self.ui.QPushButton_Land.released.connect(self.land_released)

        self.ui.QPushButton_Up.pressed.connect(self.move_up_pressed)
        self.ui.QPushButton_Up.released.connect(self.move_up_released)

        self.ui.QPushButton_Down.pressed.connect(self.move_down_pressed)
        self.ui.QPushButton_Down.released.connect(self.move_down_released)

        self.ui.QPushButton_Rotate_Right.pressed.connect(self.move_rotate_right_pressed)
        self.ui.QPushButton_Rotate_Right.released.connect(self.move_rotate_right_released)

        self.ui.QPushButton_Rotate_Left.pressed.connect(self.move_rotate_left_pressed)
        self.ui.QPushButton_Rotate_Left.released.connect(self.move_rotate_left_released)

        self.ui.QPushButton_Right_Hand.clicked.connect(self.change_to_right_hand_mode)
        self.ui.QPushButton_Left_Hand.clicked.connect(self.change_to_left_hand_mode)

        self.ui.QPushButton_Computer.clicked.connect(self.change_to_pc_source)
        self.ui.QPushButton_Tello.clicked.connect(self.change_to_tello_source)

    def closeEvent(self, event):
        """
        It is called when the application is closed.
        """

        self.CameraThread.stop_thread()
        self.CameraThread.wait(500)
        self.WiFiThread.stop_thread()
        self.WiFiThread.wait(500)
        self.DroneControlThread.stop_thread()
        self.DroneControlThread.wait(500)

        if self.has_streamon_called:
            self.tello_drone.streamoff()

        if self.CameraThread.isFinished() and self.WiFiThread.isFinished() and self.DroneControlThread.isFinished():
            event.accept()

    def image_update_slot(self, image):
        """
        Updates the displayed image from the camera.

        :param image: camera image
        """

        self.ui.QLabel_Camera_Feed.setPixmap(QPixmap.fromImage(image))

    def landmarks_update_slot(self, landmarks_list: list):
        """
        Updates hand landmarks.

        :param landmarks_list: hand landmarks
        """

        self.hand_detector.multi_hand_landmarks = landmarks_list

    def wifi_strength_update_slot(self, strength: int):
        """
        Updates the signal strength of the Wi-Fi network.

        :param strength: signal strength
        """

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

    def battery_percentage_update_slot(self, battery_percentage: int):
        """
        Updates drone's battery percentage.

        :param battery_percentage: battery percentage
        """

        self.ui.QProgressBar_Battery.setValue(battery_percentage)
        if battery_percentage <= 20:
            self.ui.QProgressBar_Battery.setStyleSheet(u"QProgressBar#QProgressBar_Battery {\n"
                                                       "    border: 2px solid grey;\n"
                                                       "    border-radius: 5px;\n"
                                                       "	 color:#EEEEEE;\n"
                                                       "}\n"
                                                       "\n"
                                                       "QProgressBar::chunk#QProgressBar_Battery  {\n"
                                                       "    background-color: #ff9933;\n"
                                                       "    width: 20px;\n"
                                                       "}\n"
                                                       "")
        else:
            self.ui.QProgressBar_Battery.setStyleSheet(u"QProgressBar#QProgressBar_Battery {\n"
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

    def tof_distance_update_slot(self, distance: int):
        """
        Updates drone's tof distance.

        :param distance: distance
        """

        self.ui.QLineEdit_Distance.setText(str(distance))

    def temperature_update_slot(self, temperature: float):
        """
        Updates drone's temperature.

        :param temperature: temperature
        """

        self.ui.QLineEdit_Temperature.setText(str(temperature))

    def absolute_height_update_slot(self, absolute_height):
        """
        Updates drone's absolute height.

        :param absolute_height: absolute_height
        """

        self.ui.QLineEdit_Absolute_Height.setText(str(absolute_height))

    def flight_time_update_slot(self, flight_time):
        """
        Updates drone's flight time.

        :param flight_time: flight_time
        """

        self.ui.QLineEdit_Flight_Time.setText(str(flight_time))

    def ui_update_slot(self):
        """
        Enables control buttons.
        """

        self.ui.QPushButton_Forward.setEnabled(True)
        self.ui.QPushButton_Backward.setEnabled(True)
        self.ui.QPushButton_Right.setEnabled(True)
        self.ui.QPushButton_Left.setEnabled(True)
        self.ui.QPushButton_Take_Off.setEnabled(True)
        self.ui.QPushButton_Up.setEnabled(True)
        self.ui.QPushButton_Down.setEnabled(True)
        self.ui.QPushButton_Rotate_Right.setEnabled(True)
        self.ui.QPushButton_Rotate_Left.setEnabled(True)
        self.ui.QPushButton_Tello.setEnabled(True)
        self.ui.QFrame_Basic_Moves.setStyleSheet(u"QFrame#QFrame_Basic_Moves {\n"
                                                 "    border-radius: 64px;\n"
                                                 "	    border: 2px solid green;\n"
                                                 "	background-color: #393E46;\n"
                                                 "}")
        self.ui.QFrame_Advanced_Moves.setStyleSheet(u"QFrame#QFrame_Advanced_Moves {\n"
                                                    "    border-radius: 64px;\n"
                                                    "	border: 2px solid green;\n"
                                                    "	background-color: #393E46;\n"
                                                    "}")

    def send_gestures_to_the_drone_control_slot(self, move):
        self.DroneControlThread.firstWork(move)

    def add_message_to_the_logs(self, message):
        """
        Adds a message to the logs

        :param message: message to add
        """

        current_time = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.ui.QTextBrowser_Logs.append("[ " + current_time + " ]" + " :  " + message)

    def set_gesture_label(self):
        """
        Sets the label of the gesture.
        """

        self.gesture_label = str(self.ui.QSpinBox_Gesture_Label.value())

    def save_gesture(self):
        """
        Saves the gesture.
        """

        if len(self.hand_detector.multi_hand_landmarks):
            self.hand_detector.convert_coordinates()
            self.hand_detector.maximum_absolute_scaling()
            self.hand_detector.min_max_scaling()
            self.hand_detector.standardization()
            self.hand_detector.robust_scaling()
            self.hand_detector.append_labels(int(self.gesture_label))
            self.hand_detector.save_data(
                'hand_detector/data/01_data_raw.csv',
                'hand_detector/data/02_data_max_abs.csv',
                'hand_detector/data/03_data_min_max.csv',
                'hand_detector/data/04_data_standardized.csv',
                'hand_detector/data/05_data_robust.csv')
            self.add_message_to_the_logs(
                "<font color=\"GreenYellow\">Gesture with label <font color=\"Plum\">"
                + self.gesture_label
                + "<font color=\"GreenYellow\"> has been successfully saved.")
        else:
            self.add_message_to_the_logs("<font color=\"OrangeRed\">No gesture has been detected in the camera image.")

    def clear_all_gestures(self):
        """
        Clears all gesture files.
        """

        if os.stat('hand_detector/data/01_data_raw.csv').st_size == 0:
            self.add_message_to_the_logs("<font color=\"Gold\">Gesture files are already empty, no need to clear.")
        else:
            self.hand_detector.clear_data('hand_detector/data/01_data_raw.csv')
            self.hand_detector.clear_data('hand_detector/data/02_data_max_abs.csv')
            self.hand_detector.clear_data('hand_detector/data/03_data_min_max.csv')
            self.hand_detector.clear_data('hand_detector/data/04_data_standardized.csv')
            self.hand_detector.clear_data('hand_detector/data/05_data_robust.csv')
            self.add_message_to_the_logs("<font color=\"GreenYellow\">All gesture files have been cleared.")

    def connect_to_the_drone(self):
        """
        Connects to the drone.
        """

        self.add_message_to_the_logs("<font color=\"Gold\">Attempting to connect to the drone.")

        if self.wifi.is_there_active_connection:
            self.add_message_to_the_logs("<font color=\"Gold\">You are already connected to the drone.")
        else:
            self.WiFiThread.start()
            self.DroneControlThread.start()

    def move_forward_pressed(self):
        self.ui.QPushButton_Forward.setIcon(QIcon(u":/images/images/forward_clicked.png"))
        self.DroneControlThread.firstWork(FORWARD)

    def move_forward_released(self):
        self.ui.QPushButton_Forward.setIcon(QIcon(u":/images/images/forward.png"))
        self.DroneControlThread.firstWork(" ")

    def move_backward_pressed(self):
        self.ui.QPushButton_Backward.setIcon(QIcon(u":/images/images/backward_clicked.png"))
        self.DroneControlThread.firstWork(BACKWARD)

    def move_backward_released(self):
        self.ui.QPushButton_Backward.setIcon(QIcon(u":/images/images/backward.png"))
        self.DroneControlThread.firstWork(" ")

    def move_right_pressed(self):
        self.ui.QPushButton_Right.setIcon(QIcon(u":/images/images/right_clicked.png"))
        self.DroneControlThread.firstWork(RIGHT)

    def move_right_released(self):
        self.ui.QPushButton_Right.setIcon(QIcon(u":/images/images/right.png"))
        self.DroneControlThread.firstWork(" ")

    def move_left_pressed(self):
        self.ui.QPushButton_Left.setIcon(QIcon(u":/images/images/left_clicked.png"))
        self.DroneControlThread.firstWork(LEFT)

    def move_left_released(self):
        self.ui.QPushButton_Left.setIcon(QIcon(u":/images/images/left.png"))
        self.DroneControlThread.firstWork(" ")

    def take_off_pressed(self):
        if self.ui.QProgressBar_Battery.value() < 20:
            self.add_message_to_the_logs("<font color=\"OrangeRed\">Unable to take off, battery below 20%.")
        else:
            self.DroneControlThread.firstWork(TAKE_OFF)


    def take_off_released(self):
        self.DroneControlThread.firstWork("")
        if self.ui.QProgressBar_Battery.value() >= 20:
            self.ui.QPushButton_Take_Off.setEnabled(False)
            self.ui.QPushButton_Land.setEnabled(True)

    def land_pressed(self):
        self.DroneControlThread.firstWork(LAND)

    def land_released(self):
        self.DroneControlThread.firstWork("")
        self.ui.QPushButton_Take_Off.setEnabled(True)
        self.ui.QPushButton_Land.setEnabled(False)

    def move_up_pressed(self):
        self.ui.QPushButton_Up.setIcon(QIcon(u":/images/images/up_clicked.png"))
        self.DroneControlThread.firstWork(UP)

    def move_up_released(self):
        self.ui.QPushButton_Up.setIcon(QIcon(u":/images/images/up.png"))
        self.DroneControlThread.firstWork(" ")

    def move_down_pressed(self):
        self.ui.QPushButton_Down.setIcon(QIcon(u":/images/images/down_clicked.png"))
        self.DroneControlThread.firstWork(DOWN)

    def move_down_released(self):
        self.ui.QPushButton_Down.setIcon(QIcon(u":/images/images/down.png"))
        self.DroneControlThread.firstWork(" ")

    def move_rotate_right_pressed(self):
        self.ui.QPushButton_Rotate_Right.setIcon(QIcon(u":/images/images/rotate_right_clicked.png"))
        self.DroneControlThread.firstWork(ROTATE_RIGHT)

    def move_rotate_right_released(self):
        self.ui.QPushButton_Rotate_Right.setIcon(QIcon(u":/images/images/rotate_right.png"))
        self.DroneControlThread.firstWork(" ")

    def move_rotate_left_pressed(self):
        self.ui.QPushButton_Rotate_Left.setIcon(QIcon(u":/images/images/rotate_left_clicked.png"))
        self.DroneControlThread.firstWork(ROTATE_LEFT)

    def move_rotate_left_released(self):
        self.ui.QPushButton_Rotate_Left.setIcon(QIcon(u":/images/images/rotate_left.png"))
        self.DroneControlThread.firstWork(" ")

    def change_to_right_hand_mode(self):
        self.ui.QPushButton_Right_Hand.setEnabled(False)
        self.ui.QPushButton_Left_Hand.setEnabled(True)
        self.CameraThread.firstWork(True)

    def change_to_left_hand_mode(self):
        self.ui.QPushButton_Right_Hand.setEnabled(True)
        self.ui.QPushButton_Left_Hand.setEnabled(False)
        self.CameraThread.firstWork(False)

    def change_to_pc_source(self):
        self.CameraThread.stop_thread()
        self.CameraThread.wait(125)
        global CAMERA_SOURCE
        CAMERA_SOURCE = 0
        self.has_streamon_called = False
        self.tello_drone.streamoff()
        self.CameraThread.start()
        self.ui.QPushButton_Computer.setEnabled(False)
        self.ui.QPushButton_Tello.setEnabled(True)
        self.ui.QPushButton_Clear_All_Gestures.setEnabled(True)
        self.ui.QPushButton_Save_Gesture.setEnabled(True)
        self.ui.QSpinBox_Gesture_Label.setEnabled(True)

    def change_to_tello_source(self):
        self.CameraThread.stop_thread()
        self.CameraThread.wait(125)
        global CAMERA_SOURCE
        CAMERA_SOURCE = 1
        self.has_streamon_called = True
        self.CameraThread.start()
        self.ui.QPushButton_Computer.setEnabled(True)
        self.ui.QPushButton_Tello.setEnabled(False)
        self.ui.QPushButton_Clear_All_Gestures.setEnabled(False)
        self.ui.QPushButton_Save_Gesture.setEnabled(False)
        self.ui.QSpinBox_Gesture_Label.setEnabled(False)


class CameraThread(QThread):
    image_update_signal = Signal(QImage)
    landmarks_update_signal = Signal(list)
    message_update_signal = Signal(str)
    gesture_update_signal = Signal(str)

    def __init__(self, drone_instance, parent=None):
        super().__init__(parent)
        self.fingers = None
        self.ThreadActive = None
        self.tello_drone = drone_instance
        self.hand_mode = True

    def run(self):
        hand_detector = HandDetector()  # Construct Data Collector instance
        hand_detector.configure_camera()  # Configure Data Collector's camera
        hand_detector.configure_MediaPipe_Hands(False, 1, 0.8, 0.6)  # Configure MediaPipe model
        self.ThreadActive = True
        if CAMERA_SOURCE:
            self.tello_drone.streamon()
        while self.ThreadActive:
            hand_detector.detect(self.hand_mode, self.tello_drone, CAMERA_SOURCE)
            self.image_update_signal.emit(hand_detector.image)
            self.landmarks_update_signal.emit(hand_detector.multi_hand_landmarks)
            self.fingers = [0, 0, 0, 0, 0]
            if hand_detector.multi_hand_landmarks is not None:
                self.fingers = hand_detector.find_fingers()
                if self.fingers == [1, 1, 1, 1, 1]:
                    self.gesture_update_signal.emit(" ")
                elif self.fingers == [0, 1, 0, 0, 0]:
                    self.gesture_update_signal.emit(UP)
                elif self.fingers == [0, 1, 1, 0, 0]:
                    self.gesture_update_signal.emit(DOWN)
                elif self.fingers == [1, 0, 0, 0, 0]:
                    if self.hand_mode:
                        self.gesture_update_signal.emit(LEFT)
                    else:
                        self.gesture_update_signal.emit(RIGHT)
                elif self.fingers == [0, 0, 0, 0, 1]:
                    if self.hand_mode:
                        self.gesture_update_signal.emit(RIGHT)
                    else:
                        self.gesture_update_signal.emit(LEFT)
                else:
                    self.gesture_update_signal.emit(" ")
            else:
                # self.gesture_update_signal.emit(" ")
                pass

            hand_detector.multi_hand_landmarks = None  # Clear hand landmarks

    def stop_thread(self):
        self.ThreadActive = False
        self.quit()

    @Slot()
    def firstWork(self, received_mode):
        self.hand_mode = received_mode


class WiFiThread(QThread):
    wifi_strength_update_signal = Signal(int)
    battery_percentage_update_signal = Signal(int)
    tof_distance_update_signal = Signal(int)
    temperature_update_signal = Signal(float)
    absolute_height_update_signal = Signal(int)
    flight_time_update_signal = Signal(int)
    message_update_signal = Signal(str)
    ui_update_signal = Signal()

    def __init__(self, wifi_instance: WiFi(), drone_instance, parent=None):

        super().__init__(parent)
        self.tello_drone = drone_instance
        self.wifi = wifi_instance
        self.ThreadActive = None

    def run(self):
        self.wifi.find_available_networks()
        if self.wifi.is_wifi_available(DRONE_WIFI_NETWORK_NAME) and not self.wifi.is_there_active_connection:
            self.wifi.connect_to(DRONE_WIFI_NETWORK_NAME, '')
            self.wifi.is_there_active_connection = True
            self.tello_drone.connect()
            self.ThreadActive = True
            self.message_update_signal.emit("<font color=\"GreenYellow\">Successfully connected to the drone.")
            self.ui_update_signal.emit()
        else:
            self.message_update_signal.emit("<font color=\"OrangeRed\">Drone WiFi is not available. Make sure the "
                                            "drone is powered on.")
        while self.ThreadActive:
            if self.wifi.current_connection() == DRONE_WIFI_NETWORK_NAME:
                self.wifi_strength_update_signal.emit(self.wifi.check_signal_strength())
                self.battery_percentage_update_signal.emit(self.tello_drone.get_battery())
                self.tof_distance_update_signal.emit(self.tello_drone.get_distance_tof())
                self.temperature_update_signal.emit(self.tello_drone.get_temperature())
                self.absolute_height_update_signal.emit(self.tello_drone.get_barometer())
                self.flight_time_update_signal.emit(self.tello_drone.get_flight_time())
            else:
                self.wifi_strength_update_signal.emit(0)

    def stop_thread(self):
        self.ThreadActive = False
        self.quit()


class DroneControlThread(QThread):

    def __init__(self, drone_instance, parent=None):
        super().__init__(parent)
        self.ThreadActive = None
        self.move = " "
        self.tello_drone = drone_instance
        self.velocity_vector = [0, 0, 0, 0]
        self.velocity = 50
        self.move_is_present = False
        self.stop_move = False

    def run(self):
        self.ThreadActive = True
        while self.ThreadActive:
            left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity = 0, 0, 0, 0
            if self.move == " " and not self.stop_move:
                self.tello_drone.send_rc_control(0, 0, 0, 0)
                self.stop_move = True
            elif self.move == FORWARD:
                forward_backward_velocity = self.velocity
                self.move_is_present = True
            elif self.move == BACKWARD:
                forward_backward_velocity = -self.velocity
                self.move_is_present = True
            elif self.move == RIGHT:
                left_right_velocity = self.velocity
                self.move_is_present = True
            elif self.move == LEFT:
                left_right_velocity = -self.velocity
                self.move_is_present = True
            elif self.move == TAKE_OFF:
                self.tello_drone.takeoff()
            elif self.move == LAND:
                self.tello_drone.land()
            elif self.move == UP:
                up_down_velocity = self.velocity
                self.move_is_present = True
            elif self.move == DOWN:
                up_down_velocity = -self.velocity
                self.move_is_present = True
            elif self.move == ROTATE_RIGHT:
                yaw_velocity = -self.velocity
                self.move_is_present = True
            elif self.move == ROTATE_LEFT:
                yaw_velocity = self.velocity
                self.move_is_present = True

            if self.move_is_present:
                self.velocity_vector = [left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity]
                self.tello_drone.send_rc_control(self.velocity_vector[0], self.velocity_vector[1],
                                                 self.velocity_vector[2], self.velocity_vector[3])
                self.move_is_present = False
                self.stop_move = False

            time.sleep(0.05)

    def stop_thread(self):
        self.ThreadActive = False
        self.quit()

    @Slot()
    def firstWork(self, received_move):
        self.move = received_move


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
