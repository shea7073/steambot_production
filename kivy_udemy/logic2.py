from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty


class Externalkivy(BoxLayout):
    pass


class Variables(BoxLayout):

    _text_ = StringProperty('hello world')

    def pressing(self, btn):
            btn.text = 'we have changed this text with self'


class LogicalInterface(BoxLayout):

    def OnPressing(self, id, id2):
        print('it works!')
        cal = eval(id2.text)
        id.text = str(cal)

    def OnRelease(self, id, id2):
        print('you released!')



class Practice7(App):
    pass


Practice7().run()