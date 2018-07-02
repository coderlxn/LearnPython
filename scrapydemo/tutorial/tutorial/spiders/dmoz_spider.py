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
        filename = response.url.split("/")[-2]
        with open(filename, "wb") as f:
            f.write(response.body)