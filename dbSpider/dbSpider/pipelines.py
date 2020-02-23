# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import copy

class DbspiderPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root',password='',database='aaa',charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # if spider.name == 'dSpider':
        #     item = copy.deepcopy(item)
        #     singer_url = item['singer_url']
        #     singer_name = item['singer_name']
        #     singer_id = item['singer_id']
        #     tags = item['tags']
        #     a = '\"' + singer_url + '\",' +'\"' + singer_name + '\",' + '\"' + singer_id + '\",' + '\"' + tags + '\"'
        #     b = 'singer_url,singer_name,singer_id,tags'
        #     sql = 'insert into dmusic({}) values({})'.format(b,a)
        #     try:
        #         x = self.cursor.execute(sql)
        #         self.conn.commit()
        #         print(x)
        #     except Exception as e:
        #         print(singer_url)
        #         print("mysql  " ,end='')
        #         print(e)

        # if spider.name == 'dSpider2':
        item = copy.deepcopy(item)

        singer_id = item['singer_id']                # 歌手id
        singer_name = item['singer_name']            # 歌手名称
        music_img = item['music_img']                # 歌曲图片url
        music_name = item['music_name']              # 歌曲名称
        music_name2 = item['music_name2']            # 歌曲名称2
        pubDate = item['pubDate']                    # 发行时间
        music_cat = item['music_cat']                # 歌曲分类
        storage_medium = item['storage_medium']      # 存储介质
        music_type = item['music_type']              # 歌曲类型
        music_mark = item['music_mark']              # 歌曲评分
        comment_num = item['comment_num']            # 评论数量
        comment_url = item['comment_url']            # 评论的url
        music_id = str(item['music_id'])                  # 歌曲id
        # a = '\"' + singer_id + '\",' + '\"' + singer_name + '\",' + '\"' + music_img + \
        #     '\",' + '\"' + music_name + '\",' + '\"' + music_name2 + '\",' + '\"' + pubDate + \
        #     '\",' + '\"' + music_cat + '\",' + '\"' + storage_medium + \
        #     '\",' + '\"' + music_type + '\",' + '\"' + music_mark + '\",' + '\"' + comment_num +\
        #     '\",' + '\"' + music_id + '\",' + '\"' + comment_url + '\"'

        # print(a)
        #
        # b =

        sql = 'insert into dmusic2(singer_id,singer_name,music_img,music_name,music_name2,pubDate,music_cat,storage_medium' \
            ',music_type,music_mark,comment_num,music_id,comment_url) ' \
              'values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'

        try:
            x = self.cursor.execute(sql, (singer_id, singer_name, music_img, music_name, music_name2, pubDate, music_cat,
                                          storage_medium, music_type, music_mark, comment_num, music_id, comment_url))
            self.conn.commit()
            print(x)
        except Exception as e:
            print("mysql  " ,end='')
            print(e)
