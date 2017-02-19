import lxml
import scrapy
from bs4 import BeautifulSoup
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from Lagou.items import LagouItem
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider

class Spider(RedisCrawlSpider):
    name = "lagou"
    host = "https://www.lagou.com"
    redis_key = "lagou:start_urls"

    #allowd_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/jobs/2638974.html']

    """
    rules = (
             Rule(LinkExtractor(allow=(r'/jobs/\d+')), callback='parse'),
             )
    """

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
        #job_advantage_name = job_advantage_soup.find('span', attrs={'class': 'advantage'}).get_text()
        job_advantage_des = job_advantage_soup.find('p').get_text()
        job['advantages'] = job_advantage_des

        #Job description should also be a dict, as it has responsibility as requirements
        #Like: job{'职位描述': {'岗位职责': 'eee', '岗位要求': 'aaa'}, 'name': 'aaa'}
        #以下用a, b, c分别代表职位描述等
        job_description_soup = container_soup.find('dd', attrs={'class': 'job_bt'})
        """
        由于网页结构中标签不一致且大量使用<p>导致不能使用上述方法，只能找到所有descrition
        a = job_description_soup.find('h3', attrs={'class': 'description'}).get_text()
        b = job_description_soup.find('p').get_text()
        responsibilities_soup = job_description_soup.find('ol', attrs={'class': ' list-paddingleft-2'}).find_all('p')
        responsibilities = []
        for responsibility in responsibilities_soup:
            responsibilities.append(responsibility.get_text())
        """
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

        yield job

        #urlFollows = "http://weibo.cn/%s/follow" % ID  # 爬第一页的关注，加入待爬队列
        idFollows = self.getNextID(soup)
        for ID in idFollows:
            url = "https://www.lagou.com/jobs/%s.html" % ID
            yield Request(url=url, callback=self.parse)

    def getNextID(self, soup):
        ids = []
        ids_soup = soup.find_all('li', attrs={'class': 'similar_list_item clearfix'})
        for _id in ids_soup:
            ids.append(_id.get('data-jobid'))

        return ids
