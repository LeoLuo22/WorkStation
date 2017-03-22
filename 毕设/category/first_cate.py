"""第一次用来分类的
    此次分类了60多万条数据
"""
from utils.mongo import connect

techs = ['开发', '测试', '运维', '数据', '项目管理',
        'PHP', 'JAVA', '研发', 'Developer', '技术', '架构师', '工程师',
         '专家', '前端', 'DBA']
products = ['产品']
designs = ['设计', '插画师', '原画师','交互', 'UI', '视觉', '视频']
markets = ['销售', '商务', '策划', '营销', '公关', '渠道', '库存', '电话']
maintains = ['运营', '客服', '编辑', '文案', '推广', '专员', '处理']
functions = ['审计', '法务', '人事', '助理', '秘书', 'HR']
finances = ['投资', '金融']

categories = {'techs': techs, 'products':products,
              'designs':designs, 'markets':markets,
              'maintains':maintains, 'functions':functions,
              'finances':finances}

def main():
    cursor = connect('lagou', 'jobs')
    cl = connect('lagou', 'categories')

    for category in categories.keys():

        for result in cursor.find():
            item = {}
            name = result.get('name')
            ID = result.get('ID')

            for c in categories.get(category):
                if c in name:
                    item['name'] = name
                    item['ID'] = ID
                    item['category'] = category
                    cl.insert(item)
                    break

if __name__ == '__main__':
    main()
