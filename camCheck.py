import cv2

def check_camera():
    # Open the default camera (usually camera index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "Camera was not detected."

    # Release the camera
    cap.release()
    
    return "Camera is working correctly."

if __name__ == '__main__':
    result = check_camera()
    print(result)
