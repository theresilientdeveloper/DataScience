# -*- coding: utf-8 -*-

# Scrapy settings for data_science project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'data_science'

SPIDER_MODULES = ['data_science.spiders']
NEWSPIDER_MODULE = 'data_science.spiders'
DOWNLOAD_DELAY = 2
COOKIES_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'data_science (+http://www.yourdomain.com)'
