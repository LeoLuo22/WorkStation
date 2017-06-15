#获得城市不同发展阶段的公司所占比例
from utils.mongo import connect

jobs = connect('lagou', 'jobs')

#cities = ('北京', '上海', '广州', '深圳', '杭州')#保存要统计的城市
cities = ('成都', '武汉', '南京', '西安', '长沙')
counter = {}#用来保存城市
company_ids = set()#用于过滤重复公司

for job in jobs.find():
    company_id = job.get('companyId')
    if company_id in company_ids:
        continue
    else:
        company_ids.add(company_id)

    company = job.get('company')
    city = job.get('location').replace(' ', '')
    dev = company.get('发展阶段').replace('发展阶段', '')

    if city in cities:
        if city in counter.keys():#如果已经存在
            if dev in counter[city].keys():#如果发展阶段已经存在城市的字典里
                counter[city][dev] += 1
            else:#如果发展阶段没有存在
                counter[city][dev] = 1
        else:#如果城市还未存在
            counter[city] = {}#置为空字典
    else:
        continue

total = 0#用来保存公司数目
for key, value in counter.items():
    count = 0#保存未融资的公司数目
    for v in value.values():
        total += v
    print(key, 'Total:', total)
    for k, v in value.items():
        if k in ('未融资', '不需要融资', ' ') or k == ' ' or k is None:
            count += v
            continue
        rate = round(v/total, 4)
        print(k, v, str(rate * 100)[0:5], '%')
    _rate = round(count/total, 4)
    print('未融资:', count, str(_rate*100)[0:5], '%')
    total = 0


