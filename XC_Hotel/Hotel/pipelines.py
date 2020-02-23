# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import copy
import pymysql

class HotelPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='demo', charset='utf8')
        self.cursor = self.conn.cursor()
        # sql2 = 'insert into url values(0,"1",0)'
        sqll = 'UPDATE hotel SET DEL_FLAG=1'
        self.cursor.execute(sqll)
        # self.cursor.execute(sql2)


    def process_item(self, item, spider):
        item = copy.deepcopy(item)
        H_NAME = item['H_NAME']
        hotel_details_url = item['url']
        H_SCORE =item['H_SCORE']
        H_COMMENT_NUMS =item['H_COMMENT_NUMS']
        H_CLASSIFICATION =item['H_CLASSIFICATION']
        city = item['city']
        SQL = 'insert into url_bak(H_NAME,hotel_details_url,h_score,h_comment_num,H_CLASSIFICATION,city) ' \
              'values ("{}","{}","{}","{}","{}","{}")'.format(H_NAME,hotel_details_url,H_SCORE,H_COMMENT_NUMS,H_CLASSIFICATION,city)
        self.cursor.execute(SQL)
        self.conn.commit()


        # item = copy.deepcopy(item)
        # H_NAME=item['H_NAME']
        # H_ADDRESS=item['H_ADDRESS']
        # PROVINCES=item['PROVINCES']
        # CITY=item['CITY']
        # COUNTY=item['COUNTY']
        # B_CIRCLE=item['B_CIRCLE']
        # H_CLASSIFICATION=item['H_CLASSIFICATION']
        # ROOM_NUM=item['ROOM_NUM']
        # MAX_PRICE=item['MAX_PRICE']
        # MIN_PRICE=item['MIN_PRICE']
        # AVG_PRICE=item['AVG_PRICE']
        # QUERY_DATE=item['QUERY_DATE']
        # DEL_FLAG = 0
        # QUERY_WEBSITE = '携程'
        # sql = 'insert into hotel(H_NAME,H_ADDRESS,PROVINCES,CITY,COUNTY,B_CIRCLE,H_CLASSIFICATION,ROOM_NAME,MAX_PRICE,MIN_PRICE,AVG_PRICE,QUERY_WEBSITE,QUERY_DATE,DEL_FLAG) ' \
        #       'values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'\
        #     .format(H_NAME,H_ADDRESS,PROVINCES,CITY,COUNTY,B_CIRCLE,H_CLASSIFICATION,ROOM_NUM,MAX_PRICE,MIN_PRICE,AVG_PRICE,QUERY_WEBSITE,QUERY_DATE,DEL_FLAG)
        # x = self.cursor.execute(sql)
        # print('执行插入结果'+ str(x))
        # self.conn.commit()

    def __del__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
