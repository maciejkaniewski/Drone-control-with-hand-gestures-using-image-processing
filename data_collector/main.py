from data_collector import DataCollector, cv2


def run_data_collector() -> None:
    """
    Executes data collector application.
    """
    data_collector = DataCollector()  # Construct Data Collector instance
    data_collector.configure_camera()  # Configure Data Collector's camera
    data_collector.configure_MediaPipe_Hands(False, 1, 0.8, 0.6)  # Configure MediaPipe model

    gesture_label = None  # Variable for gesture label
    keyboard_key = None  # Variable for keyboard key

    while data_collector.camera_capture.isOpened():  # Main loop
        data_collector.detect()
        data_collector.info(gesture_label, keyboard_key)
        keyboard_key = cv2.waitKey(5) & 0xFF  # Waiting for a keyboard key
        if keyboard_key == ord("q"):  # If "q" key is pressed
            break  # Exit the loop and quit the application
        elif keyboard_key == ord("c"):  # If "c" key is pressed
            data_collector.clear_data('data_collector/data/01_data_raw.csv')
            data_collector.clear_data('data_collector/data/02_data_max_abs.csv')
            data_collector.clear_data('data_collector/data/03_data_min_max.csv')
            data_collector.clear_data('data_collector/data/04_data_standardized.csv')
        # If "0,1,2... 9" key is pressed and hand landmarks are not empty
        elif keyboard_key in range(48, 58, 1) and data_collector.multi_hand_landmarks is not None:
            gesture_label = int(chr(keyboard_key))  # Assign label corresponding to pressed key
            data_collector.convert_coordinates()  # Convert coordinates to wrist-relative
            data_collector.maximum_absolute_scaling()  # Perform data normalization methods
            data_collector.min_max_scaling()
            data_collector.standardization()
            data_collector.append_labels(gesture_label)
            data_collector.save_data('data_collector/data/01_data_raw.csv',
                                     'data_collector/data/02_data_max_abs.csv',
                                     'data_collector/data/03_data_min_max.csv',
                                     'data_collector/data/04_data_standardized.csv')
        data_collector.multi_hand_landmarks = None  # Clear hand landmarks
    data_collector.free_camera()  # Free data_collector's resources


if __name__ == "__main__":
    run_data_collector()
