from camera import Camera, cv
from csv import writer


def run_data_collector() -> None:
    """
    Executes data collector application.
    """
    camera = Camera(1280, 720, 0)  # Construct Camera instance
    camera.initialize_MediaPipe_Hands(False, 1, 0.8, 0.6)  # Initialize MediaPipe model
    camera.start()  # Start camera

    data = []  # Empty list for data collection
    gesture_id = None  # Variable for gesture ID

    while camera.capture.isOpened():  # Main camera loop
        camera.run(gesture_id)  # Collecting data from the camera
        keyboard_key = cv.waitKey(5) & 0xFF  # Waiting for a keyboard key
        if keyboard_key == ord("q"):  # If "q" key is pressed
            break  # Exit the loop and quit the application
        elif keyboard_key == ord("c"):  # If "c" key is pressed
            f = open('data/data.csv', "w+")  # Open and clear .csv data file
            f.close()  # Close .csv data file
        elif keyboard_key in range(48, 58, 1) and camera.multi_hand_landmarks is not None:  # If "1,2... 9" key is
            # pressed and hand landmarks are not empty
            gesture_id = int(chr(keyboard_key))  # Assign ID corresponding to pressed key
            data.append(gesture_id)  # Add ID at the beginning of data
            for i in camera.multi_hand_landmarks[0].landmark:  # For each landmark in multi_hand_landmarks
                data.append(i.x * camera.width)  # Multiply normalized "x" value by camera width
                data.append(i.y * camera.height)  # Multiply normalized "y" value by camera height
            with open('data/data.csv', 'a', newline='') as f_object:  # Open .csv data file in append mode
                writer_object = writer(f_object)  # Pass the .csv  file object to the writer() function
                writer_object.writerow(data)  # Write rows with data list
                f_object.close()  # Close file object
            data.clear()  # Clear data list
    camera.free()  # Free camera's resources


if __name__ == "__main__":
    run_data_collector()
