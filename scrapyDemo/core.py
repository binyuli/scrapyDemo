
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.conf import settings
from scrapy.utils.log import configure_logging
from spiders.DmozSpider import DmozSpider
from spiders.sina_usedcar import SinaUsedCarSpider
from spiders.PCauto_rank import PCautoRankSpider

configure_logging(settings)
runner = CrawlerRunner(settings)


@defer.inlineCallbacks
def crawl():
    # yield runner.crawl(DmozSpider)
    # yield runner.crawl(SinaUsedCarSpider())
    yield runner.crawl(PCautoRankSpider())
    reactor.stop()


crawl()
reactor.run()  # the script will block here until the last crawl call is finished
