# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!


def task_20(n):
    factors = []
    for i in range(1, n + 1):
        factors.append(i)
    print(factors)
    nFactorial = 1 * factors[len(factors) - 1]
    factors.pop()
    for each in factors:
        nFactorial *= each

    sumOfDigits = 0
    for char in str(nFactorial):
        sumOfDigits += int(char)

    return sumOfDigits

if __name__ == '__main__':
    print(task_20(100))
    #answer is 648
