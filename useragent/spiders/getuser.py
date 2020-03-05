# -*- coding: utf-8 -*-
import scrapy
from useragent.items import UseragentItem

class GetuserSpider(scrapy.Spider):
    name = 'getuser'
    allowed_domains = ['useragentstring.com']
    start_urls = ['http://useragentstring.com/pages/useragentstring.php?name=All']

    def parse(self, response):
        uls = response.xpath('//div[@id="liste"]/ul')
        for ul in uls:
            lis = ul.xpath('./li/a/text()').getall()
            for li in lis:
                item = UseragentItem(User_Agent=li)
                yield item