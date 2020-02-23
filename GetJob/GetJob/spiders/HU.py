# -*- coding: utf-8 -*-
import scrapy
import json
import time
import copy

class HuSpider(scrapy.Spider):
    name = 'HU'
    allowed_domains = ['scc.hnu.edu.cn','hnu.bysjy.com.cn']
    start_urls = ['http://hnu.bysjy.com.cn/module/getcareers?start_page=1&k=&panel_name=&type=inner&day=&count=15&start=1']

    def parse(self, response):
        # print('='*10 + 'parse')
        for page_num in range(1,50):
            page_url = 'http://hnu.bysjy.com.cn/module/getcareers?start_page=1&k=&panel_name=&type=inner&day=&count=15&start={}'.format(page_num)
            yield scrapy.Request(
                url= page_url,
                callback=self.parse_page
            )

    def parse_page(self,response):
        # print('='*10 + 'parse_page')
        text = response.body.decode()
        if len(text)>200:
            content = json.loads(text)
            li_page_content = content['data']
            for dict_single_content in li_page_content:
                item = {}
                item['school'] = '湖南大学'
                item['address'] = '湖南大学' + dict_single_content['address']
                url = 'http://scc.hnu.edu.cn/detail/career?id={}'.format(dict_single_content['career_talk_id'])
                item['city_name'] = dict_single_content['city_name']                        # 城市
                item['company_name'] = dict_single_content['company_name']                  # 公司名称
                item['company_property'] = dict_single_content['company_property']          # 公司类型
                item['industry_category']= dict_single_content['industry_category']        # 行业
                item['meet_time'] = time.strftime("%Y-%m-%d",time.strptime(str(dict_single_content['meet_day']), "%Y-%m-%d"))  # 招聘会时间
                item['professionals'] = dict_single_content['professionals']                # 招哪些专业
                item['view_count'] = dict_single_content['view_count']                      # 浏览量

                meet_time = time.strftime("%Y-%m-%d",time.strptime(str(dict_single_content['meet_day']), "%Y-%m-%d"))  # 将招聘会时间转换为指定格式
                ctime = time.strftime("%Y-%m-%d",time.localtime())                                                     # 当前时间转换为指定格式
                # 如果招聘会时间 > 当前时间
                if meet_time > ctime:
                    num = 0
                    keys = ['信息', '计算机', '软件', '网络']
                    # keys = ['动物','宠物','动医','动科','动物医学','动物科学']
                    for i in keys:
                        if i in dict_single_content['professionals']:
                            num += 1
                    if num > 0 :                                                             # 所招专业和计算机有关
                        yield scrapy.Request(
                            url=url,
                            callback=self.parse2,
                            meta={'item':item}
                        )

    def parse2(self,response):
        print(2)
        # print('='*10 + 'parse2')
        try:
            li_div = response.xpath('//div[@id="data_details"]/div[1]/div[1]/div[4]/div[contains(@class,"pub-list")][1]/div')
            for single_li in li_div:
                item = copy.deepcopy(response.meta['item'])
                item['post'] = single_li.xpath('./div[1]/p[1]/a[1]/text()').extract_first()               # 岗位
                major = single_li.xpath('./div[1]/p[2]/text()').extract_first().split('：')[1]    # 招聘专业
                item['major'] = major
                item['salary'] = single_li.xpath('./div[2]/text()').extract_first()                       # 薪水
                item['NumOfMan'] = single_li.xpath('./div[3]/p[1]/text()').extract_first()                # 招聘人数
                educationAndPlace = single_li.xpath('./div[3]/p[2]/text()').extract_first().split('|')
                item['education'] = educationAndPlace[0].replace(' ','')                                  # 学历
                item['work_place'] = educationAndPlace[1].replace(' ','')                                 # 工作地点
                detail_url1 = 'http://hnu.bysjy.com.cn' + single_li.xpath('./div[1]/p[1]/a[1]/@href').extract_first()
                item['detail_url'] = detail_url1
                num = 0
                # keys = ['动物','宠物','动医','动科','动物医学','动物科学']
                keys = ['信息', '计算机', '软件', '网络']

                for i in keys:
                    if i in major:
                        num += 1
                item['key_nums'] = num                                                   # 关键字数量
                if num > 0:
                    yield scrapy.Request(
                        url=detail_url1,
                        callback=self.parse3,
                        meta={'item':item}
                    )

        except Exception as e:
            print("parse2" + e)

    def parse3(self,response):
        # print('='*10 + 'parse3')
        item = copy.deepcopy(response.meta['item'])
        detail_url = response.url
        li_job_welfare = response.xpath('//div[@id="data_details"]/div[1]/div[1]/div[1]//*[@class="job-welfare"]')
        job_welfare = ''                                                               # 福利
        for single_job_welfare in li_job_welfare:
            job_welfare += single_job_welfare.xpath('./text()').extract_first()
            job_welfare += '  '
        item['job_welfare'] = job_welfare
        yield item





