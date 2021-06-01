# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from utility import *

def task_3():
    number = 600851475143
    largest = 0
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            if isPrime(i) is True:
                largest = i
            quotient = int(number / i)
            if (isPrime(quotient) == True):
                return (quotient)
    return largest

if __name__ == '__main__':
    print(task_3())
    ## answer is 6857
    print(600851475143/6857)