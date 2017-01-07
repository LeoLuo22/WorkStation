# -*- coding:utf-8 -*-
#__author__: Leo Luo

import os
import collections
import lxml
import pymango
import requests
import random
from bs4 import BeautifulSoup
from requests.exceptions import MissingSchema

BASE_URL = "http://wiscom.chd.edu.cn:8080/opac/item.php"
HEAD = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
FILEPATH = 'e:/books/'

client = pymango.MongoClient("mongodb://localhost:27017/")
db = client.chd
collection = db.library

class Library():
    def __init__(self):
        pass

    def __get_douban_info(self, isbn):
        info_dict = {}
        url = 'http://wiscom.chd.edu.cn:8080/opac/ajax_douban.php'
        payload = {'isbn': isbn}
        response = requests.get(url, params=payload, headers=HEAD)
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
        isbn = isbn_raw.split('/')[0]
        while '-' in isbn:
            isbn = isbn.replace('-', '')
        return isbn

    def parse(self, payload):
        """Parse book information
        @param: book's id marc_no=id
        @book: book's information
        """
        book = collections.OrderedDict()
        response = requests.get(BASE_URL, params=payload, headers=HEAD)
        base = response.content.decode('utf-8')
        soup = BeautifulSoup(base, 'lxml')
        item_detail_soup = soup.find_all('dl', attrs={'class': 'booklist'})
        isbn = self.__get_isbn(item_detail_soup)
        douban_info = self.__get_douban_info(isbn)
        for detail in item_detail_soup:
            if detail.dt.string:
                book[detail.dt.string.replace(':', '')] = detail.dd.get_text()
        book.update(douban_info)#update: insert douban_info to book those are not in book
        hasImg = self.__save_image(book.get('image'), book.get('题名/责任者').replace('/', '_'))
        if hasImg:
            book['pic'] = FILEPATH + book.get('题名/责任者').replace('/', '_')
        collection.insert(book)
        #print(book)
        print("{0} 已添加".format(book.get('题名/责任者')))

    def __save_image(self, link, name):
        """Write image to disk
        @param link: Image's url on Douban
        @param name: book's name and author
        @return: None
        """
        try:
            response = requests.get(link, headers=HEAD)
        except MissingSchema:
            print("{0} 没有封面图片".format(name))
            return 0
        cwd = os.getcwd()
        os.chdir('e:/books/')
        with open(name+'.jpg', 'wb') as f:
            f.write(response.content)
        os.chdir(cwd)
        return 1

def read_url_from_file():
    with open('unusedUrls.txt', 'r') as f:
        for line in f:
            with open('usedUrls.txt', 'a') as fh:
                fh.write(line)
            yield line.replace('\n', '')

def main():
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
    a = read_url_from_file()
    while True:
        #print(next(a))
        payload['marc_no'] = next(a)
        library.parse(payload)
    return


if __name__ == "__main__":
    main()
