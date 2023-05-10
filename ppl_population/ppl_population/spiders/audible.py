import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    start_urls = ["https://www.audible.com/search"]

    def parse(self, response):
        conts = response.xpath('//div[@id="product-list-a11y-skiplink-target"]/span/ul/li')
