from data_collector import DataCollector, cv2


def run_data_collector() -> None:
    """
    Executes data collector application.
    """
    data_collector = DataCollector()  # Construct Data Collector instance
    data_collector.configure_camera()  # Configure Data Collector's camera
    data_collector.configure_MediaPipe_Hands(False, 1, 0.8, 0.6)  # Configure MediaPipe model

    gesture_id = None  # Variable for gesture ID
    keyboard_key = None  # Variable for keyboard key

    while data_collector.camera_capture.isOpened():  # Main loop
        data_collector.detect()
        data_collector.info(gesture_id, keyboard_key)
        keyboard_key = cv2.waitKey(5) & 0xFF  # Waiting for a keyboard key
        if keyboard_key == ord("q"):  # If "q" key is pressed
            break  # Exit the loop and quit the application
        elif keyboard_key == ord("c"):  # If "c" key is pressed
            data_collector.clear_data('data_collector/data/data.csv')
        # If "0,1,2... 9" key is pressed and hand landmarks are not empty
        elif keyboard_key in range(48, 58, 1) and data_collector.multi_hand_landmarks is not None:
            gesture_id = int(chr(keyboard_key))  # Assign ID corresponding to pressed key
            data_collector.data.append(gesture_id)  # Add ID at the beginning of data
            data_collector.convert_coordinates()
            data_collector.save_data('data_collector/data/data.csv')
        data_collector.multi_hand_landmarks = None  # Clear hand landmarks
    data_collector.free_camera()  # Free data_collector's resources


if __name__ == "__main__":
    run_data_collector()
