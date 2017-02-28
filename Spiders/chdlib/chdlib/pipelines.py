# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class ChdlibPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient("localhost", 27017)
        self.db = client["chd"]
        self.collection_name = 'books'

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item
