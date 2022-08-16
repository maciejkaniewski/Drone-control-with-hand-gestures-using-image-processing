import mediapipe as mp
import cv2
import numpy as np
from csv import writer

from PySide6.QtGui import QImage, Qt
from sklearn import preprocessing

# Constants for MediaPipe's landmarks
LANDMARK_COLOR_BGR = (155, 68, 236)
LANDMARK_THICKNESS = 7
LANDMARK_RADIUS = 2

# Constants for MediaPipe's hand lines
HAND_LINE_COLOR_BGR = (67, 244, 153)
HAND_LINE_THICKNESS = 4
HAND_LINE_RADIUS = 2


class DataCollector:
    """
    A class used to represent a Data Collector.
    """

    def __init__(self):
        """
        Constructs Data Collector object.
        """

        self.image = None
        self.image_width = 1280
        self.image_height = 720
        self.camera_capture = None

        self.multi_hand_landmarks = None
        self.hands = None
        self.mp_hands = None
        self.mp_drawing = None

        self.options_flag = True
        self.data_raw = []
        self.data_max_abs = []
        self.data_min_max = []
        self.data_standardized = []
        self.data_robust_scaling = []

    def configure_camera(self) -> None:
        """
        Configures the camera.
        """

        self.camera_capture = cv2.VideoCapture(0)
        self.camera_capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.image_width)
        self.camera_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.image_height)

    def free_camera(self) -> None:
        """
        Releases camera's resources.
        """

        self.camera_capture.release()
        cv2.destroyAllWindows()

    def configure_MediaPipe_Hands(self,
                                  static_image_mode: bool,
                                  max_num_hands: int,
                                  min_detection_confidence: float,
                                  min_tracking_confidence: float) -> None:
        """
        Configures the necessary modules for hand detection from the MediaPipe framework.

        :param static_image_mode: if set to false, the solution treats the input images as a video stream
        :param max_num_hands: maximum number of hands to detect
        :param min_detection_confidence: minimum confidence value ([0.0, 1.0]) from the hand detection model for the detection to be considered successful
        :param min_tracking_confidence: minimum confidence value ([0.0, 1.0]) from the landmark-tracking model for the hand landmarks to be considered tracked successfully
        """

        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=static_image_mode,
                                         max_num_hands=max_num_hands,
                                         min_detection_confidence=min_detection_confidence,
                                         min_tracking_confidence=min_tracking_confidence)

    def detect(self) -> None:
        """
        Displays the image from the camera, draws landmarks on the detected hand.
        """

        ret, frame = self.camera_capture.read()

        self.image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.image = cv2.flip(self.image, 1)
        self.image.flags.writeable = False
        results = self.hands.process(self.image)
        self.image.flags.writeable = True
        #self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    self.image,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing.DrawingSpec(color=LANDMARK_COLOR_BGR,
                                                thickness=LANDMARK_THICKNESS,
                                                circle_radius=LANDMARK_RADIUS),
                    self.mp_drawing.DrawingSpec(color=HAND_LINE_COLOR_BGR,
                                                thickness=HAND_LINE_THICKNESS,
                                                circle_radius=HAND_LINE_RADIUS),
                )
            self.multi_hand_landmarks = results.multi_hand_landmarks

        ConvertToQtFormat = QImage(self.image.data, self.image.shape[1], self.image.shape[0],
                                   QImage.Format_RGB888)
        self.image = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)

        #cv2.imshow("Data Collector", self.image)

    def info(self, gesture_label: int = None, keyboard_key=None):
        """
        Displays information about options and saved gestures.

        :param gesture_label: label of the gesture
        :param keyboard_key: pressed keyboard key
        """

        options_image = cv2.imread('data_collector/res/options.png')
        img2gray = cv2.cvtColor(options_image, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

        if gesture_label is not None:
            cv2.putText(self.image,
                        'Successfully saved',
                        (10, 25),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                        (126, 238, 28),
                        1,
                        cv2.LINE_AA)
            cv2.putText(self.image,
                        'gesture landmarks with label: ' + str(gesture_label),
                        (10, 50),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                        (126, 238, 28),
                        1,
                        cv2.LINE_AA)

        if keyboard_key == ord("o"):
            if self.options_flag is False:
                self.options_flag = True
            else:
                self.options_flag = False

        if self.options_flag:
            ROI = self.image[-405:-5, -505:-5]
            ROI[np.where(mask)] = 0
            ROI += options_image

        #cv2.imshow("Data Collector", self.image)

    def convert_coordinates(self) -> None:
        """
        Converts the coordinates of the hand landmarks from absolute to relative to the wrist point.
        """

        wrist_position = self.multi_hand_landmarks[0].landmark[
            self.mp_hands.HandLandmark.WRIST]  # Save wrist point landmark
        for landmark in self.multi_hand_landmarks[0].landmark:  # For each landmark in multi_hand_landmarks
            self.data_raw.append(
                (landmark.x - wrist_position.x) * self.image_width)  # Multiply normalized "x" value by camera width
            self.data_raw.append(
                (landmark.y - wrist_position.y) * self.image_height)  # Multiply normalized "y" value by camera height

    def maximum_absolute_scaling(self) -> None:
        """
        Rescales raw data between -1 and 1 by dividing every observation by its maximum absolute value.
        """

        scaler = preprocessing.MinMaxScaler()
        data_array = np.reshape(self.data_raw, (-1, 1))
        data_scaled = (scaler.fit_transform(data_array))
        self.data_min_max = list(np.concatenate(data_scaled).flat)

    def min_max_scaling(self) -> None:
        """
        Rescales raw data to a fixed range of [0,1] by subtracting the minimum value
        of the feature and then dividing by the range.
        """

        scaler = preprocessing.MaxAbsScaler()
        data_array = np.reshape(self.data_raw, (-1, 1))
        data_scaled = (scaler.fit_transform(data_array))
        self.data_max_abs = list(np.concatenate(data_scaled).flat)

    def standardization(self) -> None:
        """
        Transforms raw data into a distribution with a mean of 0 and a standard deviation of 1. Each standardized
        value is computed by subtracting the mean of the corresponding feature and then dividing by the standard
        deviation.
        """

        scaler = preprocessing.StandardScaler()
        data_array = np.reshape(self.data_raw, (-1, 1))
        data_scaled = (scaler.fit_transform(data_array))
        self.data_standardized = list(np.concatenate(data_scaled).flat)

    def robust_scaling(self) -> None:
        """
        Scale each feature of the data set by subtracting the median and then dividing by the interquartile range.
        """

        scaler = preprocessing.RobustScaler()
        data_array = np.reshape(self.data_raw, (-1, 1))
        data_scaled = (scaler.fit_transform(data_array))
        self.data_robust_scaling = list(np.concatenate(data_scaled).flat)

    def append_labels(self, gesture_label: int = None) -> None:
        """
        Appends gesture labels to data files.

        :param gesture_label: label of the gesture
        """

        self.data_raw.append(gesture_label)
        self.data_max_abs.append(gesture_label)
        self.data_min_max.append(gesture_label)
        self.data_standardized.append(gesture_label)
        self.data_robust_scaling.append(gesture_label)

    def save_data(self, data_raw_file_path: str, data_max_abs_file_path: str,
                  data_min_max_file_path: str, data_standardized_file_path: str,
                  data_robust_scaling_file_path: str) -> None:
        """
        Saves data to the .csv file.

        :param data_raw_file_path: path to the raw data file
        :param data_max_abs_file_path: path to the maximum absolute scaled data file
        :param data_min_max_file_path: path to the min max scaled data file
        :param data_standardized_file_path: path to the standardized data file
        :param data_robust_scaling_file_path: path to the robust scaled data file
        """

        data_files = [[self.data_raw, data_raw_file_path],
                      [self.data_max_abs, data_max_abs_file_path],
                      [self.data_min_max, data_min_max_file_path],
                      [self.data_standardized, data_standardized_file_path],
                      [self.data_robust_scaling, data_robust_scaling_file_path]]

        for files in data_files:
            with open(files[1], 'a', newline='') as f_object:  # Open .csv data file in append mode
                writer_object = writer(f_object)  # Pass the .csv  file object to the writer() function
                writer_object.writerow(files[0])  # Write rows with data list
                f_object.close()  # Close file object
                files[0].clear()  # Clear data list

    @staticmethod
    def clear_data(data_file_path: str) -> None:
        """
        Clears data.

        :param data_file_path: path to the data file
        """

        data_file = open(data_file_path, "w+")  # Open and clear .csv data file
        data_file.close()  # Close .csv data file
