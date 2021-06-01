# The sum of the squares of the first ten natural numbers is:
# 1^2 + 2^2 + ...+ 10^2 = 385
# The square of the sum of the first ten natural numbers is:
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def task_6():
    n = 100
    sumOfSquares = 0
    sum = 0
    for i in range(1, n + 1):
        sumOfSquares += i * i
        sum += i
    squareOfSum = sum * sum
    difference = squareOfSum - sumOfSquares
    return difference

if __name__ == '__main__':
    print(task_6())
    ## answer is 25164150
