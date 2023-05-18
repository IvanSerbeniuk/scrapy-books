import scrapy


class AdamchoiSpider(scrapy.Spider):
    name = "adamchoi"
    allowed_domains = ["www.adamchoi.co.uk"]
    start_urls = ["http://www.adamchoi.co.uk/"]

    def parse(self, response):
        pass
