import lxml
import scrapy
import redis
from bs4 import BeautifulSoup
from scrapy.http import Request
from Lagou.items import LagouItem
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider

class Spider(RedisCrawlSpider):
    name = "lagou"
    host = "https://www.lagou.com"
    redis_key = "lagou:start_urls"

    allowd_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/jobs/2638974.html']

    rules = (
             Rule(LinkExtractor(allow=(r'/jobs/\d+')), callback='parse'),
             )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        job = LagouItem()

        soup = BeautifulSoup(response.body, 'lxml')
        position_head_soup = soup.find('div', attrs={'class': 'position-head'})
        job['ID'] = soup.find('input', attrs={'class': 'erma_codep'}).get('value')
        job['companyId'] = position_head_soup.get('data-companyid')
        #get_text()方法返回标签内的文本内容， name=C软件工程师（西安）
        name = position_head_soup.find('span', attrs={'class': 'name'}).get_text()
        job['name'] = name
        container_soup = soup.find('div', attrs={'class': 'container clearfix', 'id': 'container'})
        #Get the advantage of job
        job_advantage_soup = container_soup.find('dd', attrs={'class': 'job-advantage'})
        job_advantage_des = job_advantage_soup.find('p').get_text()
        job['advantages'] = job_advantage_des

        job_description_soup = container_soup.find('dd', attrs={'class': 'job_bt'})
        requirements = []
        requirements_soup = job_description_soup.find_all('p')
        for requirement in requirements_soup:
            requirements.append(requirement.get_text().replace(' ','').replace('\xa0', ''))
        job['description'] = requirements

        work_addr = container_soup.find('div', attrs={'class': 'work_addr'}).get_text()
        #去除空白和换行
        work_addr = work_addr.replace(' ', '').replace('\n', '')
        job['workLocation'] = work_addr

        #获取公司信息
        company = {}
        company_soup = soup.find('div', attrs={'class': 'content_r'}).find('ul').find_all('li')
        for info in company_soup:
            company[info.find('span').get_text()] = info.get_text().replace('\n', '').replace(' ','')
        company_name = position_head_soup.find('div', attrs={'class': 'company'}).get_text()
        company['公司名称'] = company_name
        job['company'] = company

        job_briefs_soup = soup.find('dd', attrs={'class': 'job_request'})
        job_brief_soup = job_briefs_soup.find_all('span')
        job['salary'] = job_brief_soup[0].get_text().replace('/', '')
        job['location'] = job_brief_soup[1].get_text().replace('/', '')
        job['experience'] = job_brief_soup[2].get_text().replace('/', '')
        job['background'] = job_brief_soup[3].get_text().replace('/', '')
        job['isFulltime'] = job_brief_soup[4].get_text().replace('/', '')

        labels = []
        labels_soup = job_briefs_soup.find('ul', attrs={'class': 'position-label clearfix'}).find_all('li')
        for label in labels_soup:
            labels.append(label.get_text())
        job['labels'] = labels

        idFollows = self.getNextID(soup)
        for ID in idFollows:
            url = "https://www.lagou.com/jobs/%s.html" % ID
            r = redis.Redis(host='127.0.0.1', port=6379)
            r.lpush('lagou:start_urls', url)

        yield job

    def getNextID(self, soup):
        ids = []
        ids_soup = soup.find_all('li', attrs={'class': 'similar_list_item clearfix'})
        for _id in ids_soup:
            ids.append(_id.get('data-jobid'))

        return ids
