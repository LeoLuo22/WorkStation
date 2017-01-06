# -*- coding:utf-8 -*-
#__author__: Leo Luo

import os
import collections
import lxml
import requests
import proxylib
import random
from bs4 import BeautifulSoup

BASE_URL = "http://wiscom.chd.edu.cn:8080/opac/item.php"
HEAD = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

def get_douban_info(isbn):
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

def get_isbn(soup):
    """Get book's isbn
    @soup: results of find 'dl', attrs={'class': 'booklist'}
    @return: str, isbn
    """
    isbn_raw = soup[2].dd.string
    isbn = isbn_raw.split('/')[0]
    while '-' in isbn:
        isbn = isbn.replace('-', '')
    return isbn

def get_filename_and_url(payload):
    """Parse book information
    @param: book's id marc_no=id
    @book: book's information
    """
    book = collections.OrderedDict()
    response = requests.get(BASE_URL, params=payload, headers=HEAD, proxies={'http': 'http://127.0.0.1'})
    base = response.content.decode('utf-8')
    soup = BeautifulSoup(base, 'lxml')
    item_detail_soup = soup.find_all('dl', attrs={'class': 'booklist'})
    isbn = get_isbn(item_detail_soup)
    douban_info = get_douban_info(isbn)
    for detail in item_detail_soup:
        if detail.dt.string:
            book[detail.dt.string.replace(':', '')] = detail.dd.get_text()
    book.update(douban_info)#update: insert douban_info to book those are not in book
    save_image(book.get('image'), book.get('题名/责任者').replace('/', '_'))
    print(book)#TODO: Add proxy, write to mangodb, discover more links

def save_image(link, name):
    """Write image to disk
    @param link: Image's url on Douban
    @param name: book's name and author
    @return: None
    """
    response = requests.get(link, headers=HEAD)
    cwd = os.getcwd()
    os.chdir('e:/books')
    with open(name+'.jpg', 'wb') as f:
        f.write(response.content)
    os.chdir(cwd)

class BookSpider():
    def __init__(self):
        self.unusedUrls = []

    def get_urls(self, payload):
        """Discover more urls
        @param payload: dict, {'marc_no': 'id'}
        @return
        """
        ajax_url = 'http://wiscom.chd.edu.cn:8080/opac/ajax_likehood_book.php'
        response = requests.get(ajax_url, params=payload, headers=HEAD)
        soup = BeautifulSoup(response.text, 'lxml')
        hrefs = soup.find_all('a', attrs={'target': '_blank'})
        for href in hrefs:
            marc_no = href.get('href').split('=')[1]
            if marc_no not in self.unusedUrls:
                print(marc_no)
                with open('unusedUrls.txt', 'a') as f:
                    f.write(marc_no+'\n')
                self.unusedUrls.append(marc_no)
        print(len(self.unusedUrls))
        self.get_urls({'marc_no': self.unusedUrls[random.randint(0, len(self.unusedUrls)-1)]})


def main():
    """Where the module start
    @payload: book's id
    """
    payload = {}
    payload['marc_no'] = '0000405961'
    book = BookSpider()
    book.get_urls(payload)
    """
    get_douban_intro(9787114081996)
    """
    return


if __name__ == "__main__":
    main()
