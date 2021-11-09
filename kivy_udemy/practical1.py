import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button


class CanvasTut(BoxLayout):
    pass

class Game(BoxLayout):
    btn_lst = []
    i = 0
    Alpha = ['a', 'b', 'c', 'd', 'e']
    def create_btn(self):
        ALPHA = random.choice(self.Alpha)
        r = random.randrange(1, 10)
        g = random.randrange(1, 10)
        b = random.randrange(1, 10)
        R = r/10
        G = g/10
        B = b/10
        btn = Button(text=str(ALPHA), size_hint=(None, None), size=(100, 100), background_color=(R, G, B, 1), background_normal='')
        self.btn_lst.append(btn)
        self.ids.stacker.add_widget(self.btn_lst[self.i])
        self.i += 1

    def rmv_btn(self):
        if self.i > 0:
            self.ids.stacker.remove_widget(self.btn_lst[self.i-1])
            self.btn_lst.pop(self.i-1)
            self.i -= 1


class Buttons(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class Practical1(App):
    pass


Practical1().run()
