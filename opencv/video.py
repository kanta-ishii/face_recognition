import cv2

def Video():
    camera = cv2.VideoCapture(0)    # Specify webcam

    while True:
        ret, frame = camera.read()
        cv2.imshow('camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()