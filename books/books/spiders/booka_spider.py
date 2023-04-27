import scrapy


class BookSpider(scrapy.Spider):
    name = 'booki'
    allowed_hosts = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/index.html']

    def parse(self, response):
        for link in response.css('h3 a::attr(href)').getall():
            yield response.follow(link, callback=self.parse_book)
            
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


    def parse_book(self, response):
        for res in response.css('div.col-sm-6.product_main'):
            yield{
                    'name':res.css('h1::text').get(),        
                    'cost':res.css('p.price_color::text').get(),
                    'UPC':response.css('table.table.table-striped td::text').get(),
                }

# ----Light version----
# import scrapy


# class BookSpider(scrapy.Spider):
#     name = 'booki'
#     allowed_hosts = ['books.toscrape.com']
#     start_urls = ['http://books.toscrape.com/index.html']

#     def parse(self, response):
#         for link in response.css('article.product_pod'):
#             yield{
#                 'name':link.css('h3 a::text').get(),        
#                 'cost':link.css('div.product_price p::text').get(),
#             }
#         next_page = response.css('li.next a::attr(href)').get()

#         if next_page is not None:
#             yield response.follow(next_page, callback=self.parse)




#  scrapy crawl booki -O books_upc.csv
