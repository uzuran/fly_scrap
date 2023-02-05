# Here is important that you will import kivymd that you need install separate by, pip or something in your IDE.
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window


Window.size = (340, 620)


class MenuScreen(Screen):
    pass


class RegistrationScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class AboutApplicationScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name="menu"))
sm.add_widget(RegistrationScreen(name="Sign up"))
sm.add_widget(LoginScreen(name="Log in"))
sm.add_widget(AboutApplicationScreen(name="About app"))


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("log.kv")


if __name__ == "__main__":
    LabelBase.register(name="SourceCodePro", fn_regular="fonts/SofiaSansExtraCondensed-Italic-VariableFont_wght.ttf")

    MyApp().run()


