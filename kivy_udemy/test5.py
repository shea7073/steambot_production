from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout


class Interface(FloatLayout):
    pass


class Scroller():
    pass


class Stackinterface(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            b = Button(text=f'{i+1}', size_hint=(.15, .15), background_color=(1, 0, 0, 1))
            self.add_widget(b)

class Practice5(App):
    pass


Practice5().run()
