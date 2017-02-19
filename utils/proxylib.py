import requests
from bs4 import BeautifulSoup
import lxml

HEADER = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

starturl = 'http://www.kuaidaili.com/free/inha/1/'

urls = []

def getUrl():
    for i in range(1, 200):
        url = starturl.replace("1", str(i))
        r =requests.get(url, headers=HEADER)
        rst = wash(r.text)
        if rst:
            print(rst)
            with open('proxies.txt', 'a') as fh:
                fh.write(rst + '\n')
    return

def wash(urlRaw):
    ips = []
    ports = []
    urlSoup = BeautifulSoup(urlRaw, 'lxml')
    ipsRaw = urlSoup.find_all('td', attrs={'data-title': 'IP'})
    portsRaw = urlSoup.find_all('td', attrs={'data-title': 'PORT'})

    for i in range(len(ipsRaw)):
        url = "http://" + ipsRaw[i].get_text() + ":" + portsRaw[i].get_text()
        if test(url):
            return url
        return

def test(url):
    proxy = {'http': url}
    try:
        r = requests.get('https://www.baidu.com', proxies=proxy, headers=HEADER, timeout=2)
    except Exception:
        return False
    if r.status_code == 200:
        return True
    return False

def main():

    with open('proxies.txt', 'r') as fh:
        for line in fh:
            print(line.replace('\n', ''))

if __name__ == '__main__':
    main()
