from kivy.app import App
from kivy.uix.widget import Widget


class Interface(Widget):

    def On_Enter_Pressed(self):
        print('Enter has been pressed! \n Good logic!')


class TestApp(App):
    pass


TestApp().run()
