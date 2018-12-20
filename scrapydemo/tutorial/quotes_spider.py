# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 10:12 AM
# @Author  : Jax.Li
# @FileName: quotes_spider.py
# @Software: PyCharm
# @Blog    ：https://blog.jaxli.com

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                "text": quote.css("span.text::text").extract_first(),
                "author": quote.xpath("span/small/text()").extract_first(),
            }

        next_page = response.css("li.next a::attr('href')").extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
