import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'#id the spider

    def start_requests(self):
        """generate urls
        @return: must return an iterable of Requests.
        """
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """parse response
        """
        page = response.url.split("/")[-2]
        filename = 'quotes-{0}.html'.format(page)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {0}'.format(filename))
