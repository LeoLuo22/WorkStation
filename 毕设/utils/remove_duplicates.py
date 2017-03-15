import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.lagou
collection = db.duplicates


def main():
    duplicates = {}
    results = collection.find()

    for result in results:
        duplicates[result.get('ID')] = int(result.get('count')-1)

    col = db.jobs
    for key, value in duplicates.items():
        for i in range(0, value):
            col.delete_one({"ID": key})

if __name__ == '__main__':
    main()

