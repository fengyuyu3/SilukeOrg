# -*- coding: utf-8 -*-

# Scrapy settings for SilukeOrg project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'SilukeOrg'

SPIDER_MODULES = ['SilukeOrg.spiders']
NEWSPIDER_MODULE = 'SilukeOrg.spiders'
RETRY_TIMES = 10
RETRY_HTTP_CODES = [443, 8118, 808, 53281, 8123, 8888, 80, 500, 503, 504, 400, 403, 404, 408, 53281, 3128, 51552, 81, 65309, 55555]
PROXY_LIST = os.path.dirname(os.path.abspath(__file__))+"\list.txt"
PROXY_MODE = 0

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'SilukeOrg (+http://www.yourdomain.com)'
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
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
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'SilukeOrg.middlewares.SilukeorgSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'SilukeOrg.middlewares.SilukeorgSpiderMiddleware': 543,
   # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'SilukeOrg.middlewares.RandomUserAgentMiddlware': 545,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   # 'scrapy.downloadermiddlewares.useragent.HttpProxyMiddleware': None,
   'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
   'scrapy_proxies.RandomProxy': 100,
   'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'SilukeOrg.pipelines.SilukeorgPipeline': 301,
   # 'SilukeOrg.pipelines.SilukeorgMySqlPipline': 300,
   'scrapy_redis.pipelines.RedisPipeline': 200
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'xici'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'

SQL_DATETIME_FORMAT = "%Y-%m-%d %H:%M"