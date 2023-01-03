import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.widget import Widget


class Mylayout(Widget):
    pass


class Login(MDApp):
    def login_build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('log.kv')
    def logger(self):
        self.root.ids.welcome_label.text = f"Welcome {self.root.ids.user.text}!"
   
    def clear(self):
        self.root.ids.welcome_label.text = f"Create your login: {self.root.ids.user.text}!"
        self.root.ids.user.text = " "
        self.root.ids.password.text = " "





if __name__ == "__main__":
    Login().run()





