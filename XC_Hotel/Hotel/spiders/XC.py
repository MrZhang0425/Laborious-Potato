# -*- coding: utf-8 -*-
import scrapy
from GET_CODE_NAME import get_str
import re
import datetime
from selenium import webdriver
from  selenium.webdriver.chrome.options import Options    # 使用无头浏览器
import time
from scrapy import signals
import random
from Hotel.settings import USER_AGENTS
from se_get_price import selenium_get_price
import copy

class XcSpider(scrapy.Spider):
    name = 'XC'
    # allowed_domains = ['ctrip.com']
    # start_urls = ['https://hotels.ctrip.com/hotel/changsha206/p1']
    start_urls = ['https://hotels.ctrip.com/hotel/']
    url_index = 'https://hotels.ctrip.com/hotel/'          # 模板，用于字符串拼接
    hunan = ['长沙','株洲', '湘潭', '衡阳', '邵阳', '岳阳', '常德', '张家界', '益阳', '娄底', '郴州', '永州', '怀化', '湘西']
    dict_city = get_str(hunan)

    def parse(self,response):
        item={}
        for city in self.hunan:
            print('city3'  + city)
            item['city'] = city
            code_city = self.dict_city[city]
            print('dict_city  ' + code_city)
            city_url = self.start_urls[0] + code_city + '/p1'
            print('city_url  '+ city_url)

            yield scrapy.Request(
                url = city_url,
                meta={'item': copy.deepcopy(item)},
                callback = self.parse2

            )

    def parse2(self,response):
        item = response.meta['item']
        item = copy.deepcopy(item)
        city = item['city']
        print('city2   ' + city)
        max_page = response.xpath('//*[@id="page_info"]/div[1]/a[@rel="nofollow"]/text()').extract_first()  # 最大页数
        print("max_page:   " + str(max_page))
        print('aaaa' + str(self.dict_city[city]))
        for i in range(int(max_page)):
            yield scrapy.Request(
                url=self.url_index + self.dict_city[item['city']] + "/p" + str(i),
                meta={'item': copy.deepcopy(item)},
                callback = self.parse_single_page

            )

    def parse_single_page(self, response):

        item = response.meta['item']
        item = copy.deepcopy(item)
        print('===================',response.url)
        # 得到酒店详情页url
        hotel_list = response.xpath('//*[@id="hotel_list"]/div')
        for hotel_detail in hotel_list[0:-2]:
            try:
                try:
                    hotel_details_url = hotel_detail.xpath('ul/li[2]/h2/a/@href').extract_first().strip()
                    hotel_details_url = 'https://hotels.ctrip.com' + hotel_details_url
                except Exception as e:
                    print('抓取酒店详情页错误： ' +str(e))
                    continue
                # '//*[@id="2036654"]/ul/li[2]/h2/a'
                try:
                    H_CLASSIFICATION = ''
                    H_star = hotel_detail.xpath('ul/li[2]/span/span[3]/@title').extract_first().strip()
                    if '豪华' in H_star:
                        H_CLASSIFICATION = '五星级'
                    elif '高档' in H_CLASSIFICATION:
                        H_CLASSIFICATION = '四星级'
                    elif '舒适' in H_CLASSIFICATION:
                        H_CLASSIFICATION = '三星级'
                    else:
                        H_CLASSIFICATION = '二星级及以下'
                except Exception as e:
                    H_CLASSIFICATION = '二星级及以下'
                    print('h_star  ',e)
                try:
                    H_NAME = hotel_detail.xpath('ul/li[2]/h2/a/@title').extract_first().strip()
                except Exception as e:
                    print('抓取酒店名称错误： ' +str(e))
                    continue
                # H_PRICE = hotel_detail.xpath('ul/li[3]/div[1]/div/div/a/span/text()').extract_first()
                # print('价格：',H_PRICE)
                # '//*[@id="2036654"]/ul/li[2]/h2/a/text()'
                # '//*[@id="2036654"]/ul/li[4]/div[1]/a/span[2]'
                try:
                    H_SCORE = round(float(hotel_detail.xpath('ul/li[4]/div[1]/a/span[2]/text()').extract_first().strip()),1)
                except Exception as e:
                    try:
                        H_SCORE = round(float(hotel_detail.xpath('ul/li[4]/div[1]/a/span[1]/text()').extract_first().strip()),1)
                    except Exception as e:
                        H_SCORE = 0.0
                        print('抓取酒店评分错误： ' +str(e))
                print('H_SCORE  :',H_SCORE)
                print('hotel_details_url   ',hotel_details_url)
                try:
                    H_COMMENT_NUMS = int(hotel_detail.xpath('ul/li[4]/div[1]/a/span[4]/span/text()').extract_first().strip())
                except Exception as e:
                    try:
                        H_COMMENT_NUMS = int(hotel_detail.xpath('ul/li[4]/div[1]/a/span[3]/span/text()').extract_first().strip())
                    except Exception as e:
                        H_COMMENT_NUMS = 0
                        print('抓取酒店评论数错误： ' + str(e))
                print('H_COMMENT_NUMS  :',H_COMMENT_NUMS)
                # H_PRICE = hotel_detail.xpath('ul/li[3]/div[1]/div/div[1]/span/text()').extract_first().strip()
                # print('H_PRICE  :',H_PRICE)
                try:
                    print('H_NAME   ' + str(H_NAME))
                except Exception as e:
                    print(None)
                print('city  ' + item['city'])
                # '//*[@id="643604"]/'
                # hotel_details_url = 'https://hotels.ctrip.com' + str(hotel_details_url)
                try:
                    item['url'] = hotel_details_url
                    item['H_NAME'] = H_NAME
                    item['H_SCORE'] = H_SCORE
                    item['H_COMMENT_NUMS'] = H_COMMENT_NUMS
                    item['H_CLASSIFICATION'] = H_CLASSIFICATION
                    yield item
                except Exception as e:
                    print('有一个没取出来' + str(e))




                # yield item
            except Exception as e:
                print('页面抓取错误：'+str(e))


