"""This is to discover the connection
    between diploma and job
"""
from utils import mongo

jobs = mongo.connect('lagou', 'jobs')
backgrounds = mongo.connect('lagou', 'backgrounds')

items = {}#要插入到backgrounds的数据

count = 0#计数器

diplomas = []#一共有多少学历要求

def main():
    results = jobs.find()

    for result in results:
        diploma = result.get('background')

        if diploma not in items.keys():
            items[diploma] = 1
        else:
            items[diploma] = items.get(diploma) + 1

    print(items)

if __name__ == '__main__':
    main()
