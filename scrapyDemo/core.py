
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.conf import settings
from scrapy.utils.log import configure_logging
from spiders.DmozSpider import DmozSpider

configure_logging(settings)
runner = CrawlerRunner(settings)

DmozSpider = DmozSpider()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(DmozSpider)
    reactor.stop()


crawl()
reactor.run()  # the script will block here until the last crawl call is finished
