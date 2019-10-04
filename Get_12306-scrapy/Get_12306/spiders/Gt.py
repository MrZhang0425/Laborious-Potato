# -*- coding: utf-8 -*-
import scrapy
import re
import csv
import os
import urllib
import json

class GtSpider(scrapy.Spider):
    name = 'Gt'
    allowed_domains = ['12306.cn']
    start_urls = ['https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9112']
    start_station = "怀化"
    end_station = "长沙"
    departure_time = "2019-10-04"

    # 查找站名对应的代号
    def parse(self, response):
        if not os.path.exists("sation_info.csv"):
            text = response.body.decode()
            sation_content = re.split(r"@\w+\|", text)
            li_simple_name = []
            for i in sation_content:
                li_simple_name.append(i.split("|"))

            # 写入csv
            # 弹出列表第一个元素“var station_names =”
            li_simple_name.pop(0)
            # 最后一个元素进行处理“|株洲南|KVQ|zhuzhounan|zzn|2874';”，去点符号";”"
            li_simple_name[-1][-1] =li_simple_name[-1][-1] = re.match("\d+",li_simple_name[-1][-1])[0]
            # 写入csv
            with open('station_info.csv','w',encoding='utf-8',newline='') as f:
                csv_write = csv.writer(f)
                csv_write.writerow(["站名","代号","拼音","简写","序号"])
                csv_write.writerows(li_simple_name)
        else:
            pass
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse_url
        )


    def parse_url(self,response):
        # print("1"*100 + str(response.request.headers["User-Agent"]))
        start = "None"
        end = "None"
        # 查询起始站和终点站对应的代号
        with open("E:\爬虫代码\Get_12306\station_info.csv", "r", encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                try:
                    if row[0] == self.start_station:
                        start = row[1]
                    elif row[0] == self.end_station:
                        end = row[1]
                except Exception as e:
                    pass
            print("起始站代号为" + start +",终点站代号为" + end)

        if start!= "None" and end!="None":
            # start_station = urllib.quote(self.start_station)
            # end_station = urllib.quote(self.end_station)
            # a = start_station + "," +start
            # b = end_station + ","+end
            # c = self.departure_time
            c = self.departure_time
            dest_url = "https://kyfw.12306.cn/otn/leftTicket/queryA?" \
                       "leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&" \
                       "purpose_codes=ADULT".format(c,start,end)
            # print("2" * 20)
            # print(dest_url)
            headers = {
                "Host": "kyfw.12306.cn",
                "Accept":  "*/*",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Referer": "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E6%80%80%E5%8C%96,HHQ&ts=%E9%95%BF%E6%B2%99,CSQ&date=2019-10-01&flag=N,N,Y",
                "Cookie":"JSESSIONID=A193477BEFAAAD974271EE6D91037557; RAIL_EXPIRATION=1570223464791; RAIL_DEVICEID=CtCNiKTt-apDgKJ3fPc3uvi0Yqjz7gQBrHZgfMkwU52aBbIs1YI-bwCyNJsgBoEQouMYrk_oTSvygyAaMbY-7WpEsce_z1YGqJ8972xp2kM8CHjXtYsl_iOX0U2DcTN8PWj-LqmirmcdGEhxKkOKlL6ZIjSQP3Kw; BIGipServerotn=133169674.24610.0000; BIGipServerpool_passport=267190794.50215.0000; route=9036359bb8a8a461c164a04f8f50b252; _jc_save_fromStation=%u6000%u5316%2CHHQ; _jc_save_toStation=%u957F%u6C99%2CCSQ; _jc_save_fromDate=2019-10-01; _jc_save_toDate=2019-10-01; _jc_save_wfdc_flag=dc",
                        "Host": "kyfw.12306.cn"
            }
            cookie_dict = {}
            cookie = 'JSESSIONID=A193477BEFAAAD974271EE6D91037557; RAIL_EXPIRATION=1570223464791; RAIL_DEVICEID=CtCNiKTt-apDgKJ3fPc3uvi0Yqjz7gQBrHZgfMkwU52aBbIs1YI-bwCyNJsgBoEQouMYrk_oTSvygyAaMbY-7WpEsce_z1YGqJ8972xp2kM8CHjXtYsl_iOX0U2DcTN8PWj-LqmirmcdGEhxKkOKlL6ZIjSQP3Kw; BIGipServerotn=133169674.24610.0000; BIGipServerpool_passport=267190794.50215.0000; route=9036359bb8a8a461c164a04f8f50b252; _jc_save_fromStation=%u6000%u5316%2CHHQ; _jc_save_toStation=%u957F%u6C99%2CCSQ; _jc_save_fromDate=2019-10-01; _jc_save_toDate=2019-10-01; _jc_save_wfdc_flag=dc'
            for i in cookie.split('; '):
                cookie_dict[i.split('=')[0]] = i.split('=')[1]  # ，设置为字典格式
            yield scrapy.Request(dest_url, callback=self.parse_info, cookies=cookie_dict, dont_filter=True)



    # def parse(self,response):
    #     yield scrapy.Request(
    #         url=dest_url,
    #         headers=headers,
    #         callback=self.parse_info
    #     )
    def parse_info(self, response):
        item = {}
        # print("3"*20)
        # print(response.url)
        # print(response.request.headers["User-Agent"])
        # print(response.body.decode())

        # 将response的内容转为字典
        dict_resp = json.loads(response.body.decode())
        li_info = dict_resp["data"]["result"]
        # print(li_info)
        li_all_content = []
        # 数据处理，对应到各种座位的余票
        for i in li_info:
            li_single_info = []
            li_single_content = i.split("|")
            # print(li_single_content[3])
            checi = li_single_content[3]
            qidianzhan = li_single_content[4]
            zhongdianzhan = li_single_content[5]
            chufazhan = li_single_content[6]
            daodazhan = li_single_content[7]
            chufashijian = li_single_content[8]
            daodashijian = li_single_content[9]
            lishi = li_single_content[10]
            tedengzuo = li_single_content[33]
            yidengzuo = li_single_content[32]
            erdengzuo = li_single_content[31]
            gaojiruanwo = li_single_content[21]
            ruanwo = li_single_content[23]
            dongwo = li_single_content[30]
            yingwo = li_single_content[28]
            ruanzuo = li_single_content[27]
            yingzuo = li_single_content[29]
            wuzuo = li_single_content[26]
            shifouyoupiao = li_single_content[11]
            if shifouyoupiao == 'IS_TIME_NOT_BUY':
                shifouyoupiao = '列车停运'
            with open("E:\爬虫代码\Get_12306\station_info.csv", "r", encoding='utf-8') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    try:
                        if qidianzhan != chufazhan and zhongdianzhan != daodazhan:
                            if row[1] == qidianzhan:
                                qidianzhan = row[0]
                            elif row[1] == zhongdianzhan:
                                zhongdianzhan = row[0]
                            elif row[1] == chufazhan:
                                chufazhan = row[0]
                            elif row[1] == daodazhan:
                                daodazhan = row[0]
                        elif qidianzhan == chufazhan and zhongdianzhan != daodazhan:
                            if row[1] == qidianzhan:
                                qidianzhan = row[0]
                                chufazhan = qidianzhan
                            elif row[1] == zhongdianzhan:
                                zhongdianzhan = row[0]
                            elif row[1] == daodazhan:
                                daodazhan = row[0]
                        elif qidianzhan != chufazhan and zhongdianzhan == daodazhan:
                            if row[1] == qidianzhan:
                                qidianzhan = row[0]
                            elif row[1] == zhongdianzhan:
                                zhongdianzhan = row[0]
                                daodazhan = zhongdianzhan
                            elif row[1] == chufazhan:
                                chufazhan = row[0]
                        elif qidianzhan == chufazhan and zhongdianzhan == daodazhan:
                            if row[1] == qidianzhan:
                                qidianzhan = row[0]
                                chufazhan =qidianzhan
                            elif row[1] == zhongdianzhan:
                                zhongdianzhan = row[0]
                                daodazhan = zhongdianzhan
                    except Exception as e:
                        pass
            li_single_info.append(checi)
            li_single_info.append(qidianzhan)
            li_single_info.append(zhongdianzhan)
            li_single_info.append(chufazhan)
            li_single_info.append(daodazhan)
            li_single_info.append(chufashijian)
            li_single_info.append(daodashijian)
            li_single_info.append(lishi)
            li_single_info.append(tedengzuo)
            li_single_info.append(yidengzuo)
            li_single_info.append(erdengzuo)
            li_single_info.append(gaojiruanwo)
            li_single_info.append(ruanwo)
            li_single_info.append(dongwo)
            li_single_info.append(yingwo)
            li_single_info.append(ruanzuo)
            li_single_info.append(yingzuo)
            li_single_info.append(wuzuo)
            li_single_info.append(shifouyoupiao)
            li_all_content.append(li_single_info)
        # return到pipelines.py进行数据的保存
        item["li_all_content"] = li_all_content
        yield item



        # print(li_all_content[2][3])