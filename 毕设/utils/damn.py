from utils.mongo import connect

categories = connect('lagou', 'categories')
jobs = connect('lagou', 'jobs')
salarys = connect('lagou', 'salarys')

design = {}
finannce = {}
function = {}
product = {}
maintain = {}
tech = {}
market = {}

for result in categories.find():
    category = result.get('category')
    ID = result.get('ID')
    experience = jobs.find_one({'ID': ID}).get('experience')
    salary = salarys.find_one({'ID': ID}).get('salary_avg')
    if category == 'designs':
        if experience in design.keys():
            design[category] = design[category].append(salary)
            continue
        else:
            design[category] = []
            continue

    elif category == 'finances':
        if experience in finannce.keys():
            finannce[category] = finannce[category].append(salary)
            continue
        else:
            finannce[category] = []
            continue

    elif category == 'functions':
        if experience in function.keys():
            function[category] = function[category].append(salary)
            continue
        else:
            function[category] = []
            continue

    elif category == 'products':
        if experience in product.keys():
            product[category] = product[category].append(salary)
            continue
        else:
            product[category] = []
            continue

    elif category == 'maintains':
        if experience in maintain.keys():
            maintain[category] = maintain[category].append(salary)
            continue
        else:
            maintain[category] = []
            continue

    elif category == 'techs':
        if experience in tech.keys():
            tech[category] = tech[category].append(salary)
            continue
        else:
            tech[category] = []
            continue

    else:
        if experience in market.keys():
            market[category] = market[category].append(salary)
            continue
        else:
            market[category] = []
            continue

print("designs")
for key, value in design:
    print(key, ':', sum(value)//len(value))
print("finances")
for key, value in finannce:
    print(key, ':', sum(value)//len(value))
print('functions')
for key, value in function:
    print(key, ':', sum(value)//len(value))
print('products')
for key, value in product:
    print(key, ':', sum(value)//len(value))
print('maintains')
for key, value in maintain:
    print(key, ':', sum(value)//len(value))
print('techs')
for key, value in tech:
    print(key, ':', sum(value)//len(value))
print('markets')
for key, value in market:
    print(key, ':', sum(value)//len(value))
