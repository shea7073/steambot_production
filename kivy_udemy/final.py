from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import bugs


class Main(BoxLayout):
    pass


class Data(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        d = MDDataTable(
            size_hint=(0.85, 0.85),
            use_pagination=True,

            column_data=[
                ('Title', dp(30)),
                ('Current Price', dp(20)),
                ('Discount', dp(20)),
                ('Original Price', dp(22)),
                ('Release Date', dp(30)),
                ('Percentage', dp(18)),
                ('Score', dp(15))
            ],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(d)

class finish(MDApp):
    def build(self):
        self.title = 'SteamBot'
        return Main()


bugs.fixBugs()
finish().run()
