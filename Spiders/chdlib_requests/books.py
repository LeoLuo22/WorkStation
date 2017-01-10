# -*- coding:utf-8 -*-
#__author__: Leo Luo

import os
import collections
import lxml
import pymongo
import requests
import random
import time
from bs4 import BeautifulSoup
from requests.exceptions import MissingSchema
from utils import file
import url
import bson

BASE_URL = "http://wiscom.chd.edu.cn:8080/opac/item.php"
HEAD = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
FILEPATH = 'e:/books/'

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.chd
collection = db.library

class Library():
    def __init__(self):
        pass

    def __get_douban_info(self, isbn):
        """Get book's info from douban
        @param isbn
            Book's isbn
        @return
            A dict that contains douban info
        """
        info_dict = {}
        url = 'http://wiscom.chd.edu.cn:8080/opac/ajax_douban.php'
        payload = {'isbn': isbn}
        try:
            response = requests.get(url, params=payload, headers=HEAD)
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            return self.__get_douban_info(isbn)
        infos = eval(response.text) #eval function can convert str object to dict object
        for key, value in infos.items():
            while '\\' in value:
                value = value.replace('\\', '')
                infos[key] = value
        return infos

    def __get_isbn(self, soup):
        """Get book's isbn
        @soup: results of find 'dl', attrs={'class': 'booklist'}
        @return: type: str; value: isbn
        """
        isbn_raw = soup[2].dd.string
        try:
            isbn = isbn_raw.split('/')[0]
        except AttributeError:
            return 0
        while '-' in isbn:
            isbn = isbn.replace('-', '')
        return isbn

    def parse(self, payload):
        """Parse book information
        @param: book's id marc_no=id
        @book: book's information
        """
        book = collections.OrderedDict()
        try:
            response = requests.get(BASE_URL, params=payload, headers=HEAD)
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            return self.parse(payload)
        base = response.content.decode('utf-8')
        soup = BeautifulSoup(base, 'lxml')
        item_detail_soup = soup.find_all('dl', attrs={'class': 'booklist'})
        isbn = self.__get_isbn(item_detail_soup)
        if isbn:
            douban_info = self.__get_douban_info(isbn)
        for detail in item_detail_soup:
            if detail.dt.string:
                book[detail.dt.string.replace(':', '')] = detail.dd.get_text()
        if isbn:
            book.update(douban_info)#update: insert douban_info to book those are not in book
        book.update(payload)
        try:
            hasImg = self.__save_image(book.get('image'), book.get('题名/责任者').replace('/', '_'))
        except AttributeError:
            return 1
        if hasImg:
            book['pic'] = FILEPATH + book.get('题名/责任者').replace('/', '_')
        try:
            collection.insert(book)
        except pymongo.errors.ServerSelectionTimeoutError:
            print('MongoDB server is not activated, try again. ')
            return 0
        except bson.errors.InvalidDocument:
            return 1
        #print(book)
        print("{0} 已添加".format(book.get('题名/责任者')))
        return 1

    def __save_image(self, link, name):
        """Write image to disk
        @param link
            Image's url on Douban
        @param name
            book's name and author
        @return
            None
        """
        name = name.replace('>', '').replace('<', '')
        name = name.replace(':', '')
        try:
            response = requests.get(link, headers=HEAD)
        except MissingSchema:
            #print("{0} 没有封面图片".format(name))
            return 0
        except requests.exceptions.ConnectionError:
            return 0
        cwd = os.getcwd()
        os.chdir('e:/books/')
        try:
            with open(name+'.jpg', 'wb') as f:
                f.write(response.content)
        except OSError:
            with open(name[0: 2]+'.jpg', 'wb') as f:
                f.write(response.content)
        os.chdir(cwd)
        return 1

def read_url_from_file(file, last_record, used_name):
    """Read marc_no from file
    @param file
        The file contains all marc_nos
    @param last_record
        Last used  marc_no, generally saved in used_name file
    @param used_name
        Filename that is to save used marc_nos
    @return
        Literator, marc_no
    """
    totals = []
    news = []
    flag = False

    with open(file, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            totals.append(line)

    for total in totals:
        if total == last_record:
            flag = True
        if flag:
            news.append(total)

    news.remove(last_record)

    with open(used_name+'.txt', 'a') as fh:
        for new in news:
            fh.write(new+'\n')
            yield new


def main(last_record):
    """Where the module start
    @payload: book's id
    """
    """
    payload = {}
    payload['marc_no'] = '0000405961'
    book = BookSpider()
    parse(payload)
    """
    payload = {}
    library = Library()
    a = read_url_from_file('unusedUrls.txt', last_record, 'used1')
    while True:
        #print(next(a))
        try:
            payload['marc_no'] = next(a)
        except StopIteration:
            unusedUrls = []
            with open('unusedUrls.txt', 'r') as fd:
                for line in fd:
                    unusedUrls.append(line.replace('\n', ''))
            pay = {}
            last_record = unusedUrls[len(unusedUrls)-1]
            pay['marc_no'] = last_record
            book = url.BookSpider()
            try:
                book.get_urls(pay)
            except RecursionError:
                return main(last_record)
            return main(last_record)
        flag = library.parse(payload)
        if not flag:
            break
    return

    #file.remove_duplicate('merged.txt', 'usedUrls.txt', 'merged1.txt')


if __name__ == "__main__":
    main('0000065249')
