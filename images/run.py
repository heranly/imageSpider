#encoding:utf-8
#time:2020/3/2 17:36
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
process = CrawlerProcess(get_project_settings())
process.crawl('baidu')
process.crawl('google')
process.crawl('vcg')
process.crawl('veer')
process.crawl('quanjing')
process.crawl('weibo')
process.start()

