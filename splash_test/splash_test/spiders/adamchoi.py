import scrapy
from scrapy_splash import SplashRequest


class AdamchoiSpider(scrapy.Spider):
    name = "adamchoi"
    allowed_domains = ["www.adamchoi.co.uk"]
    start_urls = ["http://www.adamchoi.co.uk/"]

    scriipt = '''
        function main(splash, args)
            splash.private_mode_enabled = false
            assert(splash:go(args.url))
            all_matches = assert(splash:select_all('label.btn.btn-sm.btn-primary'))
            all_matches[2]:mouse_click()
            splash:set_viewport_full()
            return{splash:html(), splash:png()}
        end
    '''
    
    def start_requests(self):
        yield SplashRequest(url='https://www.adamchoi.co.uk/overs/detailed', callback=self.parse,
                            endpoint='execute', args={'lua_source':self.scriipt})


    def parse(self, response):
        print(response.body)
