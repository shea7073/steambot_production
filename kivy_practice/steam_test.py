from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
Window.size = (900, 450)


class SteamBot(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        refresh = MDFlatButton(font_size=20, text='Refresh', pos_hint={'center_x': .3, 'center_y': .15})
        title = MDLabel(text='[font=OLDENGL.TTF][size=54]The Steam Bot[/font][/size]', text_color=(0, 0, 1, 1),
                        pos_hint={'center_y': .95, 'center_x': .5}, halign='center', markup=True)
        data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
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

        screen.add_widget(title)
        screen.add_widget(data_tables)
        screen.add_widget(refresh)

        return screen


SteamBot().run()


