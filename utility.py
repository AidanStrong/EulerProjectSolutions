# fucntions to help with euler problems
import math


def isEven(num):
    if(num & 1):
        return False
    return True

def createFibSequenceWithMax(max):
    fibSequence = [1, 2]
    while True:
        lastNum = fibSequence[len(fibSequence) - 1]
        penultimateNum = fibSequence[len(fibSequence) - 2]
        if(lastNum + penultimateNum > max):
            break
        fibSequence.append(lastNum + penultimateNum)
    return fibSequence

def isPrime(num):

    if num == 2:
        return True

    if isEven(num):
        return False

    if num <= 1:
        return False
    sumOfDigits = 0

    for each in str(num):
        sumOfDigits += int(each)
    if sumOfDigits % 9 == 0:
        return False

    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def addZeroes(num):
    num *= 10;
    return num

if __name__ == '__main__':
    # print(isEven(0))
    # print(createFibSequenceWithMax(10))
    # print(isPrime(4239963954))
    print(addZeroes(3))

