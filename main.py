# Import Kivy modules
from kivy.app import App
from kivy.uix.label import Label

# Define the app class
class HelloWorldApp(App):
    def build(self):
        return Label(text='Hello, World.')

# Run the app
if __name__ == '__main__':
    HelloWorldApp().run()
