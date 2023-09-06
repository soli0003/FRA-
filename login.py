import cv2

def login_with_face():
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open the default camera (usually camera index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "Error: Could not open camera."

    while True:
        # Capture frame-by-frame from the camera
        ret, frame = cap.read()

        if not ret:
            return "Error: Could not read a frame."

        # Convert the frame to grayscale (required for face detection)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        # Check if a face is detected
        if len(faces) > 0:
            print("Face detected. Logging in...")
            return "Login successful."

        # Press 'q' to exit the loop and close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

    # If no face was detected
    return "Login failed. Face not detected."

if __name__ == '__main__':
    login_result = login_with_face()
    print(login_result)
