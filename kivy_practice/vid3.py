import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):

    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1

        # These will effect the entire root gridlayout
        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 100

        # Those force parameters are for setting stats for an entire grid (top_grid in this case)
        self.top_grid = GridLayout(row_force_default=True,
                                   row_default_height=40,
                                   col_force_default=True,
                                   col_default_width=100
                                   )
        self.top_grid.cols = 2



        self.top_grid.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        self.add_widget(self.top_grid)

        self.submit = Button(text='submit', font_size=32,
                             size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=200)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        self.add_widget(Label(text=f'Hello {name} whats crackin'))
        self.name.text = ''

class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
