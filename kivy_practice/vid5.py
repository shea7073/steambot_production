import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyGridLayout(Widget):

    def press(self, instance):
        name = self.name.text
        self.add_widget(Label(text=f'Hello {name} whats crackin'))
        self.name.text = ''


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
