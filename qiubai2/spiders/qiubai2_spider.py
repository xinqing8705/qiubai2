import scrapy

class QiuBai2(scrapy.Spider):
    name = 'qiubai2'
    start_urls = [
    "http://www.qiushibaike.com/",
    ]
    
    def parse(self, response):
        #from scrapy.shell import inspect_response
        #inspect_response(response,self)
        print response.xpath('//div[@class="content"]').extract()
        