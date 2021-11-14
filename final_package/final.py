from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.core.window import Window
import bugs
import sqlite3
import os
import sys
import scraper

Window.size = 1000, 600


def on_sale():
    row_data = []
    conn = sqlite3.connect('games.db')
    c = conn.cursor()
    c.execute("SELECT * FROM top_sellers WHERE discount IS NOT NULL")
    records = c.fetchall()
    for row in records:
        row_data.append(row)
    return row_data


def overwhelm():
    row_data = []
    conn = sqlite3.connect('games.db')
    c = conn.cursor()
    c.execute("SELECT * FROM top_sellers WHERE word_score = 'Overwhelmingly Positive<'")
    records = c.fetchall()
    for row in records:
        row_data.append(row)
    return row_data


def load_data():
    row_data = []
    conn = sqlite3.connect('games.db')
    c = conn.cursor()
    c.execute("SELECT * FROM top_sellers")
    records = c.fetchall()
    for row in records:
        row_data.append(row)
    return row_data


class Main(BoxLayout):
    pass


class Data(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if state == 1:
            row_data = load_data()
        elif state == 2:
            row_data = overwhelm()
        elif state == 3:
            row_data = on_sale()
        else:
            print('error')

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


class finish(MDApp):

    def build(self):
        self.title = 'SteamBot'
        return Main()

    def recreate(self):
        scraper.scrape()
        self.root.clear_widgets()
        self.root.add_widget(Main())
        print('DONE')


bugs.fixBugs()
finish().run()
