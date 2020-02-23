# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
from .settings import USER_AGENTS
from .settings import Proxies
import random
import time
from scrapy import signals


class HotelSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class HotelDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):

        if request.url:
            spider.browser.get(url=request.url)
            print(111)
            # more_btn = spider.browser.find_element_by_class_name("post_addmore")     # 更多按钮
            # print(more_btn)
            # js = "window.scrollTo(0,document.body.scrollHeight)"
            # spider.browser.execute_script(js)
            # if more_btn and request.url == "http://news.163.com/domestic/":
            #     more_btn.click()
            time.sleep(1)  # 等待加载,  可以用显示等待来优化.
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8",
                                request=request)  # 参数url指当前浏览器访问的url(通过current_url方法获取), 在这里参数url也可以用request.url
            # 参数body指要封装成符合HTTP协议的源数据, 后两个参数可有可无
        else:
            return HtmlResponse(url=request.url, status=500, request=request)  # 是原来的主页的响应对象

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class HotelProxyMiddleware(object):
    def process_request(self,request,spider):
        # 更换代理IP
        request.meta['proxy'] = random.choice(Proxies)


class SeleniumMiddleware(object):
    # def __init__(self):
    #     self.chrome_options = Options()
    #     self.chrome_options.add_argument('--headless')
    #     self.chrome_options.add_argument(random.choice(USER_AGENTS))
    #     self.chrome_options.add_argument('disable-infobars')
    #     self.driver = webdriver.Chrome(chrome_options=self.chrome_options)

    def process_request(self, request, spider):
        if request.url.startswith('https://hotels.ctrip.com/hotel'):
            print('以https://hotels.ctrip.com/开头了。。。')
            self.driver.get(request.url)
            time.sleep(3)
            print("访问{0}".format(request.url))
            if request.url.ednswith('html?isFull=F'):
                try:
                    # 页面一直循环，直到 id="myDynamicElement" 出现
                    print("xxxxxx")
                    element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="id_room_select_box"]'))
                    )
                except Exception as e:
                    print('未加载到价格HTML' + str(e))
                    self.driver.quit()
            print('yyyyyyy')
            html = self.driver.page_source
            response = scrapy.http.HtmlResponse(url=request.url,body=html,request=request,encoding='utf-8')
            self.driver.quit()
            return response



