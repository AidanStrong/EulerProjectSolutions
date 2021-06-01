# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def task_5():
    num = 20
    x = 20
    points = 0
    while True:
        print(x)
        for i in range(1, num + 1):
            if x % i == 0:
                points += 1
        if points == num:
            return x
        x += 20
        points = 0
    return x

if __name__ == '__main__':
    print(task_5())
    ## answer is 232792560
