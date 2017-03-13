# -*- coding:utf-8 -*-
#__author__: Leo Luo

import requests
from bs4 import BeautifulSoup
import lxml
import collections
import os

BASE_URL = "http://wiscom.chd.edu.cn:8080/opac/item.php"

class Books():
    def __init__(self, header=None, filename=None):
        self.__header = header
        self.filename = filename

    def generate_payload(self, begin, end):
        payload = collections.defaultdict()
        make_up = "0000000000"
        values = []
        for i in range(begin, end):
            value = i
            value = str(value)
            if len(value) != 10:
                distance = 10 - len(value)
                value = make_up[0:distance] + value
                values.append(value)
            else:
                values.append(value)
        #value = "0000198288"
        key  = "marc_no"
        payload[key] = values
        return payload

    def get_filename_and_url(self, payload):
        result = []
        #payload = self.generate_payload(211,234)
        filename_session = requests.Session()
        r = filename_session.get(BASE_URL, params=payload)
        base_soup = r.content.decode('utf-8')
        soup = BeautifulSoup(base_soup, 'lxml')
        test  = soup.find('dd')
        try:
            title = test.a.string
        except AttributeError as err:
            print("不存在!")
            return 0
        test.a.decompose()
        try:
            name  = test.string.replace("/", "_")
        except AttributeError as err:
            print(err)
            return 0
        filename = title + name
        result.append(filename)
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
            return 0
        result.append(pic_url)
        return result

    def get_img(self,result):
        print(result)
        try:
            douban = result[1]
        except TypeError as err:
            print(err)
            return 0
        filename = result[0]
        douban_session = requests.Session()
        d = douban_session.get(douban)
        content = d.content
        now_path = os.path.abspath('.')
        save_path  = now_path + "/book/"
        filename = "{0}{1}{2}".format(save_path, filename,".jpg")
        try:
            with open(filename, 'wb') as fh:
                fh.write(content)
        except (FileNotFoundError,OSError) as err:
            return 0

def real_payload(payload_dict):
    for i in range(0,len(payload_dict["marc_no"])):
        yield {"marc_no":str(payload_dict["marc_no"][i])}
def main():
    payload_dict = collections.OrderedDict()
    range_begin = input("请输入起始的数字: ")
    range_end = input("请输入结束的数字: ")
    range_begin = int(range_begin)
    range_end = int(range_end)
    book = Books()
    payload_dict = book.generate_payload(range_begin, range_end)
    a = real_payload(payload_dict)
    for i in range(range_begin, range_end):
        payload = next(a)
        print(payload)
        result = book.get_filename_and_url(payload)
        fina = book.get_img(result)
    #result = book.get_filename_and_url()
    #fina = book.get_img(result)


if __name__ == "__main__":
    main()
