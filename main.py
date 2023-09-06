from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from camCheck import check_camera
from register import detect_and_save_faces
from login import login_with_face
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3

# SQLite3 Database Initialization
class Database:
    def __init__(self, db_name='myapp.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Create a table for user data (you can customize this schema)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT,
                email TEXT
            )
        ''')
        self.conn.commit()

    def insert_user(self, full_name, email):
        # Insert a new user record into the database
        self.cursor.execute('INSERT INTO users (full_name, email) VALUES (?, ?)', (full_name, email))
        self.conn.commit()

    def close(self):
        # Close the database connection
        self.conn.close()

class MyApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', spacing=20, padding=20)
        layout.add_widget(BoxLayout(size_hint_y=None, height=1))
        button_layout = BoxLayout(orientation='horizontal', spacing=20)

        # Sign Up button
        sign_up_button = Button(
            text="Sign Up",
            size_hint=(None, None),
            size=(200, 100),
            background_color=(0.18, 0.65, 0.82, 1),  # Blue background color
            color=(1, 1, 1, 1),  # Text color (white)
            font_size=24,  # Font size
        )
        sign_up_button.bind(on_press=self.start_detection)
        button_layout.add_widget(sign_up_button)

        # Login button
        login_button = Button(
            text="Login",
            size_hint=(None, None),
            size=(200, 100),
            background_color=(0.2, 0.8, 0.2, 1),  # Green background color
            color=(1, 1, 1, 1),  # Text color (white)
            font_size=24,  # Font size
        )
        login_button.bind(on_press=self.login_with_face_and_display_result)
        button_layout.add_widget(login_button)

        layout.add_widget(button_layout)

        # Space to separate the buttons from the Check Camera button
        layout.add_widget(BoxLayout(size_hint_y=None, height=20))

        # Check Camera button
        check_camera_button = Button(
            text="Check Camera",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.9, 0.1, 0.1, 1),  # Red background color
            color=(1, 1, 1, 1),  # Text color (white)
            font_size=20,  # Font size
        )
        check_camera_button.bind(on_press=self.check_camera)
        layout.add_widget(check_camera_button)

        return layout

    # Popup 
    def show_loading_popup(self, text):
        # Create a loading popup
        self.loading_popup = Popup(title="Loading", content=Label(text=text), size_hint=(None, None), size=(200, 100))
        self.loading_popup.open()

    def hide_loading_popup(self):
        # Dismiss the loading popup
        if self.loading_popup:
            self.loading_popup.dismiss()

    # Test Camera button
    def check_camera(self, instance):
        self.show_loading_popup("Checking Camera Status, Please wait") 

        # Schedule the camera test and result display
        Clock.schedule_once(self.test_camera_and_display_result, 0)

    def test_camera_and_display_result(self, dt):
        result = check_camera()
        self.hide_loading_popup()  # Hide loading popup

        # Create a popup with the camera test result
        popup = Popup(title="Camera Test Result", content=Label(text=result), size_hint=(None, None), size=(400, 200))
        popup.open()

    def start_detection(self, instance):
        # Create a popup for user registration
        registration_popup = Popup(title="User Registration", size_hint=(None, None), size=(400, 200))
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        full_name_input = TextInput(hint_text="Full Name")
        email_input = TextInput(hint_text="Email")
        start_detection_button = Button(text="Start Detection")

        def start_detection_and_register(_):
            full_name = full_name_input.text
            email = email_input.text

            # Insert user data into the database
            db = Database()
            db.insert_user(full_name, email)
            db.close()

            # Indicate that sign-up is in progress
            global sign_up_completed
            sign_up_completed = False

            # Close the registration popup
            registration_popup.dismiss()

            # Show loading popup while performing face detection
            self.show_loading_popup("Performing Face Detection")

            # Schedule face detection and registration with sign-up completion status
            Clock.schedule_once(lambda dt, full_name=full_name: self.detect_and_register_faces(full_name, sign_up_completed), 0)

        start_detection_button.bind(on_press=start_detection_and_register)
        layout.add_widget(full_name_input)
        layout.add_widget(email_input)
        layout.add_widget(start_detection_button)
        registration_popup.content = layout
        registration_popup.open()

    def detect_and_register_faces(self, full_name, sign_up_completed):
        # Perform face detection and registration
        detect_and_save_faces(full_name, sign_up_completed)
        self.hide_loading_popup()  # Hide loading popup

        # Show a popup to indicate that the registration is completed
        popup = Popup(title="Sign Up Completed!", content=Label(text="Registration is complete."), size_hint=(None, None), size=(400, 200))
        popup.open()

    def login_with_face_and_display_result(self, instance):        
        # Call the login_with_face function from login.py
        login_result = login_with_face()

        # Create a popup to display the login result
        popup = Popup(title="Login Result", content=Label(text=login_result), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    MyApp().run()
