# This Python file uses the following encoding: utf-8
import sys
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

        self.CameraThread = CameraThread()
        self.CameraThread.start()
        self.CameraThread.image_update_signal.connect(self.image_update_slot)

    def closeEvent(self, event):
        self.CameraThread.stop()
        self.CameraThread.wait()
        if self.CameraThread.isFinished():
            event.accept()

    def image_update_slot(self, Image):
        self.ui.QLabel_Camera_Feed.setPixmap(QPixmap.fromImage(Image))

class CameraThread(QThread):

    image_update_signal = Signal(QImage)

    def run(self):

        data_collector = DataCollector()  # Construct Data Collector instance
        data_collector.configure_camera()  # Configure Data Collector's camera
        data_collector.configure_MediaPipe_Hands(False, 1, 0.8, 0.6)  # Configure MediaPipe model
        self.ThreadActive = True

        while self.ThreadActive:
            data_collector.detect()
            self.image_update_signal.emit(data_collector.image)
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
