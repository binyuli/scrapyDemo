import scrapy

from scrapy.selector import Selector
from scrapyDemo.items import ScrapydemoItem

class DmozSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["dmoz.org"]
    # start_urls = [
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    # ]
    # "http://www.landrover.com.cn/index.html"
    start_urls = [
        "http://www.jaguar.com.cn/index.html",
    ]

    # def parse(self, response):
    #     filename = response.url.split("/")[-2]
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    # def parse(self, response):
    #     for sel in response.xpath('//ul/li'):
    #         title = sel.xpath('a/text()').extract()
    #         link = sel.xpath('a/@href').extract()
    #         desc = sel.xpath('text()').extract()
    #         print title, link, desc

    def parse(self, response):
        for sel in response.xpath('/html/head/title'):
            title = sel.xpath('text()').extract()
            print title

    def parse(self, response):
        sites = response.xpath('/html/head/title')
        items = []
        for site in sites:
            item = ScrapydemoItem()
            title_list = site.xpath('text()').extract()
            print title_list[0]
            item['title'] = title_list
            items.append(item)
        return items
