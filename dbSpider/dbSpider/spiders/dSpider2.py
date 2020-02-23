# -*- coding: utf-8 -*-
import scrapy
import copy
import pymysql

class Dspider2Spider(scrapy.Spider):
    print(1)
    name = 'dSpider2'
    allowed_domains = ['music.douban.com']
    start_urls = ['http://www.baidu.com']
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='aaa', charset='utf8')
    cursor = conn.cursor()
    Cookie = 'bid=g9qgUthd58I; douban-fav-remind=1; __gads=ID=30525610039f8bce:T=1570513938:S=ALNI_MZVx-vLiUI3fSY1qdPw2w9cEFtRRA; Hm_lvt_cfafef0aa0076ffb1a7838fd772f844d=1578118870; __yadk_uid=cpT8u87Vp75JYnnFRavYpuG37t1vpOLd; _vwo_uuid_v2=DA966EBE49EFF5669923180391A566AD8|db13a8c673fa264c771b6d02f40e5257; ct=y; __utma=266659602.1500660917.1581770763.1581770763.1581770763.1; __utmz=266659602.1581770763.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); push_noty_num=0; push_doumail_num=0; __utmv=30149280.15815; __utmz=30149280.1581938348.13.10.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; viewed="1427374_34914897_34924663_6787307_26022656_1407700_6900548"; _pk_ref.100001.afe6=%5B%22%22%2C%22%22%2C1582005396%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DFQ3UNHP-v5_FVWdiJdi-2ucZa1jQBZgvRgzO29Yt9Px7GVqYsLesMlqpmslxNYwJ%26wd%3D%26eqid%3Dc05b1a2b000451bc000000055e4a76a7%22%5D; _pk_ses.100001.afe6=*; ap_v=0,6.0; __utma=30149280.503293982.1578120001.1581995440.1582005396.16; __utmc=30149280; dbcl2="158151478:t/QGmRKMfws"; _pk_id.100001.afe6=b714719514b526ba.1578118841.15.1582008022.1581995441.; __utmt=1; __utmb=30149280.6.10.1582005396; ck=wRoW'
    coolies = dict(i.split('=', 1) for i in Cookie.split(';'))
    print(coolies)
    def parse(self, response):
        print(111)
        sql = 'select singer_id, singer_name, singer_url from dmusic'
        zzz = self.cursor.execute(sql)
        print(zzz)
        y = self.cursor.fetchone()

        while y is not None:
            item = {}
            item['singer_id'] = y[0]
            item['singer_name'] = y[1]
            singer_url = y[2]
            item['singer_url'] = singer_url
            print(y[0], '   ', singer_url)                              # 歌手id
            y = self.cursor.fetchone()
            yield scrapy.Request(
                url=singer_url,
                callback=self.parse_page,
                meta={'item': item},
                dont_filter=True
            )
            y = self.cursor.fetchone()

    def parse_page(self, response):
        item = copy.deepcopy(response.meta['item'])
        # 先获得最大页
        max_page = response.xpath('//*[@id="subject_list"]/div[22]/a')
        x = 1                                                 # 最大页
        for i in max_page:
            num = i.xpath('./text()').extract_first()
            if num:
                num = int(num.strip())
                if num > x :
                    x = num
        print('max_page is : ',x, '    ', item['singer_url'])

        # 生成request
        page_num = 0
        max_page_num = (x-1)*20
        while page_num <= max_page_num:
            url = item['singer_url'] + '?start={}&type=T'.format(page_num)
            yield scrapy.Request(
                url=url,
                callback=self.parse_page2,
                meta={'item': item},
                dont_filter=True
            )
            page_num += 20

    def parse_page2(self, response):
        # print(response.body.decode())
        all_music = response.xpath('//*[@id="subject_list"]/table')
        print(len(all_music))
        for i in all_music:
            item = copy.deepcopy(response.meta['item'])
            try:
                music_img = i.xpath('./tr/td[1]/a[1]/img[1]/@src').extract_first()
            except Exception as e:
                music_img = '无图片'
                print('===========music_img================  ', str(e))
            try:
                music_name = i.xpath('./tr/td[2]/div[1]/a/text()').extract_first().strip()
            except Exception as e:
                music_name = '无歌曲名称'
                print('----------------music_name------------------------------',music_name)
            try:
                music_name2 = i.xpath('./tr/td[2]/div[1]/a[1]/span/text()').extract_first()
            except Exception as e:
                music_name2 = '无别名'
                print('====---====-music_name2---=--=-=-=-==  ', music_name2)
                # '//*[@id="subject_list"]/table[3]/tbody/tr/td[2]/div/p'

            try:
                music_message = i.xpath('./tr/td[2]/div/p/text()').extract_first()
                li_message = music_message.split('/')
                if len(li_message) == 3:
                    singer = li_message[0].strip()
                    pubDate = li_message[1].strip()
                    music_cat = '无'
                    storage_medium = li_message[2].strip()
                    music_type = '无'

                elif len(li_message) == 2:
                    singer = li_message[0].strip()
                    pubDate = li_message[1].strip()
                    music_cat = '无'
                    storage_medium = '无'
                    music_type = '无'

                elif len(li_message) == 1:
                    singer = li_message[0].strip()
                    pubDate = '无'
                    music_cat = '无'
                    storage_medium = '无'
                    music_type = '无'

                elif len(li_message) == 4:
                    singer = li_message[0].strip()
                    pubDate = li_message[1].strip()
                    music_cat = li_message[2].strip()
                    storage_medium = li_message[3].strip()
                    music_type = '无'

                elif len(li_message) == 5:
                    singer = li_message[0].strip()
                    pubDate = li_message[1].strip()
                    music_cat = li_message[2].strip()
                    storage_medium = li_message[3].strip()
                    music_type = li_message[4].strip()

                else:
                    singer = '无'
                    pubDate = '无'
                    music_cat = '无'
                    storage_medium = '无'
                    music_type = '无'

            except Exception as e:
                music_message = '无音乐信息'
                singer = '无'
                pubDate = '无'
                music_cat = '无'
                storage_medium = '无'
                music_type = '无'
                print('===========music_message================  ', str(e))

            try:
                music_mark = i.xpath('./tr/td[2]/div/div/span[2]/text()').extract_first()
                if music_mark == None:
                    music_mark = '无评分'

            except Exception as e:
                music_mark = '无评分'
                print('===========music_mark================  ', str(e))

            try:
                comment_num = i.xpath('./tr/td[2]/div/div/span[3]/text()').extract_first()
                if comment_num == None:
                    comment_num = '少于10人评价'
                else:
                    comment_num = comment_num.replace('/n', '').replace(' ', '')

            except Exception as e:
                comment_num = '少于10人评价'
                print(response.request.url,'===========comment_num================  ', str(e))

            try:
                comment_url = i.xpath('./tr/td[2]/div/a/@href').extract_first()
                music_id = comment_url.split('/')[-2]
            except Exception as e:
                comment_url = '无'
                music_id = '无'
                print('===========comment_url================  ', str(e))
            print('music_id  ' ,music_id)
            item['music_img'] = music_img                # 歌曲图片url
            item['music_name'] = music_name              # 歌曲名称
            item['music_name2'] = music_name2            # 歌曲名称2
            # item['singer'] = singer                      # 歌手名称
            item['pubDate'] = pubDate                    # 发行时间
            item['music_cat'] = music_cat                # 歌曲分类
            item['storage_medium'] = storage_medium      # 存储介质
            item['music_type'] = music_type              # 歌曲类型
            item['music_mark'] = str(music_mark)              # 歌曲评分
            item['comment_num'] = str(comment_num)            # 评论数量
            item['comment_url'] = comment_url            # 评论的url
            item['music_id'] = str(music_id)                  # 歌曲id
            yield item





