
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from utility import *

def task_7():
    n = 10001
    currentPrime = 0
    count = 0
    candidate = 1

    while count < n:
        if isPrime(candidate) == True:
            count += 1
            currentPrime = candidate
        candidate += 1
    return currentPrime



if __name__ == '__main__':
    print(task_7())
    ## answer is 104743