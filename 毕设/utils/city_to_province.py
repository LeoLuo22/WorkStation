from utils.mongo import connect
from utils.mysql import MySql

mysql = MySql('locations', 'leo', 'mm123456', collection='new_provices')
locations = connect('lagou', 'location')

cities = []
try:
    for location in locations.find():
        city = location.get('city')
        new_city = city + '%'
        result = mysql.find(mohu=True, city=new_city)
        try:
            province = result.get('Province')
        except Exception:
            print(city)
        locations.update_one({'city':city}, {'$set':{'province':province}})
finally:
    mysql.close()

