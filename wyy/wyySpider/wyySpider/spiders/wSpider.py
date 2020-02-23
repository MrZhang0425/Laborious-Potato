# -*- coding: utf-8 -*-
import scrapy
import json
import copy

class WspiderSpider(scrapy.Spider):
    name = 'wSpider'
    # allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/#/discover/artist']

    # 根据分类的id, 抓取url
    def parse(self, response):
        for i in range(1001,1004):
            for j in range(65,91):
                page_url = 'https://music.163.com/discover/artist/cat?id={}&initial={}'.format(i,j)
                # page_url = 'https://music.163.com/artist?id=2116'
                yield scrapy.Request(
                    url= page_url,
                    callback = self.parse_page
                )

    # 抓取每个歌手的详情页面
    def parse_page(self,response):
        all_singer = response.xpath('//*[@id="m-artist-box"]//li')
        # singer1 = response.xpath('//ul[@id="m-artist-box"]//li[@class="sml"]')
        # singer2 = list(set(all_singer) - set(singer1))
        # print('singer1  ' + str(len(singer1)),end='     ')
        # print('singer2  ' + str(len(singer2)))
        for i in range(len(all_singer)):
        # for i in all_singer:
            item = {}
            singer_name = response.xpath('//*[@id="m-artist-box"]/li[{}]/a[1]/text()'.format(i+1)).extract_first()   # 歌手名称
            song_url = response.xpath('//*[@id="m-artist-box"]/li[{}]/a[1]/@href'.format(i+1)).extract_first()       # 歌手的所有歌曲url
            if singer_name == None:
                singer_name = response.xpath('//*[@id="m-artist-box"]/li[{}]/p/a/text()'.format(i+1)).extract_first()  # 歌手名称
                song_url = response.xpath('//*[@id="m-artist-box"]/li[{}]/p/a/@href'.format(i+1)).extract_first()      # 歌手的所有歌曲url
            #     print('name : ' + str(name) + '  ' + 'song_url : ' + str(song_url))
            item['singer_name'] = singer_name                                               # 歌手姓名
            item['singer_id'] = str(song_url.split("=")[1]).strip()                         # 歌手id
            page_url = 'https://music.163.com' + str(song_url).strip()                      # 歌手的所有歌曲url
            yield scrapy.Request(
                url=page_url,
                callback=self.parse_page2,
                meta={'item': item}
            )


    def parse_page2(self,response):
        item = copy.deepcopy(response.meta['item'])
        songs = response.xpath('//ul[@class="f-hide"][1]/li')
        li_songs = []
        for song in songs:
            single_song_message = []
            song_name = song.xpath('./a[1]/text()').extract_first().strip().replace('"', "").replace("'", "")  # 歌曲名称
            play_url = str(song.xpath('./a[1]/@href').extract_first()).strip()                                 # 播放链接
            song_id = str(play_url.split("=")[1]).strip()                                                      # 歌曲id
            play_url = 'https://music.163.com/#' + play_url                                                    # 完整的播放链接
            single_song_message.append(song_name)
            single_song_message.append(play_url)
            single_song_message.append(song_id)
            li_songs.append(single_song_message)
            # print('song_name : ' + str(song_name) + ' play_url : ' + str(play_url))
        print(li_songs)
        describe = response.xpath('//script[@type="application/ld+json"]/text()').extract_first()              # 歌手所有描述
        describe = json.loads(describe)
        singer_image_url = describe["images"][0]                                                               # 歌手图片url
        singer_description = describe["description"]                                                           # 歌手描述
        single_message_pubDate = describe["pubDate"]                                                           # 歌手信息更新时间
        # print(singer_image_url, singer_description, single_message_pubDate)
        item['singer_image_url'] = singer_image_url                                                            # 歌手图片url
        item['singer_description'] = singer_description                                                        # 歌手描述
        item['single_message_pubDate'] = single_message_pubDate                                                # 歌手信息更新时间
        item['songs'] = li_songs                                                                               # 歌手的所有歌曲
        print(item['singer_name'])
        yield item



