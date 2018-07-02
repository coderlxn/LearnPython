# -*- coding: utf-8 -*-
from __future__ import absolute_import
import scrapy
from ..items import TencentItem


class TencentpositionSpider(scrapy.Spider):
    """
    功能：爬取腾讯社招信息
    """

    name = 'tencentPosition'
    allowed_domains = ['tencent.com']
    url = 'http://tencent.com/position.php?&start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
            item['position_name'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['position_link'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['position_type'] = each.xpath("./td[2]/text()").extract()[0]
            item['position_num'] = each.xpath("./td[3]/text()").extract()[0]
            item['work_location'] = each.xpath("./td[4]/text()").extract()[0]
            item['publish_time'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

        if self.offset < 1680: #???
            self.offset += 10

        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

