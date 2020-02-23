# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import copy
import pymysql

class WyyspiderPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root',password='',database='aaa',charset='utf8')
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        item = copy.deepcopy(item)
        # print(item)
        singer_name = item['singer_name']                                         # 歌手姓名
        singer_id = item['singer_id']                                             # 歌手id
        singer_image_url = item['singer_image_url']                               # 歌手照片url
        singer_description = item['singer_description']                           # 歌手描述
        single_message_pubDate = item['single_message_pubDate']                   # 歌手信息更新日期
        songs = str(item['songs'])                                                # 一个歌手的所有歌曲
        print(len(songs))
        a = '\"' + singer_name + '\",' +'\"' + singer_id + '\",' + '\"' + singer_image_url + '\",' + '\"' + singer_description + '\",' + '\"' + single_message_pubDate + '\",' + '\"' + songs + '\"'
        b = 'singer_name,singer_id,singer_image_url,singer_description,single_message_pubDate,songs'
        sql = 'insert into music({}) values({})'.format(b,a)
        try:
            x = self.cursor.execute(sql)
            self.conn.commit()
            print(x)
        except Exception as e:
            print(songs)
            print("mysql  " ,end='')
            print(e)

