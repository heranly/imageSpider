这是一个用于爬取图片的爬虫项目，收录的网站有：百度图片，google图片，全景，视觉中国，veer和微博图片。

使用： 再settings.py中设置要爬取的关键词，爬取页数和存储路径即可， 如 
#设置爬取关键词
KEYWORD = "美女" 
#设置爬取页数，每个渠道每页的不一样，百度每页:30张，google,quanjign,veer,vcg每页:100张，weibo每页:相册数*12张 
PAGE = 10 
#设置存储路径，图片最终路径：E:\图片\KEYWOED\xxx.jpg 
IMAGES_STORE = 'E:\图片'

如果对图片大小有要求可以在settings.py中设置过滤图片大小(单位是像素，默认最小值为0，即不过滤)
MIN_WIDTH = 0 
MIN_HEIGHT = 0

启动：
在settings.py中设置好参数后，选择你需要爬取的渠道，然后运行 run.py




