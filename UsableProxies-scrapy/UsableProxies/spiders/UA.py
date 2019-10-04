# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from UsableProxies.settings import num

class UaSpider(CrawlSpider):
    name = 'UA'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']

    # item = {}

    rules = (
        Rule(LinkExtractor(allow=r'free/inha/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        ips = []
        results = response.xpath('/html/body/div/div[4]/div[2]/div/div[2]/table/tbody/tr')
        for result in results:
            print(response.url)
            ip = (result.xpath('./td[4]/text()').extract_first()).lower() + "://" + result.xpath('./td[1]/text()').extract_first() \
                 + ":"+ result.xpath('./td[2]/text()').extract_first()
            print(ip)
            ips.append(ip)
        item["page"] = ips
        yield item
