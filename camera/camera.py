import mediapipe as mp
import cv2 as cv
from camera import constants


class Camera:
    """
    A class to represent a camera.
    """

    def __init__(self, width, height, image_source=0):
        self.multi_hand_landmarks = None
        self.hands = None
        self.mp_hands = None
        self.mp_drawing = None
        self.capture = None
        self.width = width
        self.height = height
        self.image_source = image_source

    def start(self) -> None:
        """
        Starts camera.
        """
        self.capture = cv.VideoCapture(self.image_source)
        self.capture.set(cv.CAP_PROP_FRAME_WIDTH, self.width)
        self.capture.set(cv.CAP_PROP_FRAME_HEIGHT, self.height)

    def init_hand_detection_model(self,
                                  static_image_mode,
                                  max_num_hands,
                                  min_detection_confidence,
                                  min_tracking_confidence) -> None:
        """
        Initialize the necessary modules for hand detection from the MediaPipe framework.
        """
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=static_image_mode,
                                         max_num_hands=max_num_hands,
                                         min_detection_confidence=min_detection_confidence,
                                         min_tracking_confidence=min_tracking_confidence)

    def run(self):
        """
        Starts displaying the image from the camera, draws landmarks on the detected hand.
        """
        ret, frame = self.capture.read()

        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image = cv.flip(image, 1)
        image.flags.writeable = False
        results = self.hands.process(image)
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

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

        cv.imshow("Data Collector", image)

    def clear(self) -> None:
        """
        Releases camera's resources.
        """
        self.capture.release()
        cv.destroyAllWindows()
