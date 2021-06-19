# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million
from utility import *

def task_14():

    x = 1000000
    longestChain = 0
    store = [0 for i in range (0, (3 * x) + 1)]
    candidate = 1
    while candidate != x + 1:
        n = candidate
        chain = 1
        while n != 1:
            chain += 1
            if isEven(int(n)):
                n = n / 2
            else:
                n = (3 * n) + 1
            if n <= x:
                if store[int(n)] != 0:
                    chain += store[int(n)] - 1
                   # print("breaking because we already know", n, "has chain of", store[int(n)])
                    break
        store[candidate] = chain

        if chain > longestChain:
            longestChain = chain
            winningNum = candidate
        candidate += 1

    return winningNum


if __name__ == '__main__':
    print(task_14())
    # answer is 837799
