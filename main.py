import kivy
from kivy.app import App
<<<<<<< Updated upstream
=======
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty



class MyLayout(Widget):
    greeting = ObjectProperty(None)

    def click_btn(self):
        name = self.ids.name_input.text

        self.ids.name_label.text = f"Hello {name} !"
>>>>>>> Stashed changes

from kivy.uix.widget import Widget

class MyGrid(Widget):
    pass

class MyApp(App):
    def build(self):
<<<<<<< Updated upstream
        return MyGrid()
=======
       
        return MyLayout()

>>>>>>> Stashed changes




if __name__ == "__main__":
    MyApp().run()

