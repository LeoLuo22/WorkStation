#-*- coding:utf-8 -*-
#__author__: Leo Luo

import sys
import collections
import math

Statistics = collections.namedtuple("Statistics",
                                    "mean mode median std_dev")

def main():
    if len(sys.argv) == 1 or sys.argv[1] in ('-h','--help'):
        print("Usage: {0} file1 [file2 [...fileN]]".format(sys.argv[0]))
        sys.exit()
    numbers= []
    frequencies = collections.defaultdict(int)#默认字典，如果没有key则会默认创建一个新项，返回value
    for filename in sys.argv[1:]:
        read_data(filename,numbers,frequencies)
    if numbers:
        statistics = calculate_statistics(numbers,frequencies)
        print_results(len(numbers),statistics)
    else:
        print("no numbers found")

def read_data(filename,numbers,frequencies):
    for lino,line in enumerate(open(filename,encoding='ascii'),start=1):#lino是序号
        for x in line.split():
            try:
                number = float(x)
                numbers.append(number)
                frequencies[number] += 1
            except ValueError as err:
                print("{filename}:{lino}:skipping {x} : {err}".format(**locals()))

def calculate_statistics(numbers,frequencies):
    mean = sum(numbers) / len(numbers)
    mode = calculate_mode(frequencies,3)
    median = calculate_median(numbers)
    std_dev = calculate_std_dev(numbers,mean)
    return Statistics(mean,mode,median,std_dev)

def calculate_mode(frequencies,maximum_modes):
    highers_frequency = max(frequencies.values())
    mode = [number for number,freqency in frequencies.items() if freqency == highers_frequency]
    if not (1 <= len(mode) <= maximum_modes):
        mode = None
    else:
        mode.sort()
    return mode

def calculate_median(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        return (numbers[int(len(numbers) / 2)] + numbers[int((len(numbers) / 2) - 1)]) / 2
    else:
        return numbers[int((len(numbers) - 1) / 2)]

def calculate_std_dev(numbers,mean):
    total = 0
    for number in numbers:
        total += ((number - mean)**2)
    variance = total / (len(numbers) - 1)
    return math.sqrt(variance)

def print_results(count,statistics):
    real = '9.2f'
    if statistics.mode is None:
        modeline = ""
    elif len(statistics.mode) == 1:
        modeline = "mode        ={0:{fmt}}\n".format(statistics.mode[0],fmt=real)
    else:
        modeline = ("mode         =[" + ",".join(["{0:.2f}".format(m) for m in statistics.mode]) + "]\n")
    print("""\
          count      = {0:6}
          mean      = {mean:{fmt}}
          median   = {median:{fmt}}
          {1}\
          std.dev. = {std_dev:{fmt}}""".format(
          count,modeline,fmt = real,**statistics._asdict()))

if __name__ == '__main__':
    main()
