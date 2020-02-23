# -*- coding: utf-8 -*-
import scrapy
import copy

class DspiderSpider(scrapy.Spider):
    name = 'dSpider'
    allowed_domains = ['music.douban.com']
    start_urls = ['https://music.douban.com/tag/']

    def parse(self, response):
        x = response.xpath('//*[@id="艺术家"]/div[2]/table/tbody/tr')
        for i in x:
            y = x.xpath('./td')
            for j in y:
                item = {}
                singer_url = 'https://music.douban.com' + j.xpath('./a[1]/@href').extract_first()
                # print(singer_url)
                singer_name = j.xpath('./a[1]/text()').extract_first()
                singer_id = j.xpath('./b[1]/text()').extract_first().replace('(', '').replace(')', '')
                item['singer_url'] = singer_url
                item['singer_name'] = singer_name
                item['singer_id'] = singer_id

                yield scrapy.Request(
                    url= singer_url,
                    callback = self.parse_page,
                    meta = {'item':item}
                )

    def parse_page(self,response):
        item = copy.deepcopy(response.meta['item'])
        x = response.xpath('//*[@id="content"]/div/div[2]/div[2]/a')
        li_tag = []
        for i in x:
            tag = i.xpath('./text()').extract_first().replace(' ','').replace("'",'').replace('"','')
            li_tag.append(tag)
        item['tags'] = str(li_tag)
        yield item
