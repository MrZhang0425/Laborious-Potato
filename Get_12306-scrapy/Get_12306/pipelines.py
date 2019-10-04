# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import copy
import csv

class Get12306Pipeline(object):
    def process_item(self, item, spider):
        item = copy.deepcopy(item)
        with open('vehicle_info.csv', 'w', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(["车次", "起始站", "终点站", "出发站", "到达站", "出发时间", "到达时间", "历史", "商务特等座",
                                "一等座", "二等座", "高级软卧", "软卧", "动卧", "硬卧", "软座", "硬座", "无座", "是否有票"])
            print(1)
            csv_write.writerows(item['li_all_content'])

