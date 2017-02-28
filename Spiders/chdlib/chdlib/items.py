# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class ChdlibItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID = Field()
    isbn = Field()
    douban = Field()
    lib = Field()
    出版发行项 = Field()
    个人责任者 = Field()
    中图法分类号 = Field()
    题名责任者 = Field()
    ISBN及定价 = Field()
    载体形态项 = Field()
    其它题名 = Field()
    学科主题 = Field()
    出版发行附注 = Field()
    提要文摘附注 = Field()
    豆瓣简介 = Field()
    丛编项 = Field()
    一般附注 = Field()
    内容附注 = Field()
    地名主题 = Field()
    责任者附注 = Field()
    书目附注 = Field()

