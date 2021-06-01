# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


from utility import *

#brute force algorithm, refined below
def task_10_brute_force():
    n = 2000000
    sum = 0
    while n != 0:
        if isPrime(n):
            sum += n
        n -= 1
    return sum

# Sieve of Eratosthenes is a known ancient algorithm for
# finding all prime numbers up to n
def sieve_of_eratosthenes(n):
    sum = 0
    numbers = [True for i in range (0, n + 1)]
    numbers[0] = False
    numbers[1] = False
    for j in range(0, n + 1):
        if numbers[j] == True:
            sum += j
            for i in range(2 * j, n + 1, j):
                numbers[i] = False
    return sum

if __name__ == '__main__':
    print(task_10_brute_force())
    # answer is 142913828922
    # easiest one yet...brute force not too slow...

    # but a faster way is sieve of Eratosthenes
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    print(sieve_of_eratosthenes(2000000))
    # this was about 23 times faster than the brute force
    # sieve of Eratosthenes took 536ms compared to brute force that took 12609ms

