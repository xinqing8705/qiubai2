import scrapy
from qiubai2.items import Qiubai2Item

class QiuBai2(scrapy.Spider):
    name = 'qiubai2'
    start_urls = [
    "http://www.qiushibaike.com/",
    ]
    
    # has_debug = False
    
    def parse(self, response):
        # if not self.has_debug:
            # from scrapy.shell import inspect_response
            # inspect_response(response,self)
            # has_debug = True
        for ele in response.xpath('//div[@class="article block untagged mb15"]'):
            authors = ele.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract()
            contents = ele.xpath('./div[@class="content"]/text()').extract()
            yield Qiubai2Item(author=authors, content=contents)

        