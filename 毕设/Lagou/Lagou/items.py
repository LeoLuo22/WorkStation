# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class LagouItem(scrapy.Item):
    # define the fields for your item here lik
    _id = Field()  # 工作ID
    companyId = Field()
    name = Field()  # 职位名
    advantages = Field()  # 职位诱惑
    description = Field()  # 职位描述
    workLocation = Field()  # 工作地址
    company = Field()  # 公司
    salary = Field()  # 薪水
    location = Field()  # 地址
    experience = Field()  # 工作经验
    background = Field()  # 背景
    isFulltime = Field()
    labels = Field()#标签
