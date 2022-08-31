# This Python file uses the following encoding: utf-8
import sys
import os
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from PySide6.QtWidgets import QApplication, QMainWindow

from ui import Ui_MainWindow
from data_collector import DataCollector, cv2


class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        self.data_collector = DataCollector()
        self.data_collector.configure_MediaPipe_Hands(False, 1, 0.8, 0.6)  # Configure MediaPipe model
        self.gesture_label = "0"

        self.CameraThread = CameraThread()
        self.CameraThread.start()
        self.CameraThread.image_update_signal.connect(self.image_update_slot)
        self.CameraThread.landmarks_update_signal.connect(self.landmarks_update_slot)

        self.ui.QPushButton_Save_Gesture.clicked.connect(self.save_gesture)
        self.ui.QPushButton_Clear_All_Gestures.clicked.connect(self.clear_all_gestures)
        self.ui.QSpinBox_Gesture_Label.valueChanged.connect(self.set_gesture_label)

    def closeEvent(self, event):
        self.CameraThread.stop()
        self.CameraThread.wait()
        if self.CameraThread.isFinished():
            event.accept()

    def image_update_slot(self, image):
        self.ui.QLabel_Camera_Feed.setPixmap(QPixmap.fromImage(image))

    def landmarks_update_slot(self, landmarks_list):
        self.data_collector.multi_hand_landmarks = landmarks_list

    def add_to_logs(self, message):
        current_time = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.ui.QTextBrowser_Logs.append("[ " + current_time + " ]" + " :  " + message)

    def set_gesture_label(self):
        self.gesture_label = str(self.ui.QSpinBox_Gesture_Label.value())

    def save_gesture(self):

        if len(self.data_collector.multi_hand_landmarks):

            self.data_collector.convert_coordinates()  # Convert coordinates to wrist-relative
            self.data_collector.maximum_absolute_scaling()  # Perform data normalization methods
            self.data_collector.min_max_scaling()
            self.data_collector.standardization()
            self.data_collector.robust_scaling()
            self.data_collector.append_labels(self.gesture_label)
            self.data_collector.save_data(
            'data_collector/data/01_data_raw.csv',
            'data_collector/data/02_data_max_abs.csv',
            'data_collector/data/03_data_min_max.csv',
            'data_collector/data/04_data_standardized.csv',
            'data_collector/data/05_data_robust.csv')

            self.add_to_logs("<font color=\"GreenYellow\">Gesture with label <font color=\"Plum\">" + self.gesture_label + "<font color=\"GreenYellow\"> has been successfully saved")
        else:
            self.add_to_logs("<font color=\"OrangeRed\">No gesture has been detected in the camera image")

    def clear_all_gestures(self):

        if os.stat('data_collector/data/01_data_raw.csv').st_size == 0:
            self.add_to_logs("<font color=\"Gold\">Gesture files are already empty, no need to clear")
        else:
            self.data_collector.clear_data('data_collector/data/01_data_raw.csv')
            self.data_collector.clear_data('data_collector/data/02_data_max_abs.csv')
            self.data_collector.clear_data('data_collector/data/03_data_min_max.csv')
            self.data_collector.clear_data('data_collector/data/04_data_standardized.csv')
            self.data_collector.clear_data('data_collector/data/05_data_robust.csv')

            self.add_to_logs("<font color=\"GreenYellow\">All gesture files have been cleared")


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

    def stop(self):
        self.ThreadActive = False
        self.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
