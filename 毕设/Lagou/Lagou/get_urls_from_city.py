"""This module is to get urls
   from https://www.lagou.com/jobs/allCity.html.
   And add them to redis
   @warning
    time.sleep(1)
"""
import time
import random
import requests
import redis
import urllib
import json
import lxml
from bs4 import BeautifulSoup
from utils import user_agents
from collections import OrderedDict
from utils import proxylib

proxy = {}
proxy['http'] = 'http://183.95.80.165:8080'

def get_city():
    """
        从allCity获取每个城市的url.
        @return
         dict.形式为{'北京': url}
    """
    #cities = {}

    UA = {}
    UA['User-Agent'] = random.choice(user_agents.UserAgents)

    BASE = 'https://www.lagou.com/jobs/list_?&city={0}'

    allCity_url = 'https://www.lagou.com/jobs/allCity.html'
    allCity_json = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json?city='
    response = requests.get(allCity_json, headers=UA, proxies=proxy)

    jsons = response.json()
    content = jsons.get('content')
    data = content.get('data')
    allCitySearchLabels = data.get('allCitySearchLabels')

    for dicts in allCitySearchLabels.values():
        for d in dicts:
            name = d.get('name')#获得城市名
            quote = urllib.request.quote(name)
            #cities[name] = BASE.format(quote)
            yield quote

def parse_city(city):
    base = 'https://www.lagou.com/jobs/list_?&px=default&city={0}'.format(city)
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city={0}&needAddtionalResult=false'.format(city)

    session = requests.Session()

    data = OrderedDict()
    data['first'] = 'true'
    data['pn'] = '1'
    data['kd'] = ''

    UA = {}
    UA['X-Anit-Forge-Code'] = '0'
    UA['X-Anit-Forge-Token'] = 'None'
    UA['X-Requested-With'] = 'XMLHttpRequest'
    UA['User-Agent'] = random.choice(user_agents.UserAgents)

    r = session.get(base, headers=UA, proxies=proxy)
    response = session.post(url, headers=UA, data=data, proxies=proxy)

    jsons = response.text
    return jsons
    content = jsons.get('content')
    print(content)

def main():
    city = get_city()
    print(parse_city(next(city)))


if __name__ == '__main__':
    main()
