#互联网细分行业统计
from utils.mongo import connect

jobs = connect('lagou', 'jobs')

counter = {}
companyIDs = set()

for job in jobs.find():
    company = job.get('company')
    companyID = job.get('companyId')
    if companyID in companyIDs:
        continue
    else:
        companyIDs.add(companyID)
    filed = company.get('领域')
    #scale = company.get('规模')
    if filed in counter.keys():
        counter[filed] = counter[filed] + 1
    else:
        counter[filed] = 1

print(counter)
