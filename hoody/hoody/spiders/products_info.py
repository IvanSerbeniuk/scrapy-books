import scrapy
import json
from scrapy.http.request.json_request import JsonRequest


class HoodsSpider(scrapy.Spider):
    name = 'products'
    start_urls = ['https://www.dresslily.com/hoodies-c-181.html']
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
                   'accept': 'application/json'}


    def parse(self, response):
        links = response.css('a.goods-name-link.js_logsss_click_delegate_ps::attr(href)')
        for link in links:
            yield response.follow(link, callback=self.parse_hoodos)

        next_page = response.css('div.site-pager-pad-pc.site-pager ul li a::attr(href)')[-1].get()
        if next_page is not None:
            next_page = 'https://www.dresslily.com' + next_page
            yield response.follow(next_page, callback=self.parse)  #точно переходит по ссылке?)

    def parse_hoodos(self, response):
        discount = response.css('title::text').get()
        discount = discount.split()
        try:
            res19 = response.css('div.xxkkk20 ::text')[19].get()
            res20 = response.css('div.xxkkk20 ::text')[20].get().strip()
        except:
            res19 = None
            res20 = None
        try:
            res22 = response.css('div.xxkkk20 ::text')[22].get()
            res23 = response.css('div.xxkkk20 ::text')[23].get().strip()
        except:
            res22 = None
            res23 = None
        try:
            res25 = response.css('div.xxkkk20 ::text')[25].get()
            res26 = response.css('div.xxkkk20 ::text')[26].get().strip()
        except:
            res25 = None
            res26 = None
        try:
            res28 = response.css('div.xxkkk20 ::text')[28].get()
            res29 = response.css('div.xxkkk20 ::text')[29].get().strip()
        except:
            res28 = None
            res29 = None


        yield{
            'price with dis': response.css('span.curPrice::text').get(), 
            'name': response.css('span.goodtitle::text').get(),
            'link': response.css('link ::attr(href)')[-10].get(),
            'ID': response.css('em.sku-show::text').get(),
            'discount': discount[0][1:],
            'original pr': response.css('span.js-dl-marketPrice1.marketPrice.my-shop-price.dl-has-rrp-tag::attr(data-orgp)').get(),
            'rewies count': response.css('div.slidetitle strong::text').get(),
            response.css('div.xxkkk20 ::text')[1].get(): response.css('div.xxkkk20 ::text')[2].get(), 
            response.css('div.xxkkk20 ::text')[4].get(): response.css('div.xxkkk20 ::text')[5].get(),
            response.css('div.xxkkk20 ::text')[7].get(): response.css('div.xxkkk20 ::text')[8].get().strip(),
            response.css('div.xxkkk20 ::text')[10].get(): response.css('div.xxkkk20 ::text')[11].get().strip(),
            response.css('div.xxkkk20 ::text')[13].get(): response.css('div.xxkkk20 ::text')[14].get().strip(),
            response.css('div.xxkkk20 ::text')[16].get(): response.css('div.xxkkk20 ::text')[17].get().strip(),
            res19: res20,
            res22: res23,
            res25: res26,
            res28: res29,
            }







    


# In [85]: response.css('div.site-pager-pad-pc.site-pager ul li a::attr(href)')[-1].get()
# Out[85]: '/hoodies-c-181-page-2.html'                                                         #PAGINATION - 

# fetch('https://www.dresslily.com/hoodies-c-181.html')
# In [24]: response.css('a.goods-name-link.js_logsss_click_delegate_ps::text').get()
# Out[24]: 'Flocking Lining Knit Sweatshirt O Ring A Quarter Zip Stand Collar Heathered Sweatshirt'  #NAME - 

# In [26]: response.css('a.goods-name-link.js_logsss_click_delegate_ps::attr(href)').get()
# Out[26]: 'https://www.dresslily.com/flocking-lining-knit-sweatshirt-o-product8459850.html'      #LINK


# fetch('https://www.dresslily.com/flocking-lining-knit-sweatshirt-o-product8459850.html')
# In [40]: response.css('em.sku-show::text').get()
# Out[40]: '506127503'                                                                           #ID -

# In [107]: response.css('span.curPrice::text').get()(default='Nothing found')
# Out[107]: 'USD18.99'                                                                              #PRICE WITH % -

#discount    #######view(response) - идет загрузка постоянная. Может надо sleep()? Или через тег <title>
# In [61]: response.css('title::text').get()
# Out[61]: '[39% OFF]  2023 Cat And Fist Print Drawstring Hoodie Kangaroo Pocket Ribbed Hem Hoodie In DARK GRAY | DressLily '
                                                                                                    #DISCOUNT -

# In [21]: response.css('span.js-dl-marketPrice1.marketPrice.my-shop-price.dl-has-rrp-tag::attr(data-orgp)').get()
# Out[21]: '41.09'                                                                               #ORIGINAL PRICE -


# In [8]: response.css('div.slidetitle strong::text').get()
# Out[8]: '3'                                                                                 #CUSTOMER REWIES - 

# In [12]: response.css('div.xxkkk20 ::text').getall()     #  .get() вернет только 'For Men', 'Hooodies'
# Out[12]: 
# ['\n            ',
#  'Gender:',
#  ' For Men ',
#  '             ',
#  'Clothes Type:',
#  ' Hoodies ',
#  '             ',
#  'Style:',
#  ' Casual ',
#  '             ',
#  'Occasions:',
#  ' Daily ',
#  '             ',
#  'Fit Type:',
#  ' Regular Fit ',
#  '             ',
#  'Collar:',
#  ' Hooded ',
#  '             ',
#  'Length:',
#  ' Regular ',
#  '             ',
#  'Sleeve Length:',
#  ' Long Sleeves ',
#  '             ',
#  'Pattern Type:',
#  ' Cat ',
#  '             ',
#  'Embellishment:',
#  ' Front Pocket ',
#  '             ',
#  'Material:',
#  ' Polyester,Spandex ',
#  '             ',
#  'Fabric Stretch:',
#  ' Slight Stretch ',
#  '             ',
#  'Season:',
#  ' Fall,Spring ',
#  '             ',
#  'Weight:',
#  ' 0.4150kg ',
#  '             ',
#  'Package Contents:',
#  ' 1 x Hoodie         \n    ']


# response.css('span>span.my-shop-price').getall()



