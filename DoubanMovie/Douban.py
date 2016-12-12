# -*- coding:utf-8 -*-
__author__ = "Leo Luo"

from bs4 import BeautifulSoup
import requests
import lxml
from PIL import Image
import random

BASE_URL = "https://accounts.douban.com/login?source=movie"
LOGIN_URL = "https://accounts.douban.com/login"
LOGIN_DATA = { 'source':'movie',
                                'redir':'https://movie.douban.com/',
                                'form_email':'leoluo22@gmail.com',
                                'form_password':'vampire.Leo123',
                                'login':'登录'}
HEADER = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
session = requests.Session()
session.get(BASE_URL)

proxiesList = []
flag = False
"""
class Douban(object):
    def __init__(self, proxiesList=None):
        super.__init__()
        self.__proxiesList = proxiesList

    def __getProxies(self):
        with open('proxies.txt')
"""
def getProxies():

    with open('proxies.txt', 'r') as fh:
        for line in fh:
            line = line.replace('\n', '')
            proxiesList.append(line)
    return

def test(url):
    proxy = {'http': url}
    try:
        r = requests.get('https://www.baidu.com', proxies=proxy, headers=HEADER, timeout=1)
    except Exception:
        return False
    if r.status_code == 200:
        return True
    return False

def proxy(i):
    url = proxiesList[i]
    if test(url):
        return url
    else:
        i = random.randint(1, 99)
        proxy(i)

def getCaptcha(soup, _proxy):
    result = {}
    captchaUrl = soup.find('img', attrs={'id': 'captcha_image',
                           'alt': 'captcha', 'class': 'captcha_image'})
    captcha = captchaUrl['src'].replace("amp;", '')
    r = session.get(captcha, headers=HEADER, proxies=_proxy)
    with open("captcha.png", 'wb') as fh:
        fh.write(r.content)
    i = Image.open('captcha.png')
    i.show()
    s = input("输入验证码：")
    result['captcha-solution'] = s
    result['captcha-id'] = captcha.split('?')[1].split('&')[0].replace('id=', '')
    return result


def login(logindata, _proxy):
    r = session.post(LOGIN_URL, data=logindata, proxies=_proxy)
    #print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
    #username = soup.find('a', attrs={'target':"_blank", 'href':"https://www.douban.com/accounts/", 'class':"bn-more"})
    ret = soup.find('div', attrs={'class': 'top-nav-info'})
    if ret:
        ret = ret.find('a', attrs={'class': 'bn-more', 'href': 'https://www.douban.com/accounts/', 'target':'_blank'})
        print("登录成功")
        return
    else:
        result = getCaptcha(soup, _proxy)
        LOGIN_DATA['captcha-solution'] = result.get('captcha-solution')
        LOGIN_DATA['captcha-id'] = result.get('captcha-id')
        login(LOGIN_DATA, _proxy)


def main():
    getProxies()
    url = proxy(88)
    _proxy = {'http': url}
    if login(LOGIN_DATA, _proxy):

        print(login(LOGIN_DATA, _proxy))
    #print(flag)
    #print(flag)



if __name__ == "__main__":
    main()
