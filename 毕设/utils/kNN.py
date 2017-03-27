"""使用kNN算法预测其它城市的互联网公司数目"""
import random
import operator
from math import radians, cos, sin, asin, sqrt
from utils.mongo import connect
from utils.mysql import MySql

cursor = connect('lagou', 'location')

def loadData():
    """分割数据集
        @param split ->训练数据集所占比例
    """
    trainSet = []
    testSet = []

    for result in cursor.find():
        value = result.get('company_nums')
        location = result.get('location')
        try:
            lng = location.get('lng')
            lat = location.get('lat')
        except AttributeError:
            print(result.get('city'))
            return
        dataset = [lng, lat, value]
        trainSet.append(dataset)
        """
        if random.random() < 0.67:
            trainSet.append(dataset)
        else:
            testSet.append(dataset)
        """

    #return (trainSet, testSet)
    return trainSet

def distance(lon1, lat1, lon2, lat2):
    """得到两坐标之间距离
        @param lon1 -> 经度1
        @param lat1 -> 纬度1
        @param lon2 -> 经度2
        @param lat2 -> 纬度2
        @return
         距离 米
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371#地球半径
    return c * r * 1000

#print(distance(109.934208153795, 33.8739073950852,
               #111.143156602348, 37.5273160969626))

def get_neighbors(trainSet, instance, k):
    """获取一个坐标的近邻
        @param trainSet -> 训练集
        @param instance -> 要测试的坐标
        @param k -> 近邻的数目
        @return -> list, 最近的k个邻居
    """
    distances = []
    for x in range(len(trainSet)):
        dist = distance(instance[0], instance[1],
                        trainSet[x][0], trainSet[x][1])
        distances.append((trainSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])

    return neighbors

def predict(neighbors):
    """预测
        @param neighbors -> 最近的几个邻居
    """
    #print(neighbors)
    votes = {}
    size = len(neighbors)
    nums = []
    for x in range(size):
        num = neighbors[x][-1]#获得公司数目
        if num in votes:
            votes[num] += 1
        else:
            votes[num] = 1
        #nums.append(num)
        #nums.append(num)

    sorted_votes = sorted(votes.items(),
                          key=operator.itemgetter(1),
                          reverse=True)

    return sorted_votes[0][0]
    #return value // (len(nums) - 2)
def get_accuracy(testSet, predictions):
    """计算算法准确度
        @param testSet -> 测试集
        @param predictions -> 预测集
        @return -> float, 准确度
    """
    correct = 0
    for i in range(len(testSet)):
        if abs(testSet[i][-1] - predictions[i]) < 10:
            correct += 1

    return (correct/len(testSet)) * 100

def main():
    trainSet = loadData()
    mysql = MySql('locations', 'leo', 'mm123456', collection='new_provices')
    cursor = connect('lagou', 'predicts')
    results = mysql.find()

    for result in results:
        province = result.get('Province')
        city = result.get('city')
        county = result.get('county')
        lng = float(result.get('Longitude'))
        lat = float(result.get('latitude'))
        neighbors = get_neighbors(trainSet, [lng, lat], 1)
        assume = predict(neighbors)
        cursor.insert({'province':province, 'city':city, 'county':county,
                        'lng': lng, 'lat': lat, 'value': assume})

    mysql.close()

if __name__ == '__main__':
    main()
