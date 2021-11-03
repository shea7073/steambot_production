from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout

# USES OTHER.KV

Builder.load_file('other.kv')
# go into app class and overwrite def build(), returning the kv file you want to return
# Can also directly load kv language, passed as a doc string with Builder.load_String('''kv''')

class ExternalKivy(BoxLayout):
    pass


class Page_Layout(PageLayout):
    pass


class Page_1(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Hello")
        b2 = Button(text='World')
        self.add_widget(b1)
        self.add_widget(b2)


class Page_2(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Good")
        b2 = Button(text='Job')
        self.add_widget(b1)
        self.add_widget(b2)


class Page_3(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Keep")
        b2 = Button(text='Going')
        self.add_widget(b1)
        self.add_widget(b2)


class Relative_Practice(FloatLayout):
    pass


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


class Binding(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text='hello')
        b1.bind(on_press=self.callback_func)
        self.add_widget(b1)

    def callback_func(self, event):
        print('whats up')


class Practice5(App):
    def build(self):
        return Binding()


Practice5().run()
