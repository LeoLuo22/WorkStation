import requests
import json
import time
from utils.user_agents import get_a_random_ua as ua
from utils.mongo import connect

labels = {'技术': 'tech', '产品': 'product', '设计': 'design', '运营': 'run',
          '市场与销售':'market', '职能': 'function'}

def get_ua():
    """返回一个User-Agent"""
    UA = ua()
    UA['Cookie'] = 'user_trace_token=20161218145926-d389a3999afb42bcbcac1bb930825e19; LGUID=20161218145926-83a61d19-c4ef-11e6-be78-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=C1233D92C6EB59F30C6D984EB5525462; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1489563857,1490008697,1490011886,1490015748; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1490015763; _ga=GA1.2.22814588.1482044363; LGSID=20170320191836-f5fc8c02-0d5e-11e7-9545-5254005c3644; LGRID=20170320211603-5e5f22c0-0d6f-11e7-9545-5254005c3644; TG-TRACK-CODE=hpage_code'

    return UA

def get_payload(companyId, positiontype, pageNo, pageSize):
    """创建传递参数
        @param companyId
         公司ID
        @param type
         职位分类
        @param no
         当前页数
        @param size
         一页显示几个职位
        @return
         A dict
    """
    payload = {}

    payload['companyId'] = companyId
    payload['pageNo'] = pageNo
    payload['pageSize'] = pageSize
    payload['positionFirstType'] = positiontype

    return payload

def get_results(response):
    """返回json中的results
        @param response
         json格式的返回内容
        @param return
         results。字典的列表
    """
    content = response.get('content')
    data = content.get('data')
    page = data.get('page')
    results = page.get('result')

    return results

def get_jobs(results, label):
    """返回分类下的职位数目
        @param results
         一个分类下的全部返回数目
        @param lable
         分类名
        @return
         A dict
    """
    if len(results) == 0:
        return

    positions = []#保存分类下的所有职位信息
    item = {}
    item['count'] = len(results)

    for result in results:
        position = {}

        position['createTime'] = result.get('createTime')
        position['haveDeliver'] = result.get('haveDeliver')
        position['ID'] = result.get('positionId')

        positions.append(position)

    item['positions'] = positions
    item['label'] = label

    return item

def main():
    c = connect('lagou', 'companys')

    companyIds = []
    for result in c.find():
        companyIds.append(result.get('companyId'))

    UA = get_ua()
    url = 'https://www.lagou.com/gongsi/searchPosition.json'

    cursor = connect('lagou', 'positions')

    for companyId in companyIds[0:10000]:
        company = {}
        for label in labels.keys():
            items = []
            for i in range(1, 10):
                payload = get_payload(companyId, label, i, 10)
                response = requests.get(url, params=payload, headers=UA).json()
                time.sleep(0.7)
                results = get_results(response)
                if len(results) == 0:
                    company[labels.get(label)] = get_jobs(items, label)
                    break
                else:
                    items += results

        company['companyId'] = companyId
        print("Get ", companyId)
        cursor.insert(company)

if __name__ == '__main__':
    main()
