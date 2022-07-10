import mediapipe as mp
import cv2 as cv


class Camera:
    """
    A class to represent a camera.
    """
    def __init__(
            self,
            static_image_mode,
            max_num_hands,
            model_complexity,
            min_detection_confidence,
            min_tracking_confidence,
    ):
        self.cap = None
        self.mp_hands = None
        self.mp_drawing = None
        self.hands = None
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.model_complexity = model_complexity
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

    def load_modules(self) -> None:
        """
        Loads the necessary modules for hand detection from the MediaPipe framework, starts camera operation.
        """
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=self.static_image_mode,
                                         max_num_hands=self.max_num_hands,
                                         min_detection_confidence=self.min_detection_confidence,
                                         min_tracking_confidence=self.min_tracking_confidence)
        self.cap = cv.VideoCapture(0)

    def run(self):
        """
        Starts displaying the image from the camera, draws landmarks on the detected hand.
        """
        ret, frame = self.cap.read()

        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image = cv.flip(image, 1)
        image.flags.writeable = False
        results = self.hands.process(image)
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                self.mp_drawing.draw_landmarks(
                    image,
                    hand,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing.DrawingSpec(color=(155, 68, 236), thickness=6, circle_radius=1),
                    self.mp_drawing.DrawingSpec(color=(67, 244, 153), thickness=3, circle_radius=2),
                )

        cv.imshow("Camera", image)

    def clear(self) -> None:
        """
        Release camera's resources.
        """
        self.cap.release()
        cv.destroyAllWindows()
