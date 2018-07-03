import scrapy
from scrapydemo.tutorial.tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allow_domains = ["dmoz-odp.org"]
    start_urls = [
        "http://dmoz-odp.org/Computers/Programming/Languages/Python/Books/",
        "http://dmoz-odp.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        for sel in response.xpath("//ul/li"):
            item = DmozItem()
            item["title"] = sel.xpath("a/text()").extract()
            item["link"] = sel.xpath("a/@href").extract()
            item["desc"] = sel.xpath("text()").extract()
            yield item