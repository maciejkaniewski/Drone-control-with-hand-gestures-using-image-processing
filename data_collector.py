from camera import Camera, cv


def run_application():
    """
    Executes the main application.
    """
    camera = Camera(1280, 720)
    camera.init_hand_detection_model(False, 1, 0.8, 0.6)
    camera.start()

    while camera.capture.isOpened():
        camera.run()
        keyboard_key = cv.waitKey(5) & 0xFF
        if keyboard_key == ord("q"):
            break
        elif keyboard_key == ord("m"):
            print("Save mode")
            print(
                f'Index finger tip coordinates: (',
                f'{camera.multi_hand_landmarks[0].landmark[20].x * camera.width}, '
                f'{camera.multi_hand_landmarks[0].landmark[20].y * camera.height}) '
            )
    camera.clear()


if __name__ == "__main__":
    run_application()
