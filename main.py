import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class MyGrid(Widget):
    pass

class MyApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        # center our UI to center for better view
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # image widget
        self.window.add_widget(Image(source="logo.jpg"))

        # label widget
        self.greeting = Label(
                        text = "Test invitation greeting!",
                        font_size = 18,
                        color = "#FFFF00"
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                    multiline = False,
                    padding_y = (20, 20), # change to input window to the middle
                    size_hint = (1, 0.5) # transfer text to the middle of the window
                    )
        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                        text = "Click here for log in",
                        size_hint = (1, 0.5),
                        bold = True,
                        background_color = "#FFFF00",
                        )
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = "Hello " + self.user.text + "!"

if __name__ == "__main__":
    MyApp().run()
