# -*- coding:utf-8 -*-
__author__ = "Leo Luo"

from bs4 import BeautifulSoup
import requests
import lxml
from PIL import Image
import random

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
        self.__session = requests.Session()
        self.__session.get(self.__BASE_URL, headers=self.__HEADER)
        self.__proxiesList = []
        self.__proxy = {}
        self.__getProxies()
        self.__getproxy(9)


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

def main():
    douban = Douban()
    douban.login()

if __name__ == "__main__":
    main()
