from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button


class Game(BoxLayout):
    btn_lst = []
    i = 0
    def create_btn(self, stacker):
        btn = Button(text='h', size_hint=(None, None), size=(100, 100))
        self.btn_lst.append(btn)
        self.ids.stacker.add_widget(self.btn_lst[self.i])
        self.i += 1

    def rmv_btn(self, stacker):
        self.ids.stacker.remove_widget(self.btn_lst[self.i-1])
        self.i -= 1


class Buttons(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class Practical1(App):
    pass


Practical1().run()
