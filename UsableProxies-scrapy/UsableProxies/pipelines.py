import copy
import csv
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class UsableproxiesPipeline(object):
    def process_item(self, item, spider):
        with open("proxies.csv", "a") as f:
            csv_write = csv.writer(f)
            ipitem = copy.deepcopy(item)
            ips = ipitem["page"]
            csv_write.writerow(ips)
            f.close()
            return "over!!!"
