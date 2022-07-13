from camera import Camera, cv
from csv import writer


def run_application():
    """
    Executes the main application.
    """
    camera = Camera(1280, 720)
    camera.init_hand_detection_model(False, 1, 0.8, 0.6)
    camera.start()

    data = []
    gesture_id = None

    while camera.capture.isOpened():
        camera.run(gesture_id)
        keyboard_key = cv.waitKey(5) & 0xFF
        if keyboard_key == ord("q"):  # Quit the application
            break
        elif keyboard_key == ord("c"):  # Clear .csv file
            f = open('data/data.csv', "w+")
            f.close()
        elif keyboard_key in range(48, 58, 1) and camera.multi_hand_landmarks is not None:
            gesture_id = int(chr(keyboard_key))
            data.append(gesture_id)
            for i in camera.multi_hand_landmarks[0].landmark:
                data.append(i.x * camera.width)
                data.append(i.y * camera.height)
            with open('data/data.csv', 'a', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(data)
                f_object.close()
            data.clear()
    camera.clear()


if __name__ == "__main__":
    run_application()
