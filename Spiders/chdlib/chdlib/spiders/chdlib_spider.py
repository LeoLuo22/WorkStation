from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
import lxml
import requests
import os
import scrapy

class BookSpider(CrawlSpider):
    name = "books"
    allowed_domains = ["wiscom.chd.edu.cn"]

    start_urls = [
        'http://wiscom.chd.edu.cn:8080/opac/item.php?marc_no=0000405961',
    ]

    rules = (
             Rule(LinkExtractor(allow='http://wiscom.chd.edu.cn:8080/opac/item\.php\?marc_no=\d*$'),
             callback='parse'), )

    def parse(self, response):
        item = scrapy.Item()
        soup = BeautifulSoup(response.text, 'lxml')
        try:
            pic_link = soup.find('img', attrs={'id': 'book_img'})['src']
        except TypeError:
            return
        info_soup = soup.find('div', attrs={'id': 'item_detail',
                              'style': 'float:left; width:80%;'}, )
        details_soup = info_soup.find_all('dl', attrs={'class': 'booklist'})

        item['题名/责任者'] = details_soup[0].find('dd').get_text()
        item['出版发行商'] = details_soup[1].find('dd').get_text()
        ietm['ISBN及定价'] = details_soup[2].find('dd').get_text()
        item['载体形态项'] = details_soup[3].find('dd').get_text()
        item['并列正题名'] = details_soup[4].find('dd').get_text()
        item['个人责任者'] = details_soup[5].find('dd').get_text()
        item['学科主题'] = details_soup[6].find('dd').get_text()
        item['中图法分类号'] = details_soup[7].find('dd').get_text()
        item['一般附注'] = details_soup[8].find('dd').get_text()
        item['书目附注'] = details_soup[9].find('dd').get_text()
        item['提要文摘附注'] = details_soup[10].find('dd').get_text()
        item['豆瓣简介'] = details_soup[11].find('dd').get_text()

        content = requests.get(pic_link).content
        picname = str(details_soup[0].find('dd').get_text()) + ".png"
        os.chdir('e:/books')
        with open(picname, 'wb') as f:
            f.write(content)

        return item


"""
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item
"""
