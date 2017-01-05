# -*- coding:utf-8 -*-
#__author__: Leo Luo

import requests
from bs4 import BeautifulSoup
import lxml
import collections
import os

BASE_URL = "http://wiscom.chd.edu.cn:8080/opac/item.php"

def get_img_link(soup):
    douban_url = soup.find_all('a',attrs={'target':'_blank'})
    for url in douban_url:
        d_u = url.get('href')
        if not d_u.endswith('/'):
            continue
        douban = d_u
    d = requests.get(douban)
    d_soup = d.content.decode('utf-8')
    douban_soup = BeautifulSoup(d_soup, 'lxml')
    try:
        pic_url = douban_soup.find('a', attrs={'class':'nbg'})['href']
    except TypeError as err:
        print("不存在!")
    return pic_url

def get_filename_and_url(payload):
    book = collections.OrderedDict()
    r = requests.get(BASE_URL, params=payload)
    base = r.content.decode('utf-8')
    soup = BeautifulSoup(base, 'lxml')
    img_link = get_img_link(soup)
    item_detail_soup = soup.find_all('dl', attrs={'class': 'booklist'})
    for detail in item_detail_soup:
        if detail.dt.string:
            book[detail.dt.string.replace(':','')] = detail.dd.get_text()#TODO: Add douban info
    print(book)#TODO: Add proxy, write to mangodb, discover more links, save image

def main():
    payload={}
    payload['marc_no'] = '0000405961'
    result = get_filename_and_url(payload)
    print(result)


if __name__ == "__main__":
    main()
