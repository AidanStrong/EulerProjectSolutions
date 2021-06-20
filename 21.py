#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

def task_21(n):
    sumOfDivisors = [] # key:value, number: sum of divisors
    amicableNumbers = []
    for number in range(1, n + 1):
        divisors = []
        sum = 0
        for divisor in range(1, number):
            if number % divisor == 0:
                divisors.append(divisor)
        for each in divisors:
            sum += each
        sumOfDivisors.append(sum)

    for a in range(1, n + 1):
        if a not in amicableNumbers:
            b = sumOfDivisors[a - 1]
            if b - 1 <= n:
                if sumOfDivisors[b - 1] == a:
                    if a != b:
                        amicableNumbers.append(a)
                        amicableNumbers.append(b)

    sumOfAmicableNumbers = 0
    for each in amicableNumbers:
        sumOfAmicableNumbers += each
    print(amicableNumbers)
    return sumOfAmicableNumbers


if __name__ == '__main__':
    print(task_21(10000))
    #answer is 648
