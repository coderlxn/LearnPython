# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):

    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_type = scrapy.Field()
    position_num = scrapy.Field()
    work_location = scrapy.Field()
    publish_time = scrapy.Field()

