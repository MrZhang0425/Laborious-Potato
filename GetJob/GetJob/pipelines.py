# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import copy
import pymysql
import time
import datetime

class GetjobPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='',db='Hunan_University',charset='utf8')
        self.cursor = self.conn.cursor()
        sqla = 'drop table if exists HNU;'
        sqlb = "create table HNU(id int not null primary key auto_increment," \
               "school varchar(30) not null comment '学校名称'," \
               "address varchar(30) not null comment '宣讲会地址'," \
               "company_city varchar(20) not null comment '公司所在城市'," \
               "company_name varchar(30) not null comment '公司名称'," \
               "company_property varchar(30) not null comment '公司类型'," \
               "industry_category varchar(30) not null comment '公司所在行业'," \
               "meet_time varchar(300) not null comment '宣讲会时间'," \
               "professionals varchar(500) not null comment '整个公司的招聘专业'," \
               "view_count varchar(10) not null comment '浏览量'," \
               "post varchar(30) not null comment '岗位'," \
               "major varchar(300) not null comment '职位所需专业'," \
               "salary varchar(30) not null comment '薪水'," \
               "NumOfMan varchar(30) not null comment '招聘人数'," \
               "education varchar(30) not null comment '学历'," \
               "work_place varchar(30) not null comment '工作地点'," \
               "detail_url varchar(300) not null comment '详情页url'," \
               "key_nums varchar(10) not null comment '关键字出现次数共四个'," \
               "job_welfare varchar(300) not null comment '福利');"
        self.cursor.execute(sqla)
        self.cursor.execute(sqlb)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()



    def process_item(self, item, spider):
        conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='',db='Hunan_University',charset='utf8')
        cursor = conn.cursor()
        item = copy.deepcopy(item)
        school = item['school']
        address = item['address']
        company_city = item['city_name']
        company_name = item['company_name']
        company_property = item['company_property']
        industry_category = item['industry_category']
        meet_time = item['meet_time']
        # meet_time = ''
        # for i in stime.split('-'):
        #     meet_time += i
        # meet_time = datetime.datetime.strptime(meet_time,'%Y%m%d').date()
        professionals = item['professionals']
        view_count = item['view_count']
        post = item['post']
        major = item['major']
        salary = item['salary']
        NumOfMan = item['NumOfMan']
        education = item['education']
        work_place = item['work_place']
        detail_url = item['detail_url']
        key_nums = item['key_nums']
        job_welfare = item['job_welfare']
        print(meet_time)
        a = '"' + school + '",' +'"' + address + '",' + '"' + company_city + '",' + '"' + company_name + '",' + '"' + company_property + '",' + '"' + industry_category + '",' \
             + '"'+ meet_time + '",' + '"' + professionals + '",'  + view_count + ',' + '"' + post + '",' + '"' + major + '",' + '"' + salary + '",' \
            + '"' + NumOfMan + '",' + '"' + education + '",' + '"' + work_place + '",' +  '"' + detail_url +'",'+ str(key_nums) + ','+ '"' + job_welfare + '"'

        b = 'school,address,company_city,company_name,company_property,industry_category,meet_time,professionals,view_count,post,major,salary,NumOfMan,education,work_place,detail_url,key_nums,job_welfare'

        sql = 'insert into HNU({}) values({})'.format(b,a)

        # print(sql)
        try:
            x = cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            print(x)
        except Exception as e:
            print("mysql  " ,end='')
            print(e)
        # print(item['company_name']+item['post']+item['detail_url'])
        # print(item['meet_time'])
        # print(type(item['meet_time']))





