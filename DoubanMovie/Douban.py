# -*- coding:utf-8 -*-
"""Update 3/13/2017
    1. bugfix: 无法添加到豆列
    2. bugfix: 无法评分
    3. remove proxy
"""
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
    def __init__(self, username=None, passwd=None):
        """
            创建一个登录用户
            @param username
             用户名，一般为邮箱格式
            @param passwd
             密码
        """
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

    def __getCaptcha(self, soup):
        """
            获取登陆时的验证码
        """
        result = {}
        captchaUrl = soup.find('img', attrs={'id': 'captcha_image',
                                             'alt': 'captcha',
                                             'class': 'captcha_image'})
        captcha = captchaUrl['src'].replace("amp;", '')
        r = self.__session.get(captcha, headers=self.__HEADER)
        with open("captcha.png", 'wb') as fh:
            fh.write(r.content)
        i = Image.open('captcha.png')
        i.show()
        s = input("输入验证码：")
        result['captcha-solution'] = s
        result['captcha-id'] = captcha.split('?')[1].split('&')[0].replace('id=', '')
        return result

    def login(self):
        """
            登录豆瓣
        """
        r = self.__session.post(self.__LOGIN_URL,
                                data=self.__LOGIN_DATA)
        soup = BeautifulSoup(r.text, 'lxml')
        ret = soup.find('div', attrs={'class': 'top-nav-info'})
        if ret:
            a_lable = ret.find('a', attrs={'class': 'bn-more',
                                       'href': 'https://www.douban.com/accounts/',
                                       'target':'_blank'})
            user = a_lable.find('span').get_text().split('的')[0]
            print("欢迎你，", user)
            return
        else:
            result = self.__getCaptcha(soup)
            self.__LOGIN_DATA['captcha-solution'] = result.get('captcha-solution')
            self.__LOGIN_DATA['captcha-id'] = result.get('captcha-id')
            self.login()

    def search(self, movieName):
        """搜索
            @param movieName
             电影名
            @return
             字典。包含序号和对应的搜索结果
        """
        movies = {}
        count = 1
        url = self.__SEARCH_URL.replace('MOVIENAME', urllib.parse.quote(movieName))
        r = self.__session.get(url, headers=self.__HEADER)
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
        r = self.__session.get(url, headers=self.__HEADER)
        soup = BeautifulSoup(r.text, 'lxml')
        imgUrl = soup.find('img', attrs={'title': '点击看更多海报'})['src']
        i = self.__session.get(imgUrl, headers=self.__HEADER)
        os.chdir('E:\\')
        os.chdir('Movies/Post')
        #print(os.getcwd())
        with open(movie.name + '.jpg', 'wb') as fh:
            fh.write(i.content)

    def star(self, movie, grade):
        """
            给电影打分
            @param movie
             MovieDetail object
            @param grade
             分数
        """
        link = movie.link
        mid = movie.mid#电影的ID

        url1 = 'https://movie.douban.com/subject/ID/?rating=GRADE&ck=IK2M'.replace('ID', mid).replace('GRADE', grade)
        url2 = 'https://movie.douban.com/j/subject/ID/interest?interest=collect&rating=GRADE'.replace('ID', mid).replace('GRADE', grade)
        postUrl = 'https://movie.douban.com/j/subject/ID/interest'.replace('ID', mid)
        addUrl = 'https://movie.douban.com/j/doulist/40255131/additem'

        star_data = {'ck':'IK2M',
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
                   'ck':'IK2M'
                  }

        self.__session.get(url2, headers=self.__HEADER)
        self.__session.post(postUrl, headers=self.__HEADER, data=star_data)
        self.__session.post(addUrl, headers=self.__HEADER, data=addData)
        self.__session.get(url1, headers=self.__HEADER)
        self.__saveImg(movie)

        #判断是否添加成功
        if not self.is_add_success(link):
            print("请升级程序。")
            print("https://movie.douban.com/subject/ID/?rating=GRADE&ck=LMIE，一般查看豆瓣把LMIE替换为其他什么")

        #判断是否打分成功
        if not self.isStar(link, grade):
            print("请升级程序。")
            print("https://movie.douban.com/subject/ID/?rating=GRADE&ck=LMIE，一般查看豆瓣把LMIE替换为其他什么")
            return

    def is_add_success(self, link):
        """判断是否成功添加到豆列
            @param movieID
             电影的链接
            @return
             成功了返回True
        """
        doulie_url = 'https://www.douban.com/doulist/40255131/'

        response = self.__session.get(doulie_url, headers=self.__HEADER)

        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find('div', attrs={'class': 'doulist-item'})
        href = div.find('a', attrs={'target': '_blank'}).get('href')

        if href == link:
            return True

        return False

    def isStar(self, link, grade=None):
        """判断是否打分成功
            @param link
             影片链接
            @param grade
             分数
            @return
             打分成功返回True
        """
        response = self.__session.get(link, headers=self.__HEADER)

        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find('div', attrs={'class': 'j a_stars'})
        #rateword = div.find('span', attrs={'id': 'rateword'}).get_text()
        try:
            rate = div.find('input', attrs={'id': 'n_rating'}).get('value')
        except AttributeError:
            print("你尚未标记这部电影")
            return

        if grade == None:
            print("你当前打的分数为：", rate)
            return

        if rate == grade:
            return True

        return False

class MovieDetail(object):
    def __init__(self, name, link, detail, mid):
        """包含影片信息的对象
            @param name
             影片名 eg: 无名女尸/验尸官(台)/尸检无名女尸
            @param link
             影片链接 eg: https://movie.douban.com/subject/26339213/
            @param detail
             详情 包含主演导演等
            @param mid
             means movie ID, 影片的ID eg: 26339213
        """
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
            print(key, ": ", value)
        option = int(input('选择一个选项： '))
        movie = searchs.get(option)
        douban.isStar(movie.link)
        grade = input('输入一个分数(1-5)：')
        douban.star(movie, grade)

if __name__ == "__main__":
    main()
