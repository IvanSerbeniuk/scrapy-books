import scrapy
import datetime


class HoodsSpider(scrapy.Spider):
    name = 'rewies'
    start_urls = ['https://www.dresslily.com/hoodies-c-181.html']
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

    def parse(self, response):
        links = response.css('a.goods-name-link.js_logsss_click_delegate_ps::attr(href)')
        for link in links:
            yield response.follow(link, callback=self.parse_rew)

        next_page = response.css('div.site-pager-pad-pc.site-pager ul li a::attr(href)')[-1].get()
        if next_page is not None:
            next_page = 'https://www.dresslily.com' + next_page
            yield response.follow(next_page, callback=self.parse)

    def parse_rew(self, response):

        container = response.css('div.reviewinfo.table')   #БЫВАЕТ что нет отзывов 
        for rewie in container:
            rat = rewie.css('span.review-rate span.review-star i::attr(class)').getall()
            num = rat.count('icon-star-black') 
            color = rewie.css('span.review-good-size::text')[2].get()
            color = color.split(':')
            size = rewie.css('span.review-good-size::text')[1].get()
            size = size.split(':')
            data = rewie.css('span.review-time::text').get()
            date_obj = datetime.datetime.strptime(data, '%b,%d %Y %H:%M:%S')
            unix_time = int(date_obj.timestamp())
            yield{
                'size': size[1].strip(),
                'color': color[1].strip(),
                'text': rewie.css('div.review-content-text ::text').get(),
                'rate': num,
                'ID': rewie.css('em.sku-show::text').get(),
                'Unix data':unix_time,
            }




    # 'ID': response.css('em.sku-show::text').get(),


# In [184]: len(response.css('div.reviewinfo.table'))
# Out[184]: 4                                           CONTAINER -

# In [192]: response.css('div.review-content-text ::text').get()
# Out[192]: 'CuteNice'                                   TEXT -

# In [191]: response.css('span.review-good-size::text')[1].get()
# Out[191]: 'Size: 2XL'                                  SIZE -

# In [193]: response.css('span.review-good-size::text')[2].get()
# Out[193]: 'Color: multicolor'                           COLOR - 

# In [194]: response.css('span.review-time::text').get()
# Out[194]: 'Jan,08 2023 01:03:57'                          TIME


# In [228]: response.css('div.reviewinfo.table span.review-star i::attr(class)').get()
# Out[228]: 'icon-star-black'                               RATING - 