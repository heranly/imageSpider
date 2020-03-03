# -*- coding: utf-8 -*-

# Scrapy settings for images project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'images'

SPIDER_MODULES = ['images.spiders']
NEWSPIDER_MODULE = 'images.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
    # "X-Requested-With": "XMLHttpRequest",
}
VEER_COOKIES = {
    "koa.sid":"6dqy7jDevvc3aIit5400lOC2YRTfv_tQ",
    "koa.sid.sig":"FzjnQ60L8D0ZS7195g93ZCVO4qw",
    "_ga":"GA1.2.1150420497.1583154885",
    "_gid":"GA1.2.2035731319.1583154885",
    "sajssdk_2015_cross_new_user":"1",
    "sensorsdata2015jssdkcross":"%7B%22distinct_id%22%3A%221709b6273d75d-0d58c5a1014a38-5f4e2917-2073600-1709b6273d88c8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.veer.com%2F%22%7D%2C%22%24device_id%22%3A%221709b6273d75d-0d58c5a1014a38-5f4e2917-2073600-1709b6273d88c8%22%7D",
    "Hm_lvt_f2de34005a64c75f44715498bcb136f9":"1583154887",
    "_gat_gtag_UA_103598720_1":"1",
    "_gat":"1",
    "Hm_lpvt_f2de34005a64c75f44715498bcb136f9":"1583154985",
    "_fp_":"eyJpcCI6IjExNS4yMzYuMTE5LjE0MyIsImZwIjoiODI5ODA4NzI2OTZkZmVkNmEyOTkzZjM5MjFhY2ExZTEiLCJocyI6IiQyYSQwOCR3TWFneHdVQlF3SjlyY1lRVDVYN1hPSnkxZmhqd0pHN1h1L0ZsWXJ5Y21JQUdIVmk3MTFGYSJ9"
    }


QUANJING_HEADERS = {
    "Accept":"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
    "Connection":"keep-alive",
    "Host":"www.quanjing.com",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-origin",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
    }


WEIBO_COOKIES = {
    "SCF":"AnNm9lCKWql6NGbBWSXAWnl8vEB8hZTNIRE3Rn0EUB6JvmoqGzCBxksgLqxpwKNU4RD7EKLtAsV4dwvjA79p-24.",
    "_T_WM":"623893e879f529d917a7525cd16a7bc0",
    "SUB":"_2A25zWc8NDeRhGeBK6FYS-S3JzjSIHXVQpdFFrDV6PUJbkdAKLW3fkW1NR9gO8qDMLSZz9SRNufwWTbmkiKFqcBvr",
    "SUHB":"08J7wZXyA0M_WJ",
    "SSOLoginState":"1583202141"
}

WEIBO_HEADERS = {
# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
# "Accept-Encoding":"gzip, deflate, br",
# "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
# "Cache-Control":"max-age=0",
# "Connection":"keep-alive",
# "Content-Length":"43",
# "Content-Type":"application/x-www-form-urlencoded",
# # "Cookie":"SCF=AnNm9lCKWql6NGbBWSXAWnl8vEB8hZTNIRE3Rn0EUB6JvmoqGzCBxksgLqxpwKNU4RD7EKLtAsV4dwvjA79p-24.; _T_WM=623893e879f529d917a7525cd16a7bc0; SUB=_2A25zWc8NDeRhGeBK6FYS-S3JzjSIHXVQpdFFrDV6PUJbkdAKLW3fkW1NR9gO8qDMLSZz9SRNufwWTbmkiKFqcBvr; SUHB=08J7wZXyA0M_WJ; SSOLoginState=1583202141",
# "Host":"weibo.cn",
# "Origin":"https://weibo.cn",
# # "Referer":"https://weibo.cn/find/?tf=5_007",
# "Sec-Fetch-Mode":"navigate",
# "Sec-Fetch-Site":"same-origin",
# "Sec-Fetch-User":"?1",
# "Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
}






RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 45
IMAGES_EXPIRES = 90  #90天内抓取的都不会被重抓

MIN_WIDTH = 0
MIN_HEIGHT = 0



# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'images.middlewares.ImagesSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'images.middlewares.ImagesDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'images.pipelines.MyImagesPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



#以下是要爬取的配置信息
#爬取的关键词
KEYWORD = "美女"
#爬取页数，每个渠道每页的不一样，百度每页:30张，google,quanjign,veer,vcg每页:100张，weibo每页:相册数*12张
PAGE = 10
#存储路径，图片最终路径：E:\图片\KEYWOED\xxx.jpg
IMAGES_STORE = 'E:\图片'













