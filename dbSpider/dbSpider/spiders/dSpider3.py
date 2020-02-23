# -*- coding: utf-8 -*-
import scrapy
import pymysql

class Dspider3Spider(scrapy.Spider):
    name = 'dSpider3'
    allowed_domains = ['music.douban.com']
    start_urls = ['http://music.douban.com/']
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='aaa', charset='utf8')
    cursor = conn.cursor()

    def parse(self, response):
        sql = 'select singer_id, singer_name'
