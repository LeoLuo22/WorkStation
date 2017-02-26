"""This module is for
    delete unuseful proxy
    Usage:
     wash(url=None, file=None, output=None)
"""
import os
import requests
import lxml
from bs4 import BeautifulSoup

HEADER = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def has_bing(proxy=None):
    """See whether it can open Bing with
        the given proxy
        @param proxy
         Proxy that to test.eg{'http':'http://11'}
        @return
         True if it can open Bing through proxy
    """
    response = requests.get('https://www.bing.com', headers=HEADER, timeout=1, proxies=proxy)
    soup = BeautifulSoup(response.text, 'lxml')
    bing = soup.find('div', attrs={'class': 'hp_sw_logo hpcLogoWhite'})
    #print(bing.get_text())
    if bing.get_text() == '必应':
        return True
    return False

def wash(url=None, file=None, output=None):
    """wash proxies and write to file
        @param url
         Like http://1.1.1.1:80
        @param file
         Open the file of proxies
        @param output
         Filename of the filename, default is original filename
    """
    proxy = {}

    if url:
        proxy['http'] = url
        flag = has_bing(proxy)
        if flag:
            print(url, " is OK! ")
        else:
            print(url, " is BAD! ")

        return

    elif file:
        availables = []
        with open(file, 'r') as original:
            for line in original:
                line = line.replace('\n', '')
                proxy['http'] = line
                flag = has_bing(proxy)
                if flag:
                    print(line, "is OK! ")
                    availables.append(line)

        os.remove(file)

        if not output:
            with open(file, 'a') as result:
                for available in availables:
                    result.write(available + '\n')

        else:
            with open(output+'.txt', 'a') as result:
                for available in availables:
                    result.write(available + '\n')
        return

def main():
    """Main
    """
    #wash(url='http://121.31.199.91:6675')
    wash(file='new_proxies.txt')

if __name__ == '__main__':
    main()
