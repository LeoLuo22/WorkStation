import requests
from bs4 import BeautifulSoup
import lxml
from collections import OrderedDict
def parse(webpage):
    """Parse webpage
    @param webpage
     raw html
    """
    job = OrderedDict()
    soup = BeautifulSoup(webpage, 'lxml')
    position_head_soup = soup.find('div', attrs={'class': 'position-head'})
    #get_text()方法返回标签内的文本内容， name=C软件工程师（西安）
    name = position_head_soup.find('span', attrs={'class': 'name'}).get_text()
    job['name'] = name
    container_soup = soup.find('div', attrs={'class': 'container clearfix', 'id': 'container'})
    #Get the advantage of job
    job_advantage_soup = container_soup.find('dd', attrs={'class': 'job-advantage'})
    job_advantage_name = job_advantage_soup.find('span', attrs={'class': 'advantage'}).get_text()
    job_advantage_des = job_advantage_soup.find('p').get_text()
    job[job_advantage_name] = job_advantage_des

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
    job['职位描述'] = requirements

    work_addr = container_soup.find('div', attrs={'class': 'work_addr'}).get_text()
    #去除空白和换行
    work_addr = work_addr.replace(' ', '').replace('\n', '')
    job['工作地址'] = work_addr

    #获取公司信息
    company = {}
    company_soup = soup.find('div', attrs={'class': 'content_r'}).find('ul').find_all('li')
    for info in company_soup:
        company[info.find('span').get_text()] = info.get_text().replace('\n', '').replace(' ','')
    company_name = position_head_soup.find('div', attrs={'class': 'company'}).get_text()
    company['公司名称'] = company_name
    job['公司'] = company

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

    print(job)




def main():
    parse(requests.get('https://www.lagou.com/jobs/2771322.html?source=viewrec&i=position_rec-3').text)
    parse(requests.get('https://www.lagou.com/jobs/2638974.html').text)

if __name__ == '__main__':
    main()
