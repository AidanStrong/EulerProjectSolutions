# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
from utility import *

def task_16():
    n = 1000
    nPower = 2 ** n
    nString = str(nPower)
    sum = 0
    for each in nString:
        sum += int(each)

    return sum

if __name__ == '__main__':
    print(task_16())
    # answer is 1366
