#

# It is possible to write five as a sum in exactly six different ways:
#
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at least two positive integers?

def task_76(n):
    combinations = 0
    for i in range(n - 1, 0, -1):
        print(i)

if __name__ == '__main__':
    print(task_76(5))
    #answer is
    #very fast algorithm, going to skip to problem 67 now to test it...
