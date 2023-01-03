from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyLayout(Widget):
    greeting = ObjectProperty(None)

    def click_btn(self):
        name = self.ids.name_input.text

        self.ids.name_label.text = f"Hello {name} !"


class MyApp(App):
    def build(self):

        return MyLayout()


if __name__ == "__main__":
    MyApp().run()
