import pymongo

def clean(salary):
    """清洗薪资数据
        @param salary
         原始的工资数据
        @return
          A list, 每个数据是float型,分别是最高工资
          和最低工资
    """
    #case1: 5k-8k, 5K-8K
    if '-' in salary and '以' not in salary:
        salary_range = salary.split('-')
        salary_low = float(salary_range[0].replace('k', '000').replace('K', '000'))
        salary_high = float(salary_range[1].replace('k', '000').replace('K', '000'))
        return [salary_low, salary_high]

    #case2: 5k-8k以上
    elif '以' in salary:
        s = salary.split('以')

        if '-' in s[0]:
            return clean(s[0])
        else:
            slr = float(s[0].replace('k', '000').replace('K', '000'))
            return [slr, slr]

    #case3: 100k+
    if '+' in salary:
        s = salary.split('+')

        if '-' in s[0]:
            return clean(s[0])
        else:
            slr = float(s[0].replace('k', '000').replace('K', '000'))
            return [slr, slr]

def main():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.lagou
    collection = db.jobs

    results = collection.find()

    try:
        for result in results:
            if result.get('salary_avg'):
                continue

            ID = result.get('ID')
            salary = result.get('salary')

            salary_range = clean(salary)

            try:
                salary_low = salary_range[0]
                salary_high = salary_range[1]
                salary_avg = (salary_low + salary_high) / 2
            except TypeError:
                print(ID)
                return

            db.salary.insert({'ID': ID}, {'$set': {'salary_low': salary_low,
                              'salary_high': salary_high, 'salary_avg': salary_avg}})
    except pymongo.errors.CursorNotFound:
        return main()


if __name__ == '__main__':
    main()
