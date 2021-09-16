import time

import scrapy
from scrapy.crawler import CrawlerProcess
import json
import re
import sqlite3
import os


class Test2Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=_ASC&snr=1_7_7_7000_7&filter=topsellers&infinite=0']
    counter = 0

    def parse(self, response):
        for game in response.xpath("//div[@id='search_resultsRows']/a"):
            yield {
                'title': game.xpath(".//div[@class='responsive_search_name_combined']/div[1]/span/text()").get(),
                'current_price': game.xpath(".//div[@class='col search_price_discount_combined responsive_secondrow']/@data-price-final").get(),
                'discount': game.xpath(".//div[@class='col search_discount responsive_secondrow']/span/text()").get(),
                'original_price': game.xpath(".//div[@class='responsive_search_name_combined']/div[4]/div[2]/span/strike/text()").get(),
                'release_date': game.xpath(".//div[@class='col search_released responsive_secondrow']/text()").get(),
                'rating': game.xpath(".//span[contains(@class, 'search_review_summary')]/@data-tooltip-html").get()
            }
        self.counter += 50
        if self.counter <= 300:
             yield scrapy.Request(url=f'https://store.steampowered.com/search/results/?query&start={self.counter}&count=50&dynamic_data=&sort_by=_ASC&snr=1_7_7_7000_7&filter=topsellers&infinite=0', callback=self.parse)


process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'output.json'
})


def clean_data(file_name):

    with open(file_name, encoding='utf-8') as f:
        data = json.load(f)

    de_duplicated = []
    for dic in data:
        if dic not in de_duplicated:
            de_duplicated.append(dic)

    for dic in de_duplicated:
        dic['current_price'] = '$' + str(int(dic['current_price']) / 100)
        num_pattern = "\d\d+%"
        text_pattern = "(.*?)<"
        if dic['rating'] and re.search(num_pattern, dic['rating']):
            dic['num_score'] = re.search(num_pattern, dic['rating']).group(0)
            dic['word_score'] = re.search(text_pattern, dic['rating']).group(0)
        else:
            dic['num_score'] = None
            dic['word_score'] = None

    return de_duplicated


def data_insert(list_dics):
    conn = sqlite3.connect('games.db')
    c = conn.cursor()

    c.execute('''
          CREATE TABLE IF NOT EXISTS top_sellers (
          title TEXT PRIMARY KEY, current_price TEXT, discount TEXT, original_price TEXT, 
          release_date TEXT, num_score TEXT, word_score TEXT
          )''')

    for dic in list_dics:
        c.execute("""
            INSERT or REPLACE INTO top_sellers
            (title, current_price, discount, original_price, release_date, num_score, word_score)
            VALUES
            (:title, :current_price, :discount, :original_price, :release_date, :num_score, :word_score)""", dic)

    c.execute("SELECT * FROM top_sellers WHERE word_score = 'Overwhelmingly Positive<'")
    print(len(c.fetchall()))

    conn.commit()
    c.close()
    conn.close()


if os.path.exists("output.json"):
    os.remove("output.json")
process.crawl(Test2Spider)
process.start()
ready = clean_data('output.json')
data_insert(ready)

