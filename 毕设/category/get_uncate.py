"""获取还未分类的ID和名字
"""
from utils.mongo import connect

def used():
    cursor = connect('lagou', 'categories')
    useds = []

    for result in cursor.find():
        useds.append(result.get('ID'))

    return useds

def main():
    useds = used()
    unuseds = []
    cursor = connect('lagou', 'jobs')
    cl = connect('lagou', 'uncate')
    for result in cursor.find():
        name = result.get('name')
        ID = result.get('ID')

        if ID in useds:
            continue
        else:
            item = {}
            item['ID'] = ID
            item['name'] = name
            cl.insert(item)

if __name__ == '__main__':
    main()
