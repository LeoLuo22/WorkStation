# -*- coding:utf-8 -*-
__author__ = "Leo Luo"

from bs4 import BeautifulSoup
from PIL import Image
import requests
import lxml
import random
import urllib.parse
import re
import os

class Douban(object):
    def __init__(self):
        self.__LOGIN_DATA = {'source':'movie',
                             'redir':'https://movie.douban.com/',
                             'form_email':'leoluo22@gmail.com',
                             'form_password':'vampire.Leo123',
                             'login':'登录'}
        self.__HEADER = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) ' +
                                      'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                                      'Chrome/50.0.2661.102 Safari/537.36'}
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
            r = requests.get('https://www.baidu.com',
                             proxies=proxy, headers=self.__HEADER, timeout=1)
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
                                             'alt': 'captcha',
                                             'class': 'captcha_image'})
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
        r = self.__session.post(self.__LOGIN_URL,
                                data=self.__LOGIN_DATA,
                                proxies=self.__proxy)
        #print(r.text)
        soup = BeautifulSoup(r.text, 'lxml')
        ret = soup.find('div', attrs={'class': 'top-nav-info'})
        if ret:
            ret = ret.find('a', attrs={'class': 'bn-more',
                                       'href': 'https://www.douban.com/accounts/',
                                       'target':'_blank'})
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
        print("共有", len(results), "个搜索结果")
        for result in results:
            name = result.find('a', attrs={'class': ''}).get_text().strip().replace(' ', '').replace('\n', '')
            link = result.find('a', attrs={'class': ''})['href']
            detail = result.find('p', attrs={'class': 'pl'}).get_text()
            mid = re.search('\d+', link).group()
            movie = MovieDetail(name, link, detail, mid)
            movies[count] = movie
            count += 1
        return movies

    def __saveImg(self, movie):
        mid = movie.mid
        while True:
            if '：' in movie.name:
                movie.name = movie.name.replace('：', '-')
            break
        while True:
            if '/' in movie.name:
                movie.name = movie.name.replace('/', '_')
            break
        url = 'https://movie.douban.com/subject/ID/'.replace('ID', mid)
        r = self.__session.get(url, headers=self.__HEADER, proxies=self.__proxy)
        soup = BeautifulSoup(r.text, 'lxml')
        imgUrl = soup.find('img', attrs={'title': '点击看更多海报'})['src']
        i = self.__session.get(imgUrl, headers=self.__HEADER, proxies=self.__proxy)
        os.chdir('E:\\')
        os.chdir('Movies/Post')
        #print(os.getcwd())
        with open(movie.name + '.jpg', 'wb') as fh:
            fh.write(i.content)

    def star(self, movie, grade):
        mid = movie.mid
        url1 = 'https://movie.douban.com/subject/ID/?rating=GRADE&ck=q0uf'.replace('ID', mid).replace('GRADE', grade)
        url2 = 'https://movie.douban.com/j/subject/ID/interest?interest=collect&rating=GRADE'.replace('ID', mid).replace('GRADE', grade)
        postUrl = 'https://movie.douban.com/j/subject/ID/interest'.replace('ID', mid)
        addUrl = 'https://movie.douban.com/j/doulist/40255131/additem'
        data = {'ck':'q0uf',
                'interest':'collect',
                'rating':grade,
                'foldcollect':'F',
                'tags':'',
                'comment':''
               }
        addData = {'sid':mid,
                   'skind':'1002',
                   'surl':'https://movie.douban.com/subject/ID/'.replace('ID', mid),
                   'comment':'',
                   'sync_to_mb':'',
                   'ck':'q0uf'
                  }
        #print(url1)
        #print(url2)
        #print(postUrl)
        self.__session.get(url2, headers=self.__HEADER, proxies=self.__proxy)
        self.__session.post(postUrl, headers=self.__HEADER, proxies=self.__proxy, data=data)
        self.__session.post(addUrl, headers=self.__HEADER, proxies=self.__proxy, data=addData)
        self.__session.get(url1, headers=self.__HEADER, proxies=self.__proxy)
        self.__saveImg(movie)

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
    while True:
        mName = input('输入电影名：')
        searchs = douban.search(mName)
        for key, value in searchs.items():
            print(key, ": ", value)#, value.link)
        option = int(input('选择一个选项： '))
        movie = searchs.get(option)
        grade = input('输入一个分数(1-5)：')
        douban.star(movie, grade)

if __name__ == "__main__":
    main()
