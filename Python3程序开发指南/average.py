#-*-coding:utf-8-*-
#测试
def get_value(msg):
    values = []
    while True:
        try:
            i = input(msg)
            if not i:
                return values
            val = int(i)
            values.append(val)
        except TypeError as err:
            print(err)
        except ValueError as err:
            print(err)
    return values
#Bubble sort algrithm
def my_sort(liter):
    exchange = len(liter) - 1
    bound = len(liter) - 1
    while exchange != 0:
        bound = exchange
        exchange = 0
        for j in range(0,bound):
            if liter[j] > liter[j+1]:
                liter[j],liter[j+1] = liter[j+1],liter[j]
                exchange = j
    return liter

def find_mid(m_lst):
    if len(m_lst) % 2 == 0:
        return (m_lst[int(len(m_lst)/2)] + m_lst[(int(len(m_lst)/2)-1)]) / 2
    else:
        return m_lst[int((len(m_lst)-1)/2)]

if __name__ == '__main__':
    numbers = get_value('enter a number or Enter to finish: ')
    if len(numbers) != 0:
        print("numbers: ",numbers,"count: ",len(numbers),"sum: ",sum(numbers),"highest: ",max(numbers),"lowest",min(numbers),"mean: ",sum(numbers)/len(numbers))
    else:
        print("No input")
    print("After sort: ",my_sort(numbers))
    print("middle value is: ",find_mid(my_sort(numbers)))

