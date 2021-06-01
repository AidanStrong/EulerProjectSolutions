# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

import string

def task_4():
    a = 999
    b = 999
    largest = 0
    arr = [0,0]
    while a > 99:
        while b > 99:
            candidate = a * b
            if isPalindrome(candidate) == True:
                if candidate > largest:
                    largest = candidate
                    arr[0] = a
                    arr[1] = b
            b -= 1
        a -= 1
        b = 999
    print(arr)
    ## printing the array for a and b out of curiosity, values not actually needed
    return largest


def isPalindrome(n):
    n_string = str(n)
    firstpart = n_string[0:int(len(n_string) / 2)]
    secondpart = n_string[int(len(n_string) / 2):]
    reversedFirstPart = firstpart[::-1]
    if (reversedFirstPart == secondpart):
        return True
    return False

if __name__ == '__main__':
    print(task_4())
    ## answer is 906609
    ## two factors are 993 and 913
