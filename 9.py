# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc.
import math


def task_9():
    n = 1000
    a = 1
    while a < n:
        b = a + 1
        while b < n:
            cSquared = (a ** 2) + (b ** 2)
            c = math.sqrt(cSquared)
            if c > b:
                if a + b + c == 1000:
                    return a * b * c
            b += 1
        a += 1

if __name__ == '__main__':
    print(task_9())
    ## answer is 31875000
    # a = 200
    # b = 375
    # c = 425