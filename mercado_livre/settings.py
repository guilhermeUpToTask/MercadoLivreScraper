# Scrapy settings for mercado_livre project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "mercado_livre"

SPIDER_MODULES = ["mercado_livre.spiders"]
NEWSPIDER_MODULE = "mercado_livre.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "mercado_livre.middlewares.MercadoLivreSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
ROTATING_PROXY_LIST = [
    "98.162.25.7:31653",
    "117.160.250.133:80",
    "72.195.34.59:4145",
    "79.119.155.63:8080",
    "192.252.208.67:14287",
    "102.132.201.202:80",
    "147.75.92.251:80",
    "51.210.127.15:80",
    "184.181.217.220:4145",
    "92.204.135.37:33899",
    "212.69.128.72:5678",
    "159.69.9.90:3636",
    "139.129.162.65:3128",
    "72.10.160.90:15271",
    "66.42.224.229:41679",
    "103.49.202.252:80",
    "36.64.238.82:1080",
    "103.78.52.130:4153",
    "203.89.8.107:80",
    "98.178.72.21:10919",
    "121.159.146.251:80",
    "35.185.196.38:3128",
    "72.195.34.41:4145",
    "31.170.19.4:4153",
    "161.97.163.52:23224",
    "147.75.92.244:9443",
    "104.37.135.145:4145",
    "192.252.216.81:4145",
    "146.59.70.29:32953",
    "120.194.4.157:82",
    "216.10.242.18:38131",
    "54.36.122.16:44587",
    "67.43.227.228:30471",
    "72.210.252.134:46164",
    "92.204.135.37:8623",
    "67.43.236.20:1097"
]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 543,
}

PROXY_LIST = ROTATING_PROXY_LIST  # Optional for backwards compatibility
#DOWNLOADER_MIDDLEWARES = {
#    "mercado_livre.middlewares.MercadoLivreDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "mercado_livre.pipelines.MercadoLivrePipeline": 300,
}
DB_CREDENTIALS ={
    "dbname": "mercado_livre_data",
    "user": "postgres",
    "password": "12345",
    "host": "localhost"
}
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
