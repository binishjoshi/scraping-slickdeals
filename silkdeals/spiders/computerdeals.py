import scrapy


class ComputerdealsSpider(scrapy.Spider):
    name = 'computerdeals'
    allowed_domains = ['slickdeals.net/computer-deals']
    start_urls = ['http://slickdeals.net/computer-deals/']

    def parse(self, response):
        pass
