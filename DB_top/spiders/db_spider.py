# -*- coding: utf-8 -*-
import scrapy
from DB_top.items import DbTopItem


class DbSpiderSpider(scrapy.Spider):
    name = 'db_spider'
    allowed_domains = ['https://movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=/']

    def parse(self, response):
        item = DbTopItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')

        for movie in movies:
            url = movie.xpath('.//div/div[2]/div[1]/a/@href').extract()
            item['url'] = url
            yield item

        url = response.xpath('//span[@class="next"]/a/@href').extract()[0]
        if url is not None:
            fullurl = response.urljoin(url)
            yield scrapy.Request(fullurl, callback=self.parse, dont_filter=True)



