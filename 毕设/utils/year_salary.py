#互联网公司工作年限与对应年薪
from utils.mongo import connect

categories = connect('lagou', 'categories')
jobs = connect('lagou', 'jobs')
salarys = connect('lagou', 'salarys')

product = {}
design = {}
function = {}
market = {}
finance = {}
maintain = {}
tech = {}

def count(d, ID):
    """统计计数不同分类对经验的要求与年薪
        @param d
         7种字典
        @param ID
         职位的ID
        @postcondition
         对应的字典包含不同年限的计数，年薪，平均年薪
    """
    year = jobs.find_one({'ID': ID}).get('experience')#获取工作经验
    salary = salarys.find_one({'ID': ID}).get('salary_avg')#获取平均月薪
    annual_salary = salary * 12#得到年薪

    if year in d.keys():
        d[year]['count'] += 1
        d[year]['salarys'] += salary
    else:
        d[year] = {}
        d[year]['count'] = 1
        d[year]['salarys'] = salary

    for key in d.keys():
        key = d.get(key)
        key['annual'] = key['salarys'] // key['count']

def main():
    for category in categories.find():
        cate = category.get('category')
        ID = category.get('ID')
        if cate == 'designs':
            count(design, ID)
        elif cate == 'finances':
            count(finance, ID)
        elif cate == 'functions':
            count(function, ID)
        elif cate == 'products':
            count(product, ID)
        elif cate == 'maintains':
            count(maintain, ID)
        elif cate == 'techs':
            count(tech, ID)
        else:
            count(market, ID)

    print(design)
    print(finance)
    print(function)
    print(product)
    print(tech)
    print(maintain)
    print(market)

if __name__ == '__main__':
    main()




