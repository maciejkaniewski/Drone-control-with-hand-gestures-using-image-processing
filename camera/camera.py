import mediapipe as mp
import cv2
import numpy as np

from camera import constants


class Camera:
    """
    A class used to represent a Camera.
    """

    def __init__(self, width: int, height: int, image_source: int = 0):
        """
        Constructs camera object.

        :param width: camera width
        :param height: camera height
        :param image_source: image source
        """
        self.multi_hand_landmarks = None
        self.hands = None
        self.mp_hands = None
        self.mp_drawing = None
        self.capture = None
        self.width = width
        self.height = height
        self.image_source = image_source
        self.help_flag = True

    def start(self) -> None:
        """
        Starts camera.
        """
        self.capture = cv2.VideoCapture(self.image_source)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

    def free(self) -> None:
        """
        Releases camera's resources.
        """
        self.capture.release()
        cv2.destroyAllWindows()

    def initialize_MediaPipe_Hands(self,
                                   static_image_mode: bool,
                                   max_num_hands: int,
                                   min_detection_confidence: float,
                                   min_tracking_confidence: float) -> None:
        """
        Initializes the necessary modules for hand detection from the MediaPipe framework.

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

    def run(self, gesture_id: int = None, keyboard_key=None) -> None:
        """
        Starts displaying the image from the camera, draws landmarks on the detected hand.

        :param gesture_id: ID of the gesture
        :param keyboard_key: pressed keyboard key
        """
        ret, frame = self.capture.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        image.flags.writeable = False
        results = self.hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Read logo and resize
        src = cv2.imread('resources/options.png')

        img2gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing.DrawingSpec(color=constants.LANDMARK_COLOR_BGR,
                                                thickness=constants.LANDMARK_THICKNESS,
                                                circle_radius=constants.LANDMARK_RADIUS),
                    self.mp_drawing.DrawingSpec(color=constants.HAND_LINE_COLOR_BGR,
                                                thickness=constants.HAND_LINE_THICKNESS,
                                                circle_radius=constants.HAND_LINE_RADIUS),
                )
            self.multi_hand_landmarks = results.multi_hand_landmarks

        if gesture_id is not None:
            cv2.putText(image,
                        'Successfully saved',
                        (10, 25),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                        (126, 238, 28),
                        1,
                        cv2.LINE_AA)
            cv2.putText(image,
                        'gesture landmarks with ID: ' + str(gesture_id),
                        (10, 50),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                        (126, 238, 28),
                        1,
                        cv2.LINE_AA)

        if keyboard_key == ord("o"):
            if self.help_flag is False:
                self.help_flag = True
            else:
                self.help_flag = False

        if self.help_flag:
            roi = image[-405:-5, -505:-5]
            roi[np.where(mask)] = 0
            roi += src

        cv2.imshow("Data Collector", image)
