#-*-coding:utf-8-*-
__author__ = "Leo Luo"

def cal(values):
    _sum = 0.0
    for value in values:
        _sum += value
    return _sum

def main():
    flag = 0.0
    positive = []
    negative = []
    while  True:
        value = input("请输入值，用正负号表示（回车结束输入）：")
        if len(value) == 0:
            break
        value = float(value)
        if value > 0.0:
            positive.append(value)
        else:
            negative.append(abs(value))
    positive_sum = cal(positive)
    negative_sum = cal(negative)
    print("正: {0}  负: {1}  余额:{2}".format(positive_sum, negative_sum, round(positive_sum-negative_sum, 2)))

if __name__ == "__main__":
    main()
