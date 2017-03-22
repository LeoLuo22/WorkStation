"""第一次用来分类的
    此次分类了60多万条数据
"""
from utils.mongo import connect

techs = ['Java', '.NET', 'HTML5', 'C#',
         'Android', 'C++', 'Linux',
         'Hadoop', 'Node.js', 'U3D',
         'iOS', 'html5', 'Engineer', 'MySQL',
         '程序员', 'Python']
products = ['产品', '项目', 'UE']
designs = ['动画', '3D', '剪辑', '主策']
markets = ['广告', '拓展', '客', '市场', 'BD', 'bd', '商户', '采购', '城市',
           '外贸', '社区', '餐饮']
maintains = ['SEM', 'sem', 'Sem', 'COO', '媒介', '活动', '仓储', '品牌']
functions = ['人力', '核算', '人资', '会计', '财务', '前台', '翻译', '薪资', '培训',
             '政策', '行政']
finances = ['信用', '风控', '资产', '理财', '证券']

categories = {'techs': techs, 'products':products,
              'designs':designs, 'markets':markets,
              'maintains':maintains, 'functions':functions,
              'finances':finances}

def main():
    usedID = []
    cursor = connect('lagou', 'uncate')
    cl = connect('lagou', 'categories')

    for category in categories.keys():

        for result in cursor.find():
            item = {}
            name = result.get('name')
            ID = result.get('ID')
            if ID in usedID:
                continue

            for c in categories.get(category):
                if c in name:
                    usedID.append(ID)
                    item['name'] = name
                    item['ID'] = ID
                    item['category'] = category
                    cl.insert(item)
                    break

if __name__ == '__main__':
    main()
