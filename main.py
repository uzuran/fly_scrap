# Here is important that you will import kivymd that you need install separate by, pip or something in your IDE.
from kivymd.app import MDApp
from kivy.lang import Builder

# Please tell me here why we use the MDApp ? Here we can speak about that on meeting.
class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("log.kv")


if __name__ == "__main__":
    MyApp().run()

