import redis
from pymongo import MongoClient
import random

client = MongoClient('localhost', 27017)
db = client['lagou']
used_IDS = []
for item in db.jobs.find():
    used_IDS.append(item.get('ID'))

used_IDS = set(used_IDS)

r = redis.Redis(host='127.0.0.1', port=6379)

def main():
    j = 0
    while True:
        i = random.randrange(800000, 2000000)
        if j >= 22222:
            return
        if str(i) not in used_IDS:
            j += 1
            url = "https://www.lagou.com/jobs/{0}.html".format(i)
            r.lpush('lagou:start_urls', url)
            used_IDS.add(str(i))

if __name__ == '__main__':
    main()
