# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

def task_17():
    n = 1000

    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", ""]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousand = "thousand"
    hundred = "hundred"

    sumOfLetters = 0
    for i in range(1, n +  1):
        print(i)
        if len(str(i)) == 1:
            sumOfLetters += len(digits[i - 1])
            print(digits[i - 1])

        if len(str(i)) == 2:
            if str(i)[0] == "1":
                sumOfLetters += len(teens[int(str(i)[1])])
            else:
                sumOfLetters += len(tens[int(str(i)[0]) - 1])
                if str(i)[1] != "0":
                    sumOfLetters += len(digits[int(str(i)[1]) - 1])

        if len(str(i)) == 3:
            sumOfLetters += len(digits[int(str(i)[0]) - 1])
            sumOfLetters += len(hundred)

            print(str(i)[2])
            if not(str(i)[1] == "0" and str(i)[2] == "0"):
                 sumOfLetters += len("and")
            if str(i)[1] == "1":
                sumOfLetters += len(teens[int(str(i)[2]) - 1])
            else:
                if str(i)[1] != "0": # if not just a digit
                   sumOfLetters += len(tens[int(str(i)[1]) - 1])
                sumOfLetters += len(digits[int(str(i)[2]) - 1])

        if len(str(i)) == 4:
            sumOfLetters += len(digits[int(str(i)[0]) - 1])
            sumOfLetters += len(thousand)
    return sumOfLetters

if __name__ == '__main__':
    print(task_17())
    # answer is 1366