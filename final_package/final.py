from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import bugs
import sqlite3
import os
import sys
import scraper


Window.size = 1000, 600


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    pass


class WindowManager(ScreenManager):
    def go(self, value):
        self.current = value

    def go2(self, value):
        self.current = value

    def go3(self, value):
        self.current = value


def load_data(state):
    row_data = []
    conn = sqlite3.connect('games.db')
    c = conn.cursor()
    if state == 1:
        c.execute("SELECT * FROM top_sellers")
    elif state == 2:
        c.execute("SELECT * FROM top_sellers WHERE word_score = 'Overwhelmingly Positive<' ORDER BY num_score DESC")
    elif state == 3:
        c.execute("SELECT * FROM top_sellers WHERE discount IS NOT NULL")
    else:
        print("State Error")
    records = c.fetchall()
    for row in records:
        row_data.append(row)
    return row_data


class Data1(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scraper.scrape()
        row_data = load_data(1)

        d = MDDataTable(
            size_hint=(0.85, 0.85),
            use_pagination=True,

            column_data=[
                ('Title', dp(60)),
                ('Current Price', dp(20)),
                ('Discount', dp(25)),
                ('Original Price', dp(22)),
                ('Release Date', dp(30)),
                ('Percentage', dp(18)),
                ('Score', dp(15))
            ],
            row_data=row_data,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(d)


class Data2(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        row_data = load_data(2)

        d = MDDataTable(
            size_hint=(0.85, 0.85),
            use_pagination=True,

            column_data=[
                ('Title', dp(60)),
                ('Current Price', dp(20)),
                ('Discount', dp(25)),
                ('Original Price', dp(22)),
                ('Release Date', dp(30)),
                ('Percentage', dp(18)),
                ('Score', dp(15))
            ],
            row_data=row_data,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(d)


class Data3(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        row_data = load_data(3)

        d = MDDataTable(
            size_hint=(0.85, 0.85),
            use_pagination=True,

            column_data=[
                ('Title', dp(60)),
                ('Current Price', dp(20)),
                ('Discount', dp(25)),
                ('Original Price', dp(22)),
                ('Release Date', dp(30)),
                ('Percentage', dp(18)),
                ('Score', dp(15))
            ],
            row_data=row_data,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(d)



class runner(MDApp):

    def build(self):
        self.title = 'SteamBot'
        return Builder.load_file('finish.kv')


if __name__ == '__main__':
    bugs.fixBugs()
    runner().run()
