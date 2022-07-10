from camera import Camera, cv


def run_application():
    """
    Executes the main application.
    """
    camera = Camera(False, 1, 1, 0.8, 0.5)
    camera.load_modules()

    while camera.cap.isOpened():
        camera.run()
        if cv.waitKey(10) & 0xFF == ord("q"):
            break
    camera.clear()


if __name__ == '__main__':
    run_application()
