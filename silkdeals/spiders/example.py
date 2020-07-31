import scrapy
from scrapy_selenium import SeleniumRequest


class ExampleSpider(scrapy.Spider):
    name = 'example'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):
        img = response.meta['screenshot']

        with open('screenshot.png', 'wb') as f:
            f.write(img)
