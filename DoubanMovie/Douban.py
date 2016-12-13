# -*- coding:utf-8 -*-
__author__ = "Leo Luo"

from bs4 import BeautifulSoup
import requests
import lxml
from PIL import Image
import random
import urllib.parse
import re

searchUrl = 'https://movie.douban.com/subject_search?search_text=%E4%B8%83%E6%9C%88&cat=1002'
class Douban(object):
    def __init__(self):
        self.__LOGIN_DATA = { 'source':'movie',
                                'redir':'https://movie.douban.com/',
                                'form_email':'leoluo22@gmail.com',
                                'form_password':'vampire.Leo123',
                                'login':'登录'}
        self.__HEADER = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.__BASE_URL = "https://accounts.douban.com/login?source=movie"
        self.__LOGIN_URL = "https://accounts.douban.com/login"
        self.__SEARCH_URL = "https://movie.douban.com/subject_search?search_text=MOVIENAME&cat=1002"
        self.__session = requests.Session()
        self.__session.get(self.__BASE_URL, headers=self.__HEADER)
        self.__proxiesList = []
        self.__proxy = {}
        self.__getProxies()
        self.__getproxy(1)


    def __getProxies(self):
        with open('proxies.txt', 'r') as fh:
            for line in fh:
                line = line.replace('\n', '')
                self.__proxiesList.append(line)
        return

    def __test(self, url):
        proxy = {'http': url}
        try:
            r = requests.get('https://www.baidu.com', proxies=proxy, headers=self.__HEADER, timeout=1)
        except Exception:
            return False
        if r.status_code == 200:
            return True
        return False

    def __getproxy(self, i):
        url = self.__proxiesList[i]
        if self.__test(url):
            self.__proxy = {'http://':url}
            return
        else:
            i = random.randint(1, 99)
            self.__getproxy(i)

    def __getCaptcha(self, soup):
        result = {}
        captchaUrl = soup.find('img', attrs={'id': 'captcha_image',
                           'alt': 'captcha', 'class': 'captcha_image'})
        captcha = captchaUrl['src'].replace("amp;", '')
        r = self.__session.get(captcha, headers=self.__HEADER, proxies=self.__proxy)
        with open("captcha.png", 'wb') as fh:
            fh.write(r.content)
        i = Image.open('captcha.png')
        i.show()
        s = input("输入验证码：")
        result['captcha-solution'] = s
        result['captcha-id'] = captcha.split('?')[1].split('&')[0].replace('id=', '')
        return result

    def login(self):
        r = self.__session.post(self.__LOGIN_URL, data=self.__LOGIN_DATA, proxies=self.__proxy)
        #print(r.text)
        soup = BeautifulSoup(r.text, 'lxml')
        ret = soup.find('div', attrs={'class': 'top-nav-info'})
        if ret:
            ret = ret.find('a', attrs={'class': 'bn-more', 'href': 'https://www.douban.com/accounts/', 'target':'_blank'})
            print("登录成功")
            return
        else:
            result = self.__getCaptcha(soup)
            self.__LOGIN_DATA['captcha-solution'] = result.get('captcha-solution')
            self.__LOGIN_DATA['captcha-id'] = result.get('captcha-id')
            self.login()

    def search(self, movieName):
        movies = {}
        count = 1
        url = self.__SEARCH_URL.replace('MOVIENAME', urllib.parse.quote(movieName))
        r = self.__session.get(url, headers=self.__HEADER, proxies=self.__proxy)
        #print(r.text)
        soup = BeautifulSoup(r.text, 'lxml')
        results = soup.find_all('div', attrs={'class': 'pl2'})
        print(len(results))
        for result in results:
            name = result.find('a', attrs={'class': ''}).get_text().strip()
            link = result.find('a', attrs={'class': ''})['href']
            detail = result.find('p', attrs={'class': 'pl'}).get_text()
            mid = re.search('\d+', link).group()
            movie = MovieDetail(name, link, detail, mid)
            movies[count] = movie
            count += 1
        return movies

    def star(self, mid, grade):
        url1 = 'https://movie.douban.com/subject/ID/?rating=GRADE&ck=q0uf'.replace('ID', mid).replace('GRADE', grade)
        url2 = 'https://movie.douban.com/j/subject/ID/interest?interest=collect&rating=GRADE'.replace('ID', mid).replace('GRADE', grade)
        postUrl = 'https://movie.douban.com/j/subject/ID/interest'.replace('ID', mid)
        data = {'ck':'q0uf',
                'interest':'collect',
                'rating':grade,
                'foldcollect':'F',
                'tags':'',
                'comment':''
                }
        print(url1)
        print(url2)
        print(postUrl)
        self.__session.get(url2, headers=self.__HEADER, proxies=self.__proxy)
        self.__session.post(postUrl, headers=self.__HEADER, proxies=self.__proxy, data=data)
        self.__session.get(url1, headers=self.__HEADER, proxies=self.__proxy)

class MovieDetail(object):
    def __init__(self, name, link, detail, mid):
        self.name = name
        self.link = link
        self.detail = detail
        self.mid = mid

    def __str__(self):
        return self.name

def main():
    douban = Douban()
    douban.login()
    searchs = douban.search('七月与安生')
    for key, value in searchs.items():
        print(key, ": " ,value, value.link)
    option = int(input('选择一个选项： '))
    mid = searchs.get(option).mid
    grade = input('输入一个分数(1-5)')
    douban.star(mid, grade)

if __name__ == "__main__":
    main()
