# -*- coding: utf-8 -*-

from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from lxml import etree
from bs4 import BeautifulSoup

class PCautoRankSpider(RedisSpider):
    name = 'PCauto_rank'
    # index_page = 'http://price.pcauto.com.cn/top/r3/'
    index_page = 'http://price.pcauto.com.cn/top/hot/s1-t1.html'
    api_url = 'http://price.pcauto.com.cn%s'

    def start_requests(self):
        yield Request(self.index_page, callback=self.get_left_nav)

    # 测试 BeautifulSoup 是否能连续使用两个 find_all 方法
    def get_left_nav(self,response):
        # model = etree.HTML(response.body_as_unicode())
        # nav_list = model.xpath('//div[@id="leftNav"]/ul[@class="pb200"]/li//a[@class="dd "]')
        soup = BeautifulSoup(response.body_as_unicode(), 'lxml')
        nav_list = soup.find('div', id='leftNav').find('ul', class_='pb200').find_all('li').find_all('a', class_='dd')
        for sub_nav in nav_list:
            href = self.api_url % sub_nav.xpath('./@href')[0]
            yield Request(href, callback=self.get_url)

    def get_url(self):
        pass

