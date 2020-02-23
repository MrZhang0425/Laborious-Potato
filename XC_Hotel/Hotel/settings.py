# -*- coding: utf-8 -*-
import random
# Scrapy settings for Hotel project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Hotel'

SPIDER_MODULES = ['Hotel.spiders']
NEWSPIDER_MODULE = 'Hotel.spiders'

LOG_LEVEL = 'WARNING'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; pl-PL; rv:1.0.1) Gecko/20021111 Chimera/0.6',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.8 (KHTML, like Gecko, Safari) Cheshire/1.0.UNOFFICIAL',
    'Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)'
]
USER_AGENT = random.choice(USER_AGENTS)

Proxies = ['http://112.80.76.15:8118',
'http://120.77.245.11:8080',
'http://47.95.249.140:8118',
'http://115.79.24.188:38702',
'http://125.71.212.13:9000',
'http://60.205.188.24:3128',
'http://183.129.244.16:13357',
'http://121.232.194.163:9000',
'http://47.102.101.218:8118',
'http://47.101.36.129:8118',
'http://47.106.124.179:80',
'http://42.159.91.248:8081',
'http://117.90.137.53:9000',
'http://183.166.125.48:9999',
'http://117.57.90.234:9999',
'http://49.235.69.138:8118',
'http://222.73.218.38:8888',
'http://47.104.172.108:8118',
'http://121.232.194.71:9000',
'http://1.197.203.199:9999',
'http://39.108.71.144:8000',
'http://47.107.37.228:8118',
'http://47.106.192.167:8000',
'http://136.228.128.6:51114',
'http://120.77.245.11:8080',
'http://182.101.207.11:8080',
'http://115.79.24.188:38702',
'http://139.199.19.174:8118',
'http://121.199.59.43:80',
'http://119.23.21.39:80',
'http://117.90.137.53:9000',
'http://61.150.96.27:36880',
'http://121.232.148.121:9000',
'http://125.110.116.74:9000',
'http://125.71.212.13:9000',
'http://136.228.128.6:51114',
'http://27.188.65.244:8060',
'http://183.129.244.16:13357',
'http://125.71.212.17:9000',
'http://120.79.184.148:8118',
'http://183.129.244.16:11834',
'http://183.129.244.16:11006',
'http://163.204.240.216:9999',
'http://183.129.244.16:13357',
'http://59.172.27.6:38380',
'http://47.107.69.175:8000',
'http://118.122.114.236:9000',
'http://144.123.70.176:9999',
'http://120.26.199.103:8118',
'http://60.217.73.238:8060',
'http://59.172.27.6:38380',
'http://202.109.157.65:9000',
'http://115.28.148.192:8118',
'http://139.196.22.147:80',
'http://27.188.65.244:8060',
'http://116.62.198.43:8080',
'http://39.96.210.247:80',
'http://47.95.249.140:8118',
'http://60.205.188.24:3128',
'http://47.107.190.212:8118',
'http://125.71.212.17:9000',
'http://47.101.36.129:8118',
'http://118.122.114.238:9000',
'http://111.11.100.13:8060',
'http://27.188.64.70:8060',
'http://60.13.42.124:9999',
'http://118.122.114.236:9000',
'http://47.107.190.212:8118',
'http://183.129.244.16:13357',
'http://58.16.7.37:33355',
'http://120.79.64.147:8118',
'http://47.106.192.167:8000',
'http://47.104.172.108:8118',
'http://121.232.148.178:9000',
'http://27.152.8.60:9999',
'http://47.104.75.226:8118',
'http://183.129.244.16:11389',
'http://42.159.91.248:8081',
'http://193.112.128.212:8118',
'http://60.173.241.77:8060',
'http://47.107.93.105:8000',
'http://182.101.207.11:8080',
'http://120.77.245.11:8080',
'http://113.12.202.50:50327',
'http://47.106.124.179:80',
'http://59.172.27.6:38380',
'http://219.157.86.141:8118',
'http://47.95.249.140:8118',
'http://183.166.125.48:9999',
'http://36.7.69.56:8060',
'http://60.205.188.24:3128']

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16
# DOWNLOAD_TIMEOUT = 10
# RETRY_ENABLED = False
# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    # 'Hotel.middlewares.HotelDownloaderMiddleware': 543,
    'Hotel.middlewares.HotelProxyMiddleware': 543,
    # 'Hotel.middlewares.SeleniumMiddleware': 302,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARS = {
#    'Hotel.middlewares.SeleniumMiddleware':1,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Hotel.pipelines.HotelPipeline': 300,
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to

# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
