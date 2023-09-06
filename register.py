import cv2
import os

def detect_and_save_faces(full_name, sign_up_completed, output_directory='detected_faces'):
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open the default camera (usually camera index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Create a directory to store the detected faces
    os.makedirs(output_directory, exist_ok=True)

    while not sign_up_completed:
        # Capture frame-by-frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read a frame.")
            break

        # Convert the frame to grayscale (required for face detection)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        # Extract and save the detected faces as separate image files with the entered name
        for i, (x, y, w, h) in enumerate(faces):
            face = frame[y:y+h, x:x+w]
            face_name = os.path.join(output_directory, f'{full_name}_face_{i}.jpg')
            cv2.imwrite(face_name, face)

        # Check if a face is detected, and complete the sign-up process
        if len(faces) > 0:
            sign_up_completed = True

        # Press 'q' to exit the loop and close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
             
    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
