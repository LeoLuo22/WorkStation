import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'#id the spider

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        """parse response
        """
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css('span.text::text')[0].extract(),
                'author': quote.css('span small::text')[0].extract(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
        next_page = response.css('li.next a::attr(href)')[0].extract()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
510721197212194241
