from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class UserScreen(Screen):
    def __init__(self, full_name, image_path, **kwargs):
        super(UserScreen, self).__init__(**kwargs)
        self.full_name = full_name
        self.image_path = image_path

        # Create the user interface for the UserScreen
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Display the user's image
        image = Image(source=image_path)
        layout.add_widget(image)
        
        # Greet the user with their full name
        greeting_label = Label(text=f"Hi {full_name}!")
        layout.add_widget(greeting_label)

        self.add_widget(layout)
