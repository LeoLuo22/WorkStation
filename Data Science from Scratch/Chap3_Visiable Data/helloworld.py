from matplotlib import pyplot as plt
from collections import Counter

"""折线图
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdps = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdps, color='green', marker='o', linestyle='solid')

plt.title('GDP')

plt.xlabel('year')
plt.ylabel('$billion')
plt.show()
"""

"""直方图
movies = ['Anne Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
number_oscars = [5, 11, 3, 8 ,10]

#条形的默认宽度是0.8，对左侧坐标加上0.10
#每个条形就放置在中心
xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, number_oscars)

plt.ylabel('Number')
plt.title('Favorate')

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()
"""
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x - 4 for x in histogram.keys()],#每个条形向左侧移动四个单位
        histogram.values(),#给每个条形设置正确的高度
        8)#每个条形的宽度设置为8

plt.axis([-5, 105, 0, 5]) #x轴从-5到105，y轴取值0到5

plt.xticks([10 * i for i in range(11)]) #x轴标记为0，10...100
plt.xlabel('十分')
plt.ylabel('学生数')
plt.title('考试分数分布图')
plt.show()
